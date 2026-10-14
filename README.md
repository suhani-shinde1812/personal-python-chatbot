# 🐍 Personal Python Question-Answering Chatbot

An intelligent, natural language question-answering chatbot dedicated to answering questions about Python programming using an NLP-powered predefined knowledge base.

---

## 📌 Problem Statement

> **Develop a simple personal chatbot that can answer questions related to Python programming.**
> 
> The chatbot should allow a user to enter a Python-related question in natural language and provide an appropriate answer based on a predefined Python knowledge base.

---

## ✨ Features

- **Natural Language Understanding (NLU)**: Accepts questions phrased naturally (e.g. *"Can you explain tuple vs list?"*, *"How do decorators work in Python?"*, *"What are \*args and \*\*kwargs?"*).
- **TF-IDF Vectorization & Cosine Similarity**: Uses standard, battle-tested Information Retrieval techniques via `scikit-learn` to calculate question similarity and rank best-matching answers.
- **Predefined Knowledge Base (62+ Encyclopedic Python Entries)**: Comprehensive coverage across **16 core topics**, including:
  - Python Overview, History, & Features
  - Zen of Python (`import this`) & Internals (`.pyc`, Bytecode, PVM)
  - Variables, Data Types & Dynamic Typing
  - Mutability vs. Immutability
  - String Operations, Slicing, & f-strings Formatting
  - Operators, Identity (`is`) vs Equality (`==`)
  - Lists, Tuples, Dictionaries, Sets, & Frozensets
  - Detailed comparisons (List vs Tuple, Shallow vs Deep Copy)
  - The `collections` module (`Counter`, `defaultdict`, `deque`, `namedtuple`)
  - Functions, Scope (LEGB Rule), `global` & `nonlocal`
  - `*args`, `**kwargs`, & Default Parameter Traps
  - Lambda Expressions, `map()`, `filter()`, & `reduce()`
  - Recursion & Call Stacks
  - List, Dict, & Set Comprehensions
  - Iterators & Iterables (`iter()`, `next()`, `StopIteration`)
  - Generators & `yield`
  - Object-Oriented Programming (Classes, Objects, `__init__`, `self`)
  - Instance vs Class vs Static Methods (`@classmethod`, `@staticmethod`)
  - Inheritance, Multiple Inheritance & MRO (C3 Linearization)
  - Polymorphism & Duck Typing
  - Encapsulation, Access Modifiers, & Name Mangling
  - Abstraction (`abc` module, `@abstractmethod`)
  - Dunder / Magic Methods (`__str__`, `__repr__`, `__len__`, `__getitem__`, `__add__`)
  - Properties (`@property`, getters/setters) & Dataclasses (`@dataclass`)
  - Decorators & Closures (`functools.wraps`)
  - Exception Handling (`try...except...else...finally`) & Custom Exceptions
  - File I/O (`open()`, modes, `with` context managers)
  - JSON serialization & deserialization (`loads`, `dumps`, `load`, `dump`)
  - Modules, Packages, `sys.path`, & `if __name__ == '__main__':`
  - Environments & Packaging (`pip`, `venv`, `requirements.txt`)
  - Concurrency & Internals: Global Interpreter Lock (GIL)
  - Multithreading vs Multiprocessing
  - Asynchronous Concurrency with `asyncio` (`async`/`await`)
  - Memory Management & Generational Garbage Collection (`gc`)
  - Clean Code & Style: PEP 8 Standards
- **Typo & Variation Tolerance**: Automatically handles common user misspellings (e.g., *"pythin"*, *"decorater"*, *"tupel"*, *"inheretance"*).
- **Executable Code Snippets**: Every technical explanation includes a copyable, syntactically clean code example.
- **Dual Interfaces**:
  1. **Interactive Web App**: Modern UI featuring quick topic pills, confidence percentage badges, syntax-highlighted code blocks with 1-click copy, dynamic suggestion chips, and responsive layout.
  2. **Terminal CLI Mode**: Terminal experience (`python chatbot.py`) for quick command-line grading or headless testing.
- **Graceful Fallback & Suggestions**: When an out-of-domain query is asked (e.g., *"What is the capital of France?"*), the chatbot politely informs the user and provides suggestions of valid Python questions.

---

## 📂 Project Architecture

```
Personal Chatbot/
├── knowledge_base.json     # Predefined Python QA dataset (patterns, answers, code, topics)
├── nlp_engine.py          # TF-IDF vectorizer, cosine similarity matching & scoring engine
├── chatbot.py             # Chatbot class with session history & interactive CLI mode
├── app.py                 # Flask web server providing REST API & serving web UI
├── test_chatbot.py        # Automated unit tests covering queries, edge cases & fallback
├── requirements.txt       # Project dependencies
├── templates/
│   └── index.html         # Web application template
└── static/
    ├── css/
    │   └── style.css      # Dark modern theme, glassmorphism, responsive styling
    └── js/
        └── app.js         # Frontend interactivity, API communication & code copying
```

---

## 🚀 Getting Started

### 1. Prerequisites

Python 3.9+ installed on your system.

### 2. Installation

Install the required dependencies:

```bash
pip install -r requirements.txt
```

*(Dependencies: `flask`, `flask-cors`, `scikit-learn`, `numpy`)*

---

## 💻 How to Run

### Option A: Web Application (Recommended)

Start the Flask web server:

```bash
python app.py
```

Then open your browser to:
👉 **[http://127.0.0.1:5500](http://127.0.0.1:5500)**

*(On Windows PowerShell, you can launch it directly with: `start http://127.0.0.1:5500`)*

#### In the Web UI you can:
- Type any question in the input box and hit **Enter**.
- Click any **Topic Pill** on the sidebar to filter questions.
- Click any **Suggestion Chip** below the answers to chain questions.
- Click **"Copy"** on any code snippet box to copy code to your clipboard.
- Use **"Clear History"** to reset conversation.

---

### Option B: Terminal CLI Interface

To run directly inside your terminal or command prompt:

```bash
python chatbot.py
```

#### Terminal Commands:
- Type your question in natural language (e.g., `What is list comprehension?`)
- Type `topics` to list all available topics in the knowledge base.
- Type `samples` to view sample questions.
- Type `help` to view help.
- Type `exit` to quit.

---

### Option C: Deploy to Render (Cloud Hosting)

This repository includes a `render.yaml` and `Procfile` configured for 1-click Render deployment:

1. Sign in to [Render.com](https://render.com).
2. Click **New +** ➔ **Web Service**.
3. Connect your GitHub repository: `suhani-shinde1812/personal-python-chatbot`.
4. Render will auto-fill the settings:
   - **Environment**: `Python`
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `gunicorn app:app`
5. Click **Create Web Service** (Free tier). Render will build and provide a live public URL (e.g. `https://personal-python-chatbot.onrender.com`).

---

## 🧪 Running Automated Tests

Run the test suite to verify question matching, text cleaning, paraphrase recognition, and fallback handling:

```bash
python -m unittest test_chatbot.py
```

Expected output:
```
.......
----------------------------------------------------------------------
Ran 7 tests in 0.033s

OK
```

---

## 📝 Sample Questions to Try

1. *"What is Python?"*
2. *"What is the difference between list and tuple?"*
3. *"How do *args and **kwargs work in Python?"*
4. *"Explain class and inheritance in Python"*
5. *"What does __init__ and self do?"*
6. *"How to handle exceptions using try except?"*
7. *"What is a decorator in Python?"*
8. *"What is the Global Interpreter Lock (GIL)?"*
9. *"How to read and write files in Python?"*
10. *"What is PEP 8?"*
