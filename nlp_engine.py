import json
import os
import re
import difflib
from typing import Dict, List, Optional, Tuple
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Common programming typos and synonyms to normalize
COMMON_TYPOS = {
    "differe": "difference",
    "diffrence": "difference",
    "diffrnce": "difference",
    "pythin": "python",
    "pythn": "python",
    "pthon": "python",
    "pyhton": "python",
    "functon": "function",
    "functons": "functions",
    "func": "function",
    "funcs": "functions",
    "decorater": "decorator",
    "decoraters": "decorators",
    "dictonary": "dictionary",
    "dictonaries": "dictionaries",
    "dict": "dictionary",
    "dicts": "dictionaries",
    "tupel": "tuple",
    "tupels": "tuples",
    "inheretance": "inheritance",
    "comprehention": "comprehension",
    "comprehentions": "comprehensions",
    "excepton": "exception",
    "exceptons": "exceptions",
    "variabel": "variable",
    "variabels": "variables",
    "lamda": "lambda",
    "args": "*args",
    "kwargs": "**kwargs",
    "lib": "library",
    "libs": "libraries",
    "libary": "library",
    "libaries": "libraries",
    "libraris": "libraries",
    "librari": "library"
}


def clean_text(text: str) -> str:
    """Preprocess text by lowercasing, preserving operator symbols, and correcting typos."""
    text = text.lower().strip()
    # Normalize equality operators so they don't get stripped by punctuation cleaner
    text = text.replace("===", " triple_equal ")
    text = text.replace("==", " double_equal ")
    text = text.replace("!=", " not_equal ")
    # Normalize punctuation but retain * and _ for Python specifics (*args, __init__)
    text = re.sub(r"[^\w\s\*\_\-]", " ", text)
    tokens = text.split()

    # Apply typo corrections
    corrected = [COMMON_TYPOS.get(t, t) for t in tokens]
    return " ".join(corrected).strip()


class PythonChatbotEngine:
    """NLP Question-Answering engine using TF-IDF and Cosine Similarity."""

    def __init__(self, kb_path: str = "knowledge_base.json", min_similarity_threshold: float = 0.16):
        self.kb_path = kb_path
        self.min_similarity_threshold = min_similarity_threshold
        self.knowledge_base: List[Dict] = []
        self.corpus: List[str] = []
        self.entry_index_map: List[int] = []  # Maps corpus row to knowledge_base entry index
        self.vectorizer: Optional[TfidfVectorizer] = None
        self.tfidf_matrix = None
        self.all_keywords: List[str] = []
        self.load_knowledge_base()
        self._build_index()

    def load_knowledge_base(self):
        """Loads knowledge base from JSON file."""
        if not os.path.exists(self.kb_path):
            raise FileNotFoundError(f"Knowledge base file not found at {self.kb_path}")
        with open(self.kb_path, "r", encoding="utf-8") as f:
            self.knowledge_base = json.load(f)

    def _build_index(self):
        """Builds TF-IDF vector space over patterns, keywords, and topics."""
        self.corpus = []
        self.entry_index_map = []
        all_kw_set = set()

        for idx, entry in enumerate(self.knowledge_base):
            patterns = entry.get("patterns", [])
            keywords = entry.get("keywords", [])
            topic = entry.get("topic", "")

            for kw in keywords:
                all_kw_set.add(kw.lower())

            # Add each pattern as a distinct corpus document linked to this entry
            for pattern in patterns:
                combined_text = f"{pattern} {' '.join(keywords)} {topic}"
                self.corpus.append(clean_text(combined_text))
                self.entry_index_map.append(idx)

            # Add an entry with all keywords, topic, and id
            kw_text = f"{' '.join(keywords)} {topic} {entry.get('id', '')}"
            self.corpus.append(clean_text(kw_text))
            self.entry_index_map.append(idx)

        self.all_keywords = list(all_kw_set)

        # Fit TF-IDF with unigrams and bigrams
        self.vectorizer = TfidfVectorizer(
            ngram_range=(1, 2),
            sublinear_tf=True,
            stop_words="english"
        )
        self.tfidf_matrix = self.vectorizer.fit_transform(self.corpus)

    def get_entry_by_id(self, item_id: str) -> Optional[Dict]:
        """Retrieve an entry by its ID."""
        for item in self.knowledge_base:
            if item["id"] == item_id:
                return item
        return None

    def get_all_topics(self) -> List[str]:
        """Returns unique topics available in the knowledge base."""
        topics = []
        for item in self.knowledge_base:
            t = item.get("topic", "General")
            if t not in topics:
                topics.append(t)
        return topics

    def get_sample_questions(self, count: int = 8) -> List[Dict]:
        """Returns a curated list of sample questions."""
        samples = []
        for item in self.knowledge_base[:count]:
            samples.append({
                "id": item["id"],
                "question": item["patterns"][0],
                "topic": item["topic"]
            })
        return samples

    def answer_query(self, user_query: str) -> Dict:
        """
        Finds the most appropriate answer for the user's natural language question.
        Returns response dictionary with matched entry, confidence score, and suggestions.
        """
        cleaned_query = clean_text(user_query)

        # Handle greetings and casual queries
        greetings = ["hi", "hello", "hey", "greetings", "good morning", "good evening", "howdy", "sup"]
        if cleaned_query in greetings or cleaned_query.startswith("hello ") or cleaned_query.startswith("hi "):
            return {
                "matched": True,
                "confidence": 1.0,
                "answer": "Hello! I am your personal Python Question-Answering Chatbot. I have a comprehensive knowledge base covering Python from fundamentals (variables, data types, loops) to advanced topics (OOP, decorators, generators, GIL, asyncio, and memory management). Ask me anything!",
                "topic": "Greeting",
                "code_example": "# Example: Ask me about any Python concept!\n# Try: 'What is the difference between list and tuple?'\n# Or: 'How do decorators work in Python?'",
                "related_questions": [
                    "What is Python?",
                    "What is the difference between list and tuple in Python?",
                    "How do decorators work in Python?",
                    "What are *args and **kwargs in Python?",
                    "Explain the Zen of Python"
                ]
            }

        # Vectorize user query
        query_vec = self.vectorizer.transform([cleaned_query])
        similarities = cosine_similarity(query_vec, self.tfidf_matrix).flatten()

        # Aggregate maximum similarity per knowledge_base entry
        entry_scores: Dict[int, float] = {}
        for corpus_idx, score in enumerate(similarities):
            entry_idx = self.entry_index_map[corpus_idx]
            current_max = entry_scores.get(entry_idx, 0.0)
            if score > current_max:
                entry_scores[entry_idx] = float(score)

        # Keyword boost: if exact technical terms or fuzzy matches appear in query
        query_tokens = set(cleaned_query.split())
        for entry_idx, entry in enumerate(self.knowledge_base):
            entry_keywords = {k.lower() for k in entry.get("keywords", [])}
            overlap = query_tokens.intersection(entry_keywords)
            if overlap:
                boost = 0.18 * len(overlap)
                entry_scores[entry_idx] = entry_scores.get(entry_idx, 0.0) + boost

            # Specific comparison boost: if query asks for difference / vs
            if any(term in cleaned_query for term in ["vs", "versus", "difference", "compare"]) and "vs" in entry.get("id", ""):
                entry_scores[entry_idx] = entry_scores.get(entry_idx, 0.0) + 0.25

            # Boost for === / == query
            if "triple_equal" in query_tokens and entry.get("id") == "equal_vs_triple_equal":
                entry_scores[entry_idx] = entry_scores.get(entry_idx, 0.0) + 0.55

            # Boost for library / libraries query
            if ("library" in query_tokens or "libraries" in query_tokens) and entry.get("id") == "python_libraries":
                entry_scores[entry_idx] = entry_scores.get(entry_idx, 0.0) + 0.45

        # Sort entries by final score
        sorted_entries = sorted(entry_scores.items(), key=lambda x: x[1], reverse=True)

        if not sorted_entries:
            return self._build_fallback_response(cleaned_query)

        best_idx, best_score = sorted_entries[0]
        best_entry = self.knowledge_base[best_idx]

        # Gather related question suggestions from other top matches or related_topics
        suggestions = []
        for rel_id in best_entry.get("related_topics", []):
            rel_entry = self.get_entry_by_id(rel_id)
            if rel_entry and rel_entry["patterns"]:
                suggestions.append(rel_entry["patterns"][0])

        for other_idx, score in sorted_entries[1:5]:
            other_entry = self.knowledge_base[other_idx]
            if other_entry["patterns"] and other_entry["patterns"][0] not in suggestions:
                suggestions.append(other_entry["patterns"][0])

        suggestions = suggestions[:4]

        # Check threshold
        if best_score < self.min_similarity_threshold:
            return self._build_fallback_response(cleaned_query, suggestions)

        return {
            "matched": True,
            "id": best_entry["id"],
            "topic": best_entry.get("topic", "General"),
            "matched_question": best_entry["patterns"][0],
            "confidence": round(float(best_score), 3),
            "answer": best_entry["answer"],
            "code_example": best_entry.get("code_example", ""),
            "related_questions": suggestions
        }

    def _build_fallback_response(self, query: str, suggestions: Optional[List[str]] = None) -> Dict:
        """Returns a helpful fallback response when confidence is below threshold."""
        if not suggestions:
            suggestions = [
                "What is the difference between list and tuple in Python?",
                "What are *args and **kwargs in Python?",
                "How does inheritance work in Python?",
                "What is a decorator in Python?",
                "What is the Global Interpreter Lock (GIL)?"
            ]

        return {
            "matched": False,
            "confidence": 0.0,
            "answer": f"I couldn't find a direct match for \"{query}\" in my predefined Python knowledge base. Here are some related Python concepts you can ask me about:",
            "topic": "Not Found",
            "code_example": "",
            "related_questions": suggestions
        }


if __name__ == "__main__":
    engine = PythonChatbotEngine()
    test_queries = [
        "What is Python?",
        "Difference between list and tuple",
        "How do *args work?",
        "what is pythin",
        "explain dunder methods in python",
        "what is the gil?",
        "What is the capital of France?"
    ]
    for q in test_queries:
        print("Query:", q)
        res = engine.answer_query(q)
        print("Matched:", res["matched"], "| Confidence:", res["confidence"], "| Topic:", res.get("topic"))
        print("Answer preview:", res["answer"][:75], "...")
        print("-" * 50)
