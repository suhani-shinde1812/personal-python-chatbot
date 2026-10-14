"""
Unit and Integration Tests for Python QA Chatbot
"""

import unittest
from chatbot import PythonChatbot
from nlp_engine import PythonChatbotEngine, clean_text


class TestPythonChatbot(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.chatbot = PythonChatbot(kb_path="knowledge_base.json")
        cls.engine = cls.chatbot.engine

    def test_knowledge_base_loaded(self):
        """Verify knowledge base is loaded with entries having required fields."""
        self.assertGreater(len(self.engine.knowledge_base), 0)
        required_keys = {"id", "topic", "patterns", "keywords", "answer"}
        for entry in self.engine.knowledge_base:
            self.assertTrue(required_keys.issubset(entry.keys()), f"Missing keys in {entry.get('id')}")
            self.assertIsInstance(entry["patterns"], list)
            self.assertGreater(len(entry["patterns"]), 0)

    def test_clean_text(self):
        """Test text preprocessing logic."""
        raw = "What is a LIST in Python!?!?"
        cleaned = clean_text(raw)
        self.assertEqual(cleaned, "what is a list in python")

        special = "How do *args and __init__ work?"
        cleaned_special = clean_text(special)
        self.assertIn("*args", cleaned_special)
        self.assertIn("__init__", cleaned_special)

    def test_exact_match_queries(self):
        """Test exact queries from knowledge base patterns."""
        queries = [
            ("What is Python?", "what_is_python"),
            ("What is the difference between list and tuple in Python?", "list_vs_tuple"),
            ("What are *args and **kwargs in Python?", "args_kwargs"),
            ("What is a decorator in Python?", "decorators"),
            ("What is GIL in Python?", "gil")
        ]
        for query, expected_id in queries:
            res = self.chatbot.ask(query)
            self.assertTrue(res["matched"], f"Failed to match query: {query}")
            self.assertEqual(res.get("id"), expected_id, f"Wrong ID for query: {query}")
            self.assertGreater(res["confidence"], 0.25)

    def test_paraphrased_natural_language_queries(self):
        """Test variations and natural language queries."""
        variations = [
            ("can you explain tuple vs list", "list_vs_tuple"),
            ("tell me how to handle try except errors", "exception_handling"),
            ("how do i write classes and objects", "oop_basics"),
            ("what is constructor dunder init", "init_method"),
            ("anonymous lambda function usage", "lambda_functions")
        ]
        for query, expected_id in variations:
            res = self.chatbot.ask(query)
            self.assertTrue(res["matched"], f"Failed to match variation: {query}")
            self.assertEqual(res.get("id"), expected_id, f"Wrong match for {query}: got {res.get('id')}")

    def test_greeting_handling(self):
        """Test greeting response."""
        res = self.chatbot.ask("Hello")
        self.assertTrue(res["matched"])
        self.assertEqual(res["topic"], "Greeting")
        self.assertIn("Python", res["answer"])

    def test_typo_tolerance(self):
        """Test that common typos like 'pythin', 'decorater', 'tupel' still match accurately."""
        typo_queries = [
            ("what is pythin", "what_is_python"),
            ("how do decoraters work", "decorators"),
            ("explain list vs tupel", "list_vs_tuple"),
            ("how does inheretance work", "inheritance")
        ]
        for query, expected_id in typo_queries:
            res = self.chatbot.ask(query)
            self.assertTrue(res["matched"], f"Failed to match typo query: {query}")
            self.assertEqual(res.get("id"), expected_id, f"Wrong match for typo {query}: {res.get('id')}")

    def test_advanced_topics(self):
        """Test advanced Python concepts like asyncio, memory management, and dataclasses."""
        advanced = [
            ("what is asyncio and coroutines", "asyncio_concurrency"),
            ("how does garbage collection work in python", "memory_management_gc"),
            ("what is a dataclass in python", "dataclasses"),
            ("explain multiple inheritance and mro", "multiple_inheritance_and_mro"),
            ("what is the zen of python", "zen_of_python")
        ]
        for query, expected_id in advanced:
            res = self.chatbot.ask(query)
            self.assertTrue(res["matched"], f"Failed on advanced query: {query}")
            self.assertEqual(res.get("id"), expected_id, f"Wrong match for {query}: {res.get('id')}")

    def test_equality_and_libraries_queries(self):
        """Test == vs === and python libraries queries."""
        test_cases = [
            ("the differe between == and ===", "equal_vs_triple_equal"),
            ("== vs ===", "equal_vs_triple_equal"),
            ("Does Python have === operator?", "equal_vs_triple_equal"),
            ("libraries in python", "python_libraries"),
            ("answer of libraries in python", "python_libraries"),
            ("What is a library in Python?", "python_libraries")
        ]
        for query, expected_id in test_cases:
            res = self.chatbot.ask(query)
            self.assertTrue(res["matched"], f"Failed to match query: {query}")
            self.assertEqual(res.get("id"), expected_id, f"Wrong match for {query}: got {res.get('id')}")

    def test_chat_history_recording(self):
        """Verify chat history tracking and clearing."""
        self.chatbot.clear_history()
        self.assertEqual(len(self.chatbot.history), 0)

        self.chatbot.ask("What is Python?")
        self.assertEqual(len(self.chatbot.history), 1)
        self.assertEqual(self.chatbot.history[0]["user"], "What is Python?")

        self.chatbot.clear_history()
        self.assertEqual(len(self.chatbot.history), 0)


if __name__ == "__main__":
    unittest.main()

