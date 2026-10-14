"""
Python Question-Answering Chatbot
CLI & Core Application Module
"""

import sys
import os
from typing import List, Dict
from nlp_engine import PythonChatbotEngine


class PythonChatbot:
    """Manages chatbot state, chat history, and question-answering interactions."""

    def __init__(self, kb_path: str = "knowledge_base.json"):
        self.engine = PythonChatbotEngine(kb_path=kb_path)
        self.history: List[Dict] = []

    def ask(self, query: str) -> Dict:
        """Processes a query, records conversation history, and returns the response."""
        response = self.engine.answer_query(query)
        self.history.append({
            "user": query,
            "bot": response
        })
        return response

    def get_topics(self) -> List[str]:
        return self.engine.get_all_topics()

    def get_sample_questions(self) -> List[Dict]:
        return self.engine.get_sample_questions()

    def clear_history(self):
        self.history.clear()


def run_cli():
    """Interactive command-line interface for the Python QA Chatbot."""
    if sys.stdout.encoding != "utf-8":
        try:
            sys.stdout.reconfigure(encoding="utf-8")
        except AttributeError:
            pass

    chatbot = PythonChatbot()

    banner = """
========================================================================
       🐍 WELCOME TO THE PERSONAL PYTHON QA CHATBOT 🐍
========================================================================
 Ask me any question related to Python programming!
 
 Commands:
   - 'help'    : Display this help message
   - 'topics'  : View all available Python topics in knowledge base
   - 'samples' : View sample questions you can ask
   - 'exit'    : Quit the chatbot
========================================================================
"""
    print(banner)

    while True:
        try:
            user_input = input("\n🧑 You: ").strip()
            if not user_input:
                continue

            lower_cmd = user_input.lower()
            if lower_cmd in ["exit", "quit", "q"]:
                print("\n👋 Goodbye! Happy Python coding!\n")
                break

            if lower_cmd == "help":
                print("\n💡 Type any Python question naturally, e.g.:")
                print("   - 'What is the difference between list and tuple?'")
                print("   - 'How do decorators work in Python?'")
                print("   - 'What is the Global Interpreter Lock (GIL)?'")
                continue

            if lower_cmd == "topics":
                print("\n📚 Available Topics:")
                for idx, t in enumerate(chatbot.get_topics(), 1):
                    print(f"   {idx}. {t}")
                continue

            if lower_cmd == "samples":
                print("\n✨ Sample Questions to Ask:")
                for item in chatbot.get_sample_questions():
                    print(f"   • {item['question']} [{item['topic']}]")
                continue

            # Process QA query
            res = chatbot.ask(user_input)

            print(f"\n🤖 Bot [{res.get('topic', 'General')}]:")
            print(f"{res['answer']}")

            if res.get("code_example"):
                print("\n💻 Code Example:")
                print("----------------------------------------")
                print(res["code_example"])
                print("----------------------------------------")

            if res.get("related_questions"):
                print("\n🔍 Related Questions:")
                for q in res["related_questions"][:3]:
                    print(f"   ➜ {q}")

        except (KeyboardInterrupt, EOFError):
            print("\n\n👋 Exiting chatbot. Have a great day!")
            break


if __name__ == "__main__":
    run_cli()
