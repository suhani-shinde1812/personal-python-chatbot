"""
Builds an encyclopedic knowledge base covering all facets of Python programming.
"""

import json

entries = [
    {
        "id": "what_is_python",
        "topic": "Python Basics",
        "patterns": [
            "What is Python?",
            "Tell me about Python",
            "What is Python programming language?",
            "Why use Python?",
            "Introduce Python"
        ],
        "keywords": ["python", "language", "overview", "introduction", "features", "guido", "interpreted"],
        "answer": "Python is a high-level, interpreted, dynamically typed, and garbage-collected programming language created by Guido van Rossum in 1991. It emphasizes readability with its clean syntax and use of significant indentation. Python supports multiple paradigms including Object-Oriented, Functional, and Procedural programming.",
        "code_example": "# Print Hello World\nprint('Hello, Python World!')",
        "related_topics": ["python_features", "interpreted_vs_compiled", "zen_of_python"]
    },
    {
        "id": "python_features",
        "topic": "Python Basics",
        "patterns": [
            "What are the key features of Python?",
            "Why is Python so popular?",
            "What makes Python special?",
            "Advantages of Python"
        ],
        "keywords": ["features", "benefits", "advantages", "popular", "simple", "portable", "interpreted"],
        "answer": "Core features of Python:\n1. **Simple & Readable**: Clean, English-like syntax.\n2. **Interpreted**: Executes line-by-line without explicit manual compilation step.\n3. **Dynamically Typed**: Types are verified and bound at runtime.\n4. **Batteries Included**: Vast standard library for math, networking, OS, and file I/O.\n5. **Cross-Platform**: Runs on Windows, Linux, macOS.\n6. **Extensible**: Integrates easily with C, C++, and Java.",
        "code_example": "x = 42        # int\nx = 'hello'   # dynamically rebound to str\nprint(x, type(x))",
        "related_topics": ["what_is_python", "interpreted_vs_compiled"]
    },
    {
        "id": "interpreted_vs_compiled",
        "topic": "Python Basics",
        "patterns": [
            "Is Python interpreted or compiled?",
            "How does Python execute code?",
            "Explain Python bytecode and CPython",
            "How Python works under the hood"
        ],
        "keywords": ["interpreted", "compiled", "bytecode", ".pyc", "cpython", "pvm", "virtual machine"],
        "answer": "Python is both compiled and interpreted! When you run a script, the CPython compiler first compiles the source code (`.py`) into intermediate bytecode (`.pyc` files in `__pycache__`). Then, the Python Virtual Machine (PVM) interprets and executes this bytecode instruction by instruction.",
        "code_example": "# Inspect bytecode using the dis module\nimport dis\n\ndef add(a, b):\n    return a + b\n\ndis.dis(add)",
        "related_topics": ["what_is_python", "gil"]
    },
    {
        "id": "zen_of_python",
        "topic": "Python Basics",
        "patterns": [
            "What is the Zen of Python?",
            "How to see Zen of Python?",
            "Guiding principles of Python",
            "import this"
        ],
        "keywords": ["zen of python", "tim peters", "import this", "philosophy", "principles"],
        "answer": "The Zen of Python is a collection of 19 guiding design aphorisms written by Tim Peters. Key maxims include:\n- Beautiful is better than ugly.\n- Explicit is better than implicit.\n- Simple is better than complex.\n- Readability counts.\n- There should be one-- and preferably only one --obvious way to do it.",
        "code_example": "# Run in Python interpreter:\nimport this",
        "related_topics": ["pep8", "what_is_python"]
    },
    {
        "id": "variables_datatypes",
        "topic": "Data Types",
        "patterns": [
            "What are variables and data types in Python?",
            "How do variables work in Python?",
            "What data types exist in Python?",
            "List of Python data types"
        ],
        "keywords": ["variables", "data types", "int", "float", "str", "bool", "none", "types"],
        "answer": "Variables are named references (pointers) to objects in memory. You don't declare types explicitly.\n\nBuilt-in data types:\n- **Numeric**: `int`, `float`, `complex`\n- **Sequence**: `str`, `list`, `tuple`, `range`\n- **Mapping**: `dict`\n- **Set**: `set`, `frozenset`\n- **Boolean**: `bool` (`True`, `False`)\n- **Binary**: `bytes`, `bytearray`\n- **None**: `NoneType` (`None`)",
        "code_example": "name = 'Guido'     # str\nage = 65            # int\nratio = 3.14159     # float\nis_active = True    # bool\ndata = None         # NoneType",
        "related_topics": ["type_casting", "mutability_immutability"]
    },
    {
        "id": "type_casting",
        "topic": "Data Types",
        "patterns": [
            "What is type casting in Python?",
            "How to convert data types in Python?",
            "Type conversion implicit explicit"
        ],
        "keywords": ["type casting", "conversion", "int()", "str()", "float()", "typecast"],
        "answer": "Type casting is converting a value from one data type to another:\n1. **Implicit Conversion**: Performed automatically by Python (e.g., adding `int` and `float` produces `float`).\n2. **Explicit Conversion**: Performed manually using built-in constructors: `int()`, `float()`, `str()`, `list()`, `tuple()`, `set()`, `bool()`.",
        "code_example": "val_str = '100'\nval_int = int(val_str)      # 100\nval_float = float(val_int)  # 100.0\nval_bool = bool(val_int)    # True",
        "related_topics": ["variables_datatypes"]
    },
    {
        "id": "mutability_immutability",
        "topic": "Data Types",
        "patterns": [
            "What is mutable and immutable in Python?",
            "Difference between mutable and immutable data types",
            "Which objects are immutable in Python?",
            "Explain mutability"
        ],
        "keywords": ["mutable", "immutable", "mutability", "id()", "state", "changeable"],
        "answer": "- **Mutable**: Objects whose state or contents can be modified after creation without changing their memory address (`id`). Examples: `list`, `dict`, `set`, `bytearray`.\n- **Immutable**: Objects whose value cannot be altered once created. Any modification creates a new object in memory. Examples: `int`, `float`, `str`, `tuple`, `frozenset`, `bool`.",
        "code_example": "# Mutable list\na = [1, 2]\na.append(3)   # Same id, modified in-place\n\n# Immutable string\ns = 'hello'\n# s[0] = 'H'  # TypeError! Must create new string:\ns = 'H' + s[1:]",
        "related_topics": ["lists", "tuples", "shallow_vs_deep_copy"]
    },
    {
        "id": "strings_and_methods",
        "topic": "Strings",
        "patterns": [
            "How do strings work in Python?",
            "What are common string methods in Python?",
            "String slicing and manipulation in Python",
            "Explain string methods"
        ],
        "keywords": ["string", "str", "slice", "split", "join", "strip", "replace", "upper", "lower"],
        "answer": "Strings in Python are immutable sequences of Unicode characters enclosed in single, double, or triple quotes.\n\nCommon methods:\n- `s.split(sep)`: Splits string into list of substrings.\n- `sep.join(list)`: Concatenates iterable with separator.\n- `s.strip()`: Trims leading/trailing whitespace.\n- `s.replace(old, new)`: Replaces occurrences.\n- `s.find(sub)` / `s.startswith(sub)` / `s.endswith(sub)`: Search string.\n- `s[start:stop:step]`: String slicing.",
        "code_example": "msg = '  python programming  '\ncleaned = msg.strip().title()      # 'Python Programming'\nwords = cleaned.split()            # ['Python', 'Programming']\njoined = '-'.join(words)           # 'Python-Programming'\nreversed_str = cleaned[::-1]       # Slicing reverse",
        "related_topics": ["string_formatting", "mutability_immutability"]
    },
    {
        "id": "string_formatting",
        "topic": "Strings",
        "patterns": [
            "How to format strings in Python?",
            "What are f-strings in Python?",
            "Difference between f-strings and format()",
            "String interpolation in Python"
        ],
        "keywords": ["f-strings", "format", "string formatting", "% formatting", "interpolation"],
        "answer": "Python provides 3 ways to format strings:\n1. **f-strings (Formatted String Literals)** (Python 3.6+): Prefix with `f`, embed expressions inside `{}`. Fastest, most readable, and recommended.\n2. **`str.format()`**: Uses `{}` placeholders (e.g. `'Hello, {}'.format(name)`).\n3. **`%` formatting (printf-style)**: Legacy style (e.g. `'Hello, %s' % name`).",
        "code_example": "item = 'Book'\nprice = 29.99\n\n# f-string with formatting expression\nprint(f'{item} costs ${price:.2f}')\n# Expressions inside f-strings\nprint(f'Total with tax: ${price * 1.08:.2f}')",
        "related_topics": ["strings_and_methods"]
    },
    {
        "id": "operators",
        "topic": "Operators",
        "patterns": [
            "What operators exist in Python?",
            "Explain arithmetic, logical, and comparison operators in Python",
            "Python operators overview",
            "Bitwise and membership operators"
        ],
        "keywords": ["operators", "arithmetic", "logical", "comparison", "bitwise", "membership", "in", "and", "or", "not"],
        "answer": "Python operators:\n1. **Arithmetic**: `+`, `-`, `*`, `/` (float div), `//` (floor div), `%` (modulus), `**` (exponentiation).\n2. **Comparison**: `==`, `!=`, `>`, `<`, `>=`, `<=`.\n3. **Logical**: `and`, `or`, `not`.\n4. **Identity**: `is`, `is not` (checks memory address identity).\n5. **Membership**: `in`, `not in` (checks membership in sequence/collection).\n6. **Bitwise**: `&`, `|`, `^`, `~`, `<<`, `>>`.",
        "code_example": "print(7 // 2)      # 3 (floor division)\nprint(2 ** 4)      # 16 (exponentiation)\nprint(5 in [1, 5]) # True (membership)\nprint(True and False) # False (logical)",
        "related_topics": ["is_vs_equal"]
    },
    {
        "id": "is_vs_equal",
        "topic": "Operators",
        "patterns": [
            "What is the difference between is and == in Python?",
            "is vs == in Python",
            "Difference between identity and equality in Python",
            "When to use is vs =="
        ],
        "keywords": ["is vs ==", "identity", "equality", "id()", "compare", "comparison"],
        "answer": "- `==` checks for **Equality of Values**: It tests whether the values of two objects are equal by calling `__eq__()`.\n- `is` checks for **Identity**: It tests whether two variables point to the exact same object in memory (`id(a) == id(b)`).\n\n**Best Practice**: Always use `is` when checking against `None` (e.g., `if val is None:`).",
        "code_example": "a = [1, 2, 3]\nb = [1, 2, 3]\n\nprint(a == b)  # True (same values)\nprint(a is b)  # False (different objects in memory)\n\nc = a\nprint(a is c)  # True (both point to same memory address)",
        "related_topics": ["operators", "mutability_immutability"]
    },
    {
        "id": "equal_vs_triple_equal",
        "topic": "Operators",
        "patterns": [
            "What is the difference between == and === in Python?",
            "Difference between == and ===",
            "Does Python have a === operator?",
            "== vs ===",
            "Why does Python not have ===?",
            "How does strict equality work in Python compared to JavaScript?"
        ],
        "keywords": ["==", "===", "triple_equal", "double_equal", "strict equality", "equality", "syntaxerror", "is operator"],
        "answer": "In Python, **there is NO `===` operator**!\n\n1. **In Python**:\n   - `==` is the equality operator. It compares values (checking if two objects have equal values by calling `__eq__()`).\n   - Python does not have or support `===`. Attempting to write `a === b` raises a `SyntaxError: invalid syntax`.\n   - If you want strict object identity comparison (checking whether two variables refer to the exact same object in memory, like `===` in languages like JavaScript), Python uses the `is` keyword instead.\n\n2. **Summary**:\n   - Value comparison: Use `==` (e.g., `5 == 5.0` is `True`)\n   - Identity/reference comparison: Use `is` (e.g., `5 is 5.0` is `False`)\n   - `===`: Does NOT exist in Python syntax.",
        "code_example": "# 1. Value equality with ==\nprint(5 == 5.0)    # True (values are mathematically equal)\n\n# 2. Strict identity with 'is'\nprint(5 is 5.0)    # False (different types and memory addresses)\n\n# 3. Trying to use === in Python:\n# result = (5 === 5)  # Raises SyntaxError: invalid syntax",
        "related_topics": ["is_vs_equal", "operators", "variables_datatypes"]
    },
    {
        "id": "lists",
        "topic": "Data Structures",
        "patterns": [
            "What is a list in Python?",
            "How do Python lists work?",
            "Explain lists and list methods",
            "How to create and modify lists?"
        ],
        "keywords": ["list", "append", "extend", "insert", "pop", "remove", "slicing", "mutable"],
        "answer": "A list is an ordered, mutable collection of items enclosed in square brackets `[]`. Lists allow duplicates and can hold items of different types.\n\nEssential methods:\n- `append(x)`: Adds `x` to end.\n- `extend(iterable)`: Appends all items from iterable.\n- `insert(i, x)`: Inserts `x` at index `i`.\n- `pop([i])`: Removes and returns item at index (default last).\n- `remove(x)`: Removes first matching item `x`.\n- `sort()`: In-place sort; `reverse()`: In-place reverse.",
        "code_example": "nums = [3, 1, 4]\nnums.append(1)\nnums.extend([5, 9])\nnums.sort()\nprint(nums)  # [1, 1, 3, 4, 5, 9]",
        "related_topics": ["tuples", "list_vs_tuple", "list_comprehension"]
    },
    {
        "id": "tuples",
        "topic": "Data Structures",
        "patterns": [
            "What is a tuple in Python?",
            "How do tuples work in Python?",
            "What are tuples used for?",
            "Why use tuples instead of lists?",
            "Tuple unpacking in Python"
        ],
        "keywords": ["tuple", "tuples", "immutable", "parentheses", "hashable", "unpacking"],
        "answer": "A tuple is an ordered, **immutable** sequence enclosed in parentheses `()`. Because tuples cannot be modified once created, they are faster than lists, use less memory, and can be used as dictionary keys.\n\nTo create a single-element tuple, include a trailing comma: `t = (42,)`.\nTuples support unpacking: `x, y = (10, 20)`.",
        "code_example": "point = (10, 20)\nx, y = point  # Tuple unpacking\nprint(f'x: {x}, y: {y}')\n\n# Single-item tuple\nsingle = (5,)  # Comma is required!",
        "related_topics": ["lists", "list_vs_tuple", "dictionaries"]
    },
    {
        "id": "list_vs_tuple",
        "topic": "Data Structures",
        "patterns": [
            "What is the difference between list and tuple in Python?",
            "List vs tuple",
            "Tuple vs list",
            "Explain tuple vs list",
            "When to use list vs tuple?"
        ],
        "keywords": ["difference", "compare", "vs", "versus", "list vs tuple", "mutable", "immutable"],
        "answer": "Key differences between List and Tuple:\n1. **Mutability**: Lists are mutable (can add, remove, change items); Tuples are immutable.\n2. **Syntax**: Lists use square brackets `[1, 2]`; Tuples use parentheses `(1, 2)`.\n3. **Performance**: Tuples are faster to instantiate and iterate over, and consume less memory.\n4. **Hashability**: Tuples are hashable and can be dictionary keys (if contents are immutable); Lists are unhashable.\n5. **Usage**: Use lists for collections of data that will grow or change; use tuples for fixed heterogeneous records.",
        "code_example": "lst = [1, 2, 3]\nlst[0] = 99  # OK\n\ntup = (1, 2, 3)\n# tup[0] = 99  # TypeError: 'tuple' object does not support item assignment",
        "related_topics": ["lists", "tuples"]
    },
    {
        "id": "dictionaries",
        "topic": "Data Structures",
        "patterns": [
            "What is a dictionary in Python?",
            "How do dictionaries work in Python?",
            "Explain dict key-value pairs and methods",
            "How to iterate over a dictionary?"
        ],
        "keywords": ["dictionary", "dict", "key-value", "hash map", "get", "keys", "values", "items"],
        "answer": "A dictionary (`dict`) is an associative container of key-value pairs enclosed in `{}`. Keys must be unique and immutable (hashable), such as strings, numbers, or tuples.\n\nKey methods:\n- `d[key]`: Access value (raises `KeyError` if absent).\n- `d.get(key, default)`: Safe access without error.\n- `d.keys()`, `d.values()`, `d.items()`: View keys, values, or (key, value) pairs.\n- `d.update({...})`: Merges another dictionary.\n- `d.pop(key)`: Removes key and returns its value.",
        "code_example": "user = {'id': 101, 'name': 'Sarah', 'role': 'Admin'}\nprint(user.get('email', 'N/A'))  # Safe retrieval\n\nfor k, v in user.items():\n    print(f'{k} -> {v}')",
        "related_topics": ["sets", "collections_module"]
    },
    {
        "id": "sets",
        "topic": "Data Structures",
        "patterns": [
            "What is a set in Python?",
            "How do sets work in Python?",
            "Explain set operations union intersection",
            "What is a frozenset?"
        ],
        "keywords": ["set", "frozenset", "unique", "union", "intersection", "difference", "duplicates"],
        "answer": "A set is an unordered collection of unique, hashable items enclosed in `{}` or created with `set()`. Sets automatically discard duplicates.\n\nOperations:\n- `a | b`: Union (all elements from both).\n- `a & b`: Intersection (elements in both).\n- `a - b`: Difference (elements in `a` but not `b`).\n- `a ^ b`: Symmetric difference (elements in either, but not both).\n- `frozenset`: An immutable version of a set that can be used as a dictionary key.",
        "code_example": "a = {1, 2, 3}\nb = {3, 4, 5}\nprint(a | b)   # Union: {1, 2, 3, 4, 5}\nprint(a & b)   # Intersection: {3}\nprint(a - b)   # Difference: {1, 2}\n\n# Removing duplicates from list\nclean = list(set([1, 2, 2, 3]))  # [1, 2, 3]",
        "related_topics": ["dictionaries", "lists"]
    },
    {
        "id": "collections_module",
        "topic": "Data Structures",
        "patterns": [
            "What is the collections module in Python?",
            "Explain defaultdict, Counter, deque in Python",
            "Advanced data structures collections",
            "How to use Counter and defaultdict?"
        ],
        "keywords": ["collections", "counter", "defaultdict", "deque", "namedtuple", "ordereddict"],
        "answer": "The `collections` module provides specialized container datatypes beyond built-in `dict`, `list`, `set`, and `tuple`:\n- `Counter`: Counts hashable objects and occurrences.\n- `defaultdict`: Dictionary that calls a factory function for missing keys (no `KeyError`).\n- `deque`: Double-ended queue with $O(1)$ appends and pops from both ends.\n- `namedtuple`: Creates tuple subclasses with named fields.",
        "code_example": "from collections import Counter, defaultdict, deque\n\n# Counter\ncounts = Counter('banana')\nprint(counts['a'])  # 3\n\n# defaultdict\ngroups = defaultdict(list)\ngroups['fruits'].append('apple')\n\n# deque\nq = deque([1, 2])\nq.appendleft(0)\nprint(q)  # deque([0, 1, 2])",
        "related_topics": ["dictionaries", "lists"]
    },
    {
        "id": "shallow_vs_deep_copy",
        "topic": "Data Structures",
        "patterns": [
            "What is the difference between shallow copy and deep copy in Python?",
            "Shallow copy vs deep copy",
            "How does copy module work in Python?",
            "Explain copy.copy and copy.deepcopy"
        ],
        "keywords": ["shallow copy", "deep copy", "copy.copy", "copy.deepcopy", "clone", "nested"],
        "answer": "- **Shallow Copy (`copy.copy(x)`)**: Creates a new compound object, but populates it with references to the child objects contained in the original. Modifying nested mutable objects affects both original and copy.\n- **Deep Copy (`copy.deepcopy(x)`)**: Creates a new compound object and recursively copies all nested child objects found in the original, ensuring complete separation.",
        "code_example": "import copy\n\noriginal = [[1, 2], [3, 4]]\nshallow = copy.copy(original)\ndeep = copy.deepcopy(original)\n\noriginal[0][0] = 99\nprint(shallow[0][0])  # 99 (affected!)\nprint(deep[0][0])     # 1 (completely independent!)",
        "related_topics": ["mutability_immutability", "lists"]
    },
    {
        "id": "control_flow",
        "topic": "Control Flow",
        "patterns": [
            "How do if elif else statements work in Python?",
            "What is control flow in Python?",
            "Ternary operator in Python",
            "Conditional statements in Python"
        ],
        "keywords": ["if", "elif", "else", "conditional", "ternary", "control flow"],
        "answer": "Control flow manages the execution path based on boolean evaluations.\n- Syntax uses `if`, `elif` (else if), and `else` with indentation.\n- **Ternary Operator (Conditional Expression)**: `value_if_true if condition else value_if_false`.",
        "code_example": "score = 85\nif score >= 90:\n    grade = 'A'\nelif score >= 80:\n    grade = 'B'\nelse:\n    grade = 'C'\n\n# Ternary expression\nstatus = 'Pass' if score >= 50 else 'Fail'\nprint(f'{grade} - {status}')",
        "related_topics": ["loops", "pass_break_continue"]
    },
    {
        "id": "loops",
        "topic": "Control Flow",
        "patterns": [
            "How do loops work in Python?",
            "Difference between for loop and while loop",
            "While else and for else in Python",
            "Looping in Python"
        ],
        "keywords": ["for loop", "while loop", "for else", "while else", "iteration"],
        "answer": "- **`for` loop**: Iterates over any iterable sequence (lists, strings, ranges, dictionaries).\n- **`while` loop**: Repeats as long as a condition evaluates to `True`.\n- **`else` clause on loops**: Executes only if the loop completes normally without encountering a `break` statement.",
        "code_example": "# for-else prime search\nfor n in range(2, 10):\n    for x in range(2, n):\n        if n % x == 0:\n            break\n    else:\n        # Loop fell through without break\n        print(n, 'is a prime number')",
        "related_topics": ["pass_break_continue", "enumerate_zip_range"]
    },
    {
        "id": "pass_break_continue",
        "topic": "Control Flow",
        "patterns": [
            "What is the difference between pass, break, and continue?",
            "How do break, continue, and pass work in Python?",
            "Explain loop control statements in Python"
        ],
        "keywords": ["pass", "break", "continue", "loops", "control flow"],
        "answer": "- `break`: Terminates the innermost active loop immediately.\n- `continue`: Skips the remainder of the current iteration and jumps to the next iteration.\n- `pass`: A null statement placeholder used when syntax requires code but no action is needed.",
        "code_example": "for i in range(5):\n    if i == 1:\n        continue  # skip 1\n    if i == 4:\n        break     # terminate at 4\n    print(i)      # prints 0, 2, 3\n\ndef placeholder_func():\n    pass          # implementation coming later",
        "related_topics": ["loops"]
    },
    {
        "id": "enumerate_zip_range",
        "topic": "Control Flow",
        "patterns": [
            "What are range, enumerate, and zip in Python?",
            "How to use enumerate and zip in Python?",
            "Difference between range and enumerate",
            "Loop with index and parallel looping"
        ],
        "keywords": ["range", "enumerate", "zip", "index", "parallel loop", "iteration"],
        "answer": "- `range(start, stop, step)`: Generates an immutable sequence of numbers on-demand.\n- `enumerate(iterable, start=0)`: Yields pairs of `(index, item)`, cleanly tracking loop index.\n- `zip(*iterables)`: Pairs elements from multiple iterables together into tuples.",
        "code_example": "names = ['Alice', 'Bob', 'Charlie']\nscores = [85, 92, 78]\n\n# enumerate\nfor i, name in enumerate(names, start=1):\n    print(f'{i}. {name}')\n\n# zip\nfor name, score in zip(names, scores):\n    print(f'{name}: {score}')",
        "related_topics": ["loops", "iterators_and_iterables"]
    },
    {
        "id": "functions",
        "topic": "Functions",
        "patterns": [
            "How to define a function in Python?",
            "What are functions in Python?",
            "How do functions and return statements work?",
            "Define function def keyword"
        ],
        "keywords": ["function", "def", "return", "arguments", "parameters", "call", "docstring"],
        "answer": "A function is a reusable block of organized code. Defined using `def`, followed by the name, parameters in parentheses, and a colon. Return values with `return` (default returns `None` if omitted).",
        "code_example": "def calculate_rectangle_area(width: float, height: float) -> float:\n    \"\"\"Calculates and returns rectangle area.\"\"\"\n    return width * height\n\narea = calculate_rectangle_area(5.0, 3.0)\nprint('Area:', area)",
        "related_topics": ["arguments_and_parameters", "args_kwargs", "lambda_functions"]
    },
    {
        "id": "arguments_and_parameters",
        "topic": "Functions",
        "patterns": [
            "What are parameters and arguments in Python?",
            "Positional vs keyword arguments in Python",
            "Default arguments in Python",
            "Positional-only and keyword-only arguments"
        ],
        "keywords": ["parameters", "arguments", "positional", "keyword", "default", "positional-only", "/"],
        "answer": "- **Parameters**: Variables defined in the function signature.\n- **Arguments**: Real values passed when calling the function.\n- **Positional Arguments**: Assigned based on order.\n- **Keyword Arguments**: Passed as `name=value`.\n- **Positional-Only (`/`) & Keyword-Only (`*`)**: Python 3.8+ lets you force arguments before `/` to be positional-only and arguments after `*` to be keyword-only.",
        "code_example": "def configure(mode, /, timeout=30, *, verbose=False):\n    print(f'mode={mode}, timeout={timeout}, verbose={verbose}')\n\nconfigure('fast', timeout=10, verbose=True)",
        "related_topics": ["functions", "args_kwargs", "default_arguments_gotcha"]
    },
    {
        "id": "args_kwargs",
        "topic": "Functions",
        "patterns": [
            "What are *args and **kwargs in Python?",
            "How to use *args and **kwargs?",
            "Variable length arguments in Python functions",
            "Difference between *args and **kwargs"
        ],
        "keywords": ["*args", "**kwargs", "args", "kwargs", "arbitrary arguments", "keyword arguments"],
        "answer": "`*args` and `**kwargs` allow functions to accept variable numbers of arguments:\n1. `*args`: Collects extra positional arguments into a **tuple**.\n2. `**kwargs`: Collects extra keyword arguments into a **dictionary**.\n\nThe names `args` and `kwargs` are conventions; the `*` and `**` unpack/pack operators are what matter.",
        "code_example": "def log_info(*args, **kwargs):\n    print('Positional arguments (tuple):', args)\n    print('Keyword arguments (dict):', kwargs)\n\nlog_info('Server', 'Running', port=8080, status=200)",
        "related_topics": ["functions", "arguments_and_parameters"]
    },
    {
        "id": "default_arguments_gotcha",
        "topic": "Functions",
        "patterns": [
            "Why is mutable default argument bad in Python?",
            "Mutable default argument trap gotcha",
            "def func(a, lst=[]) problem in Python",
            "How to handle default arguments safely"
        ],
        "keywords": ["mutable default", "gotcha", "lst=[]", "default argument trap", "none default"],
        "answer": "In Python, default parameter expressions are evaluated **once at function definition time**, not each time the function is called! If you use a mutable object (like a list `[]` or dict `{}`) as a default value, the same object is shared across all function calls.\n\n**Solution**: Use `None` as the default and initialize inside the function.",
        "code_example": "# WRONG:\n# def add_item(item, target=[]):\n#     target.append(item)\n#     return target\n\n# CORRECT IDIOM:\ndef add_item(item, target=None):\n    if target is None:\n        target = []\n    target.append(item)\n    return target\n\nprint(add_item('apple'))  # ['apple']\nprint(add_item('banana')) # ['banana'] (not shared!)",
        "related_topics": ["functions", "mutability_immutability"]
    },
    {
        "id": "variable_scope_legb",
        "topic": "Functions",
        "patterns": [
            "What is variable scope and LEGB rule in Python?",
            "Explain LEGB rule in Python",
            "How does variable lookup work in Python?",
            "Local vs global variables in Python"
        ],
        "keywords": ["legb", "scope", "local", "enclosing", "global", "built-in", "lookup"],
        "answer": "Python resolves names using the **LEGB rule** in this order:\n1. **L - Local**: Names assigned within a function.\n2. **E - Enclosing**: Names in the local scope of any enclosing functions (closures).\n3. **G - Global**: Names assigned at the top level of the module or declared `global`.\n4. **B - Built-in**: Pre-assigned built-in names (`len`, `range`, `int`, etc.).",
        "code_example": "x = 'global' # Global\n\ndef outer():\n    x = 'enclosing' # Enclosing\n    def inner():\n        x = 'local' # Local\n        print(x)\n    inner()\n\nouter()",
        "related_topics": ["global_nonlocal", "functions"]
    },
    {
        "id": "global_nonlocal",
        "topic": "Functions",
        "patterns": [
            "What is global and nonlocal in Python?",
            "Difference between global and nonlocal",
            "When to use global keyword in Python?",
            "How to modify enclosing variable in Python"
        ],
        "keywords": ["global", "nonlocal", "scope", "closure", "modify outer"],
        "answer": "- `global`: Declares that a variable inside a function refers to the module-level global variable, allowing you to modify it.\n- `nonlocal`: Declares that a variable inside a nested function refers to the nearest enclosing scope variable that is not global, enabling closures to modify state.",
        "code_example": "count = 0\ndef increment_global():\n    global count\n    count += 1\n\ndef make_counter():\n    num = 0\n    def counter():\n        nonlocal num\n        num += 1\n        return num\n    return counter\n\nc = make_counter()\nprint(c(), c())  # 1, 2",
        "related_topics": ["variable_scope_legb", "decorators"]
    },
    {
        "id": "lambda_functions",
        "topic": "Functions",
        "patterns": [
            "What is a lambda function in Python?",
            "How do anonymous functions work in Python?",
            "Explain lambda expressions with examples",
            "When to use lambda in Python?"
        ],
        "keywords": ["lambda", "anonymous", "inline function", "map", "filter", "sort"],
        "answer": "A lambda function is a small, anonymous inline function defined with the `lambda` keyword. It can take any number of arguments, but can contain only **one expression**, which is evaluated and returned automatically.\n\nMost commonly used with `sorted()`, `map()`, or `filter()`.",
        "code_example": "# Syntax: lambda arguments: expression\nsquare = lambda x: x ** 2\nprint(square(6))  # 36\n\n# Sort pairs by second element\nusers = [('Alice', 25), ('Bob', 20), ('Charlie', 30)]\nusers.sort(key=lambda u: u[1])\nprint(users)",
        "related_topics": ["map_filter_reduce", "list_comprehension"]
    },
    {
        "id": "map_filter_reduce",
        "topic": "Functions",
        "patterns": [
            "What are map, filter, and reduce in Python?",
            "How to use map and filter in Python?",
            "Explain functools.reduce in Python",
            "Functional programming in Python"
        ],
        "keywords": ["map", "filter", "reduce", "functools", "functional", "iterable"],
        "answer": "- `map(func, iterable)`: Applies a function to all items in an iterable and returns an iterator.\n- `filter(func, iterable)`: Filters items from an iterable for which `func(item)` returns `True`.\n- `functools.reduce(func, iterable)`: Cumulatively applies a binary function to items from left to right, reducing the sequence to a single cumulative value.",
        "code_example": "from functools import reduce\n\nnums = [1, 2, 3, 4, 5]\n\n# map\ndoubled = list(map(lambda x: x * 2, nums))     # [2, 4, 6, 8, 10]\n# filter\nevens = list(filter(lambda x: x % 2 == 0, nums)) # [2, 4]\n# reduce\nproduct = reduce(lambda a, b: a * b, nums)     # 120",
        "related_topics": ["lambda_functions", "list_comprehension"]
    },
    {
        "id": "recursion",
        "topic": "Functions",
        "patterns": [
            "What is recursion in Python?",
            "How does recursion work in Python?",
            "Recursion limit in Python",
            "Explain recursive function with base case"
        ],
        "keywords": ["recursion", "recursive", "base case", "call stack", "sys.getrecursionlimit"],
        "answer": "Recursion occurs when a function calls itself to solve a smaller subproblem of the original task. Every recursive function must have:\n1. **Base Case**: A terminating condition that stops recursion.\n2. **Recursive Step**: Calling itself with modified input moving toward the base case.\n\nPython has a maximum recursion depth (default 1000) accessible via `sys.getrecursionlimit()`.",
        "code_example": "def factorial(n: int) -> int:\n    if n <= 1:           # Base case\n        return 1\n    return n * factorial(n - 1) # Recursive step\n\nprint(factorial(5))  # 120",
        "related_topics": ["functions"]
    },
    {
        "id": "list_comprehension",
        "topic": "Advanced Basics",
        "patterns": [
            "What is list comprehension in Python?",
            "How does list comprehension work?",
            "Syntax for list comprehension",
            "Explain list comprehension with examples"
        ],
        "keywords": ["list comprehension", "syntax", "filter", "mapping", "compact loop"],
        "answer": "List comprehension provides a concise syntax to create new lists from existing iterables. It is often faster and more readable than standard `for` loops with `.append()`.\n\n**Syntax**: `[expression for item in iterable if condition]`",
        "code_example": "# Squares of even numbers from 0 to 9\neven_squares = [x ** 2 for x in range(10) if x % 2 == 0]\nprint(even_squares)  # [0, 4, 16, 36, 64]",
        "related_topics": ["dict_set_comprehension", "generators", "lists"]
    },
    {
        "id": "dict_set_comprehension",
        "topic": "Advanced Basics",
        "patterns": [
            "What are dictionary and set comprehensions in Python?",
            "How to use dict comprehension?",
            "Syntax for set comprehension in Python",
            "Comprehensions in Python"
        ],
        "keywords": ["dict comprehension", "set comprehension", "syntax", "comprehensions"],
        "answer": "Similar to list comprehensions, Python supports comprehensions for dictionaries and sets:\n- **Dict Comprehension**: `{key_expr: value_expr for item in iterable if condition}`\n- **Set Comprehension**: `{expr for item in iterable if condition}`",
        "code_example": "# Dict comprehension\nsquares_dict = {x: x**2 for x in range(5)}\nprint(squares_dict)  # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}\n\n# Set comprehension\nunique_lens = {len(w) for w in ['python', 'code', 'chat', 'dev']}\nprint(unique_lens)   # {3, 4, 6}",
        "related_topics": ["list_comprehension", "dictionaries", "sets"]
    },
    {
        "id": "iterators_and_iterables",
        "topic": "Advanced Basics",
        "patterns": [
            "What is the difference between iterable and iterator in Python?",
            "Iterable vs iterator in Python",
            "How do iter() and next() work?",
            "Explain Python iteration protocol"
        ],
        "keywords": ["iterable", "iterator", "iter()", "next()", "__iter__", "__next__", "StopIteration"],
        "answer": "- **Iterable**: Any object capable of returning its members one at a time. Must implement `__iter__()` (e.g. lists, tuples, dicts, strings).\n- **Iterator**: An object representing a stream of data with state. Must implement `__next__()` (returns next item or raises `StopIteration`) and `__iter__()` (returns self).",
        "code_example": "my_list = [10, 20]\nmy_iter = iter(my_list) # Get iterator\n\nprint(next(my_iter))    # 10\nprint(next(my_iter))    # 20\n# print(next(my_iter))  # Raises StopIteration",
        "related_topics": ["generators", "loops"]
    },
    {
        "id": "generators",
        "topic": "Advanced Topics",
        "patterns": [
            "What is a generator in Python?",
            "What is yield in Python?",
            "Difference between return and yield",
            "Explain generator functions and expressions"
        ],
        "keywords": ["generator", "yield", "iterator", "next()", "memory efficiency", "generator expression"],
        "answer": "A generator is a function that returns an iterator using the `yield` keyword instead of `return`. Unlike regular functions that calculate and return all values at once into memory, generators yield values **lazily** (one-by-one on demand), drastically conserving memory for massive datasets.",
        "code_example": "def fibonacci_gen(limit):\n    a, b = 0, 1\n    while a < limit:\n        yield a\n        a, b = b, a + b\n\nfor num in fibonacci_gen(20):\n    print(num, end=' ')  # 0 1 1 2 3 5 8 13",
        "related_topics": ["iterators_and_iterables", "list_comprehension"]
    },
    {
        "id": "oop_basics",
        "topic": "Object-Oriented Programming",
        "patterns": [
            "What is Object-Oriented Programming (OOP) in Python?",
            "Explain classes and objects in Python",
            "What are the four pillars of OOP in Python?",
            "Object-oriented programming concepts"
        ],
        "keywords": ["oop", "class", "object", "instance", "methods", "attributes", "pillars"],
        "answer": "OOP models software around data (attributes) and behaviors (methods). The 4 Pillars of OOP:\n1. **Encapsulation**: Bundles data and methods, restricting direct access via privacy conventions.\n2. **Inheritance**: Derives new classes from existing classes to reuse logic.\n3. **Polymorphism**: Allows different classes to be treated through a uniform interface.\n4. **Abstraction**: Exposes essential features while hiding complex internal details.",
        "code_example": "class BankAccount:\n    def __init__(self, owner, balance=0):\n        self.owner = owner\n        self._balance = balance # Encapsulated\n        \n    def deposit(self, amount):\n        self._balance += amount\n        return self._balance\n\nacct = BankAccount('Alice', 100)\nprint('New balance:', acct.deposit(50))",
        "related_topics": ["classes_and_objects", "init_method", "inheritance", "polymorphism"]
    },
    {
        "id": "classes_and_objects",
        "topic": "Object-Oriented Programming",
        "patterns": [
            "How to create a class and object in Python?",
            "Difference between class and object in Python",
            "Class attributes vs instance attributes",
            "Define a class in Python"
        ],
        "keywords": ["class", "object", "instance", "class attribute", "instance attribute"],
        "answer": "- **Class**: A blueprint or prototype from which objects are created.\n- **Object (Instance)**: A concrete instantiation of a class.\n- **Class Attribute**: Belongs to the class itself, shared by all instances.\n- **Instance Attribute**: Belongs to a specific instance, distinct per object.",
        "code_example": "class Employee:\n    company = 'TechCorp'  # Class attribute\n    \n    def __init__(self, name, salary):\n        self.name = name  # Instance attribute\n        self.salary = salary\n\ne1 = Employee('John', 60000)\nprint(e1.name, e1.company)",
        "related_topics": ["init_method", "self_keyword", "oop_basics"]
    },
    {
        "id": "init_method",
        "topic": "Object-Oriented Programming",
        "patterns": [
            "What is __init__ in Python?",
            "Explain Python constructor",
            "How does __init__ work in Python classes?",
            "Why do we need __init__?"
        ],
        "keywords": ["__init__", "constructor", "dunder", "initialize", "instantiation"],
        "answer": "`__init__` is a special dunder (double-underscore) method that acts as the **constructor/initializer** in Python. When you create an instance of a class, Python automatically calls `__init__` to initialize the object's instance variables.",
        "code_example": "class User:\n    def __init__(self, username, email):\n        self.username = username\n        self.email = email\n\nu = User('py_dev', 'dev@example.com')\nprint(u.username, u.email)",
        "related_topics": ["self_keyword", "classes_and_objects"]
    },
    {
        "id": "self_keyword",
        "topic": "Object-Oriented Programming",
        "patterns": [
            "What is self in Python?",
            "Why is self used in class methods?",
            "What does self represent?",
            "Is self a keyword in Python?"
        ],
        "keywords": ["self", "instance reference", "class method", "keyword"],
        "answer": "`self` represents the specific **instance of the class** on which a method is being called. It allows methods to access and modify the object's attributes and other methods.\n\n*Note*: `self` is not a reserved syntax keyword in Python, but a universal PEP 8 convention.",
        "code_example": "class Counter:\n    def __init__(self):\n        self.count = 0\n    def increment(self):\n        self.count += 1\n        return self.count\n\nc = Counter()\nprint(c.increment())  # 1",
        "related_topics": ["init_method", "methods_types"]
    },
    {
        "id": "methods_types",
        "topic": "Object-Oriented Programming",
        "patterns": [
            "Difference between instance method, class method, and static method",
            "What is @classmethod and @staticmethod in Python?",
            "Types of methods in Python OOP",
            "When to use @staticmethod vs @classmethod"
        ],
        "keywords": ["classmethod", "staticmethod", "instance method", "@classmethod", "@staticmethod", "cls", "self"],
        "answer": "1. **Instance Method**: Receives `self` (the instance). Can read/modify instance and class state.\n2. **Class Method (`@classmethod`)**: Receives `cls` (the class) instead of instance. Can modify class state and serves as alternative constructors.\n3. **Static Method (`@staticmethod`)**: Does not receive `self` or `cls`. Behaves like a plain function isolated inside the class namespace.",
        "code_example": "class MathOps:\n    pi = 3.14159\n    \n    @classmethod\n    def circle_area(cls, radius):\n        return cls.pi * (radius ** 2)\n        \n    @staticmethod\n    def add(a, b):\n        return a + b\n\nprint(MathOps.circle_area(5))\nprint(MathOps.add(10, 20))",
        "related_topics": ["oop_basics", "self_keyword"]
    },
    {
        "id": "inheritance",
        "topic": "Object-Oriented Programming",
        "patterns": [
            "What is inheritance in Python?",
            "How does inheritance work in Python?",
            "Explain super() in Python inheritance",
            "Single, multiple, and multilevel inheritance"
        ],
        "keywords": ["inheritance", "subclass", "superclass", "super()", "parent", "child", "override"],
        "answer": "Inheritance allows a child (derived) class to inherit attributes and methods from a parent (base) class, encouraging code reusability. The `super()` function is used to invoke methods and constructors from the parent class.",
        "code_example": "class Animal:\n    def __init__(self, name):\n        self.name = name\n    def speak(self):\n        return '...' \n\nclass Dog(Animal):\n    def speak(self):\n        return f'{self.name} says Woof!'\n\ndog = Dog('Buddy')\nprint(dog.speak())  # Buddy says Woof!",
        "related_topics": ["multiple_inheritance_and_mro", "polymorphism"]
    },
    {
        "id": "multiple_inheritance_and_mro",
        "topic": "Object-Oriented Programming",
        "patterns": [
            "What is multiple inheritance and MRO in Python?",
            "Explain Method Resolution Order in Python",
            "What is C3 linearization in Python?",
            "Diamond problem in Python"
        ],
        "keywords": ["mro", "method resolution order", "multiple inheritance", "c3 linearization", "diamond problem"],
        "answer": "Python supports **Multiple Inheritance** where a class can inherit from more than one parent. To determine the order in which base classes are searched when resolving methods, Python uses the **C3 Linearization Algorithm** (Method Resolution Order, MRO). You can view the order via `ClassName.__mro__`.",
        "code_example": "class A: pass\nclass B(A): pass\nclass C(A): pass\nclass D(B, C): pass\n\nprint(D.__mro__)",
        "related_topics": ["inheritance", "oop_basics"]
    },
    {
        "id": "polymorphism",
        "topic": "Object-Oriented Programming",
        "patterns": [
            "What is polymorphism and duck typing in Python?",
            "Explain duck typing in Python",
            "How does polymorphism work in Python?",
            "If it walks like a duck"
        ],
        "keywords": ["polymorphism", "duck typing", "method overriding", "interface"],
        "answer": "Polymorphism means 'many forms'—allowing different classes to implement methods with the same name. Python relies heavily on **Duck Typing**: *\"If it walks like a duck and quacks like a duck, it's a duck.\"* Python checks for the presence of methods/attributes at runtime rather than strictly checking the object's explicit class inheritance.",
        "code_example": "class Duck:\n    def quack(self):\n        return 'Quack!'\n\nclass Person:\n    def quack(self):\n        return 'I am mimicking a duck!'\n\ndef make_it_quack(entity):\n    print(entity.quack()) # Duck typing in action!\n\nmake_it_quack(Duck())\nmake_it_quack(Person())",
        "related_topics": ["oop_basics", "inheritance"]
    },
    {
        "id": "encapsulation",
        "topic": "Object-Oriented Programming",
        "patterns": [
            "What is encapsulation in Python?",
            "Public, protected, and private access modifiers in Python",
            "Name mangling with double underscore in Python",
            "How to achieve data hiding in Python?"
        ],
        "keywords": ["encapsulation", "private", "protected", "name mangling", "_", "__", "data hiding"],
        "answer": "Encapsulation binds data and code together while restricting unauthorized access:\n1. **Public** (`var`): Accessible anywhere.\n2. **Protected** (`_var`): Convention indicating internal use (accessible, but discouraged outside class/subclasses).\n3. **Private** (`__var`): Triggers **Name Mangling** where Python renames the attribute to `_ClassName__var` to prevent accidental overriding in subclasses.",
        "code_example": "class Account:\n    def __init__(self, balance):\n        self.__balance = balance # Private\n        \n    def get_balance(self):\n        return self.__balance\n\nacct = Account(500)\nprint(acct.get_balance()) # 500\n# acct.__balance -> AttributeError!\n# print(acct._Account__balance) # Accessible via mangled name",
        "related_topics": ["oop_basics", "property_decorator"]
    },
    {
        "id": "abstraction",
        "topic": "Object-Oriented Programming",
        "patterns": [
            "What is abstraction in Python?",
            "How to create abstract classes in Python?",
            "Explain abc module and @abstractmethod",
            "Abstract base class in Python"
        ],
        "keywords": ["abstraction", "abc", "abstractmethod", "abstract base class", "interface"],
        "answer": "Abstraction hides implementation details and exposes only the essential interface. In Python, you implement abstraction using the `abc` (Abstract Base Classes) module and the `@abstractmethod` decorator. An abstract class cannot be instantiated directly; subclasses must implement all abstract methods.",
        "code_example": "from abc import ABC, abstractmethod\n\nclass Shape(ABC):\n    @abstractmethod\n    def area(self):\n        pass\n\nclass Circle(Shape):\n    def __init__(self, r):\n        self.r = r\n    def area(self):\n        return 3.14159 * self.r * self.r\n\nc = Circle(4)\nprint('Area:', c.area())",
        "related_topics": ["oop_basics", "inheritance"]
    },
    {
        "id": "dunder_magic_methods",
        "topic": "Object-Oriented Programming",
        "patterns": [
            "What are magic methods or dunder methods in Python?",
            "Explain __str__ vs __repr__ in Python",
            "Operator overloading using dunder methods",
            "List of special methods in Python"
        ],
        "keywords": ["dunder", "magic methods", "__str__", "__repr__", "__len__", "__getitem__", "operator overloading"],
        "answer": "Magic methods (dunder methods, starting and ending with double underscores `__`) allow custom classes to hook into Python's built-in operators and protocols:\n- `__str__`: User-friendly string representation (`print(obj)`).\n- `__repr__`: Unambiguous developer/debugging string representation.\n- `__len__`: Hook for `len(obj)`.\n- `__getitem__`: Hook for index bracket access `obj[key]`.\n- `__add__`: Overloads the `+` operator.",
        "code_example": "class Vector:\n    def __init__(self, x, y):\n        self.x, self.y = x, y\n        \n    def __add__(self, other):\n        return Vector(self.x + other.x, self.y + other.y)\n        \n    def __repr__(self):\n        return f'Vector({self.x}, {self.y})'\n\nv1 = Vector(2, 3)\nv2 = Vector(5, 7)\nprint(v1 + v2)  # Vector(7, 10)",
        "related_topics": ["init_method", "oop_basics"]
    },
    {
        "id": "property_decorator",
        "topic": "Object-Oriented Programming",
        "patterns": [
            "What is @property in Python?",
            "How to use getters and setters in Python?",
            "Property decorator explanation with examples",
            "Pythonic getter and setter"
        ],
        "keywords": ["@property", "getter", "setter", "deleter", "property decorator", "encapsulation"],
        "answer": "The `@property` decorator allows you to define methods that can be accessed like attributes (without parentheses), enabling Pythonic getters, setters, and validation without breaking existing code interfaces.",
        "code_example": "class Temperature:\n    def __init__(self, celsius=0):\n        self._celsius = celsius\n        \n    @property\n    def celsius(self):\n        return self._celsius\n        \n    @celsius.setter\n    def celsius(self, value):\n        if value < -273.15:\n            raise ValueError('Temperature below absolute zero!')\n        self._celsius = value\n\nt = Temperature(25)\nt.celsius = 30  # Invokes setter\nprint(t.celsius) # Invokes getter: 30",
        "related_topics": ["encapsulation", "decorators"]
    },
    {
        "id": "dataclasses",
        "topic": "Object-Oriented Programming",
        "patterns": [
            "What is a dataclass in Python?",
            "How to use @dataclass in Python?",
            "Explain dataclasses module",
            "Why use dataclasses instead of standard classes?"
        ],
        "keywords": ["dataclass", "@dataclass", "boilerplate", "__init__", "__repr__", "type hints"],
        "answer": "Introduced in Python 3.7, `@dataclass` automatically generates boilerplate special methods such as `__init__()`, `__repr__()`, `__eq__()`, and comparison methods based on type annotations, significantly reducing code verbosity.",
        "code_example": "from dataclasses import dataclass\n\n@dataclass\nclass Product:\n    name: str\n    price: float\n    quantity: int = 1\n    \n    def total_cost(self) -> float:\n        return self.price * self.quantity\n\np = Product('Keyboard', 49.99, 2)\nprint(p)  # Product(name='Keyboard', price=49.99, quantity=2)",
        "related_topics": ["oop_basics", "init_method"]
    },
    {
        "id": "decorators",
        "topic": "Advanced Topics",
        "patterns": [
            "What is a decorator in Python?",
            "How do decorators work in Python?",
            "Explain @ symbol in Python",
            "How to create a custom decorator with arguments?"
        ],
        "keywords": ["decorator", "@", "wrapper", "higher-order function", "closure", "functools.wraps"],
        "answer": "A decorator is a callable that takes another function as an argument, extends its behavior without directly modifying its source code, and returns the modified function. Applied using the `@decorator_name` syntax.\n\nBest practice: Use `@functools.wraps` to preserve the original function's name and docstring.",
        "code_example": "from functools import wraps\nimport time\n\ndef timer(func):\n    @wraps(func)\n    def wrapper(*args, **kwargs):\n        start = time.time()\n        result = func(*args, **kwargs)\n        print(f'{func.__name__} took {time.time() - start:.4f}s')\n        return result\n    return wrapper\n\n@timer\ndef slow_add(a, b):\n    return a + b\n\nslow_add(5, 10)",
        "related_topics": ["functions", "generators"]
    },
    {
        "id": "exception_handling",
        "topic": "Control Flow & Errors",
        "patterns": [
            "How to handle exceptions in Python?",
            "What is try except in Python?",
            "Explain error handling in Python",
            "What is finally and else in try except?",
            "Built-in exceptions in Python"
        ],
        "keywords": ["try", "except", "finally", "else", "raise", "exception", "error handling"],
        "answer": "Exceptions are runtime errors handled via `try`, `except`, `else`, and `finally` blocks:\n- `try`: Code that may raise an exception.\n- `except ExceptionType as e`: Catches and handles specific errors.\n- `else`: Runs only if no exception was raised in `try`.\n- `finally`: Runs unconditionally (ideal for resource cleanup).\n- `raise`: Manually triggers an exception.",
        "code_example": "try:\n    num = int('abc')\nexcept ValueError as err:\n    print(f'Handled ValueError: {err}')\nelse:\n    print('Conversion successful!')\nfinally:\n    print('Cleanup completed.')",
        "related_topics": ["custom_exceptions", "file_handling"]
    },
    {
        "id": "custom_exceptions",
        "topic": "Control Flow & Errors",
        "patterns": [
            "How to create custom exceptions in Python?",
            "Define user-defined exception in Python",
            "Inheriting from Exception class in Python",
            "Raise custom error"
        ],
        "keywords": ["custom exception", "user-defined exception", "raise", "inherit Exception"],
        "answer": "Custom exceptions are created by defining a new class that inherits from the built-in `Exception` (or a more specific exception class like `ValueError`).",
        "code_example": "class InsufficientFundsError(Exception):\n    \"\"\"Raised when transaction exceeds balance.\"\"\"\n    def __init__(self, balance, amount):\n        super().__init__(f'Cannot withdraw ${amount}; balance is only ${balance}')\n\ndef withdraw(balance, amount):\n    if amount > balance:\n        raise InsufficientFundsError(balance, amount)\n    return balance - amount\n\n# withdraw(100, 150) # Raises InsufficientFundsError",
        "related_topics": ["exception_handling"]
    },
    {
        "id": "file_handling",
        "topic": "File I/O",
        "patterns": [
            "How to read and write files in Python?",
            "Explain file handling in Python",
            "What is with open in Python?",
            "File modes in Python"
        ],
        "keywords": ["open", "read", "write", "with statement", "file i/o", "modes", "close"],
        "answer": "File handling uses `open(filename, mode, encoding)`.\nAlways use the `with` statement (context manager) to ensure the file is automatically closed when done, even if errors occur.\n\nCommon modes: `'r'` (read), `'w'` (write, overwrites), `'a'` (append), `'rb'`/`'wb'` (binary).",
        "code_example": "# Writing to file\nwith open('demo.txt', 'w', encoding='utf-8') as f:\n    f.write('Hello, File!\\nSecond line.')\n\n# Reading line by line\nwith open('demo.txt', 'r', encoding='utf-8') as f:\n    for line in f:\n        print(line.strip())",
        "related_topics": ["context_managers", "json_handling"]
    },
    {
        "id": "context_managers",
        "topic": "File I/O",
        "patterns": [
            "What is a context manager in Python?",
            "How does the with statement work in Python?",
            "Explain __enter__ and __exit__ in Python",
            "contextlib contextmanager in Python"
        ],
        "keywords": ["context manager", "with statement", "__enter__", "__exit__", "contextlib", "resource management"],
        "answer": "Context managers handle the setup and teardown of resources (like files, database locks, or network sockets). Implemented either using a class with `__enter__()` and `__exit__()` methods, or using the `@contextlib.contextmanager` decorator with `yield`.",
        "code_example": "from contextlib import contextmanager\n\n@contextmanager\ntagged_block(tag):\n    print(f'<{tag}>')\n    try:\n        yield\n    finally:\n        print(f'</{tag}>')\n\nwith tagged_block('header'):\n    print('Page Title')",
        "related_topics": ["file_handling", "dunder_magic_methods"]
    },
    {
        "id": "json_handling",
        "topic": "File I/O",
        "patterns": [
            "How to read and parse JSON in Python?",
            "Explain json module in Python",
            "Difference between json.loads and json.load",
            "json.dump vs json.dumps in Python"
        ],
        "keywords": ["json", "loads", "dumps", "load", "dump", "serialization", "deserialization"],
        "answer": "Python's `json` module translates Python objects to/from JSON:\n- `json.loads(string)`: Deserializes JSON string into Python dict/list.\n- `json.dumps(obj)`: Serializes Python object into JSON formatted string.\n- `json.load(file)`: Reads and deserializes JSON directly from a file stream.\n- `json.dump(obj, file)`: Serializes and writes Python object into a file stream.",
        "code_example": "import json\n\ndata = {'name': 'Alex', 'languages': ['Python', 'SQL']}\n# Object to JSON string\njson_str = json.dumps(data, indent=2)\nprint(json_str)\n\n# JSON string back to dict\nparsed = json.loads(json_str)\nprint(parsed['name'])",
        "related_topics": ["file_handling", "dictionaries"]
    },
    {
        "id": "modules_and_packages",
        "topic": "Modules & Packaging",
        "patterns": [
            "What is a module and package in Python?",
            "How to import modules in Python?",
            "Difference between module and package",
            "How does import work in Python?"
        ],
        "keywords": ["module", "package", "import", "sys.path", "__init__.py", "namespace"],
        "answer": "- **Module**: A single Python file (`.py`) containing functions, classes, and statements.\n- **Package**: A directory containing modules and an `__init__.py` file (optional in Python 3.3+ namespace packages, but recommended).\n- Python searches for imports in `sys.path` (current directory, standard library, and `site-packages`).",
        "code_example": "# Importing entire module\nimport math\nprint(math.sqrt(16))\n\n# Specific import with alias\nfrom datetime import datetime as dt\nprint(dt.now())",
        "related_topics": ["name_main", "pip_virtualenv"]
    },
    {
        "id": "python_libraries",
        "topic": "Modules & Packaging",
        "patterns": [
            "What are libraries in Python?",
            "What is a library in Python?",
            "Explain Python libraries",
            "What libraries are used in Python?",
            "Difference between library, module, and package in Python",
            "Most popular Python libraries"
        ],
        "keywords": ["library", "libraries", "package", "numpy", "pandas", "requests", "standard library", "third-party", "framework"],
        "answer": "A **library** in Python is a pre-written collection of modules and packages that provide reusable code, functions, and classes to perform specific tasks without writing code from scratch.\n\nPython has two main types of libraries:\n1. **Python Standard Library ('Batteries Included')**: Built right into Python (no installation needed):\n   - `math`, `random`: Mathematical operations & random numbers\n   - `os`, `sys`: Operating system interactions and runtime parameters\n   - `json`, `csv`: Data serialization and file formats\n   - `datetime`: Date and time manipulation\n   - `re`: Regular expressions\n   - `collections`, `itertools`: Specialized data structures & iteration\n\n2. **Third-Party Libraries (Installed via `pip`)**:\n   - **Data Science & Analytics**: `NumPy` (numerical arrays), `Pandas` (dataframes), `SciPy`\n   - **Machine Learning & AI**: `Scikit-learn`, `TensorFlow`, `PyTorch`\n   - **Web Development**: `Flask`, `FastAPI`, `Django`\n   - **Data Visualization**: `Matplotlib`, `Seaborn`, `Plotly`\n   - **Networking & Scraping**: `Requests`, `BeautifulSoup`, `Scrapy`\n\n*Difference summary*: A **module** is a single `.py` file; a **package** is a folder with `__init__.py` and multiple modules; a **library** is an umbrella collection of packages designed for a specific domain.",
        "code_example": "# Using a standard library:\nimport math\nprint('Square root:', math.sqrt(25)) # 5.0\n\n# Using a popular third-party library (e.g. requests):\n# pip install requests\n# import requests\n# resp = requests.get('https://api.github.com')\n# print(resp.status_code)",
        "related_topics": ["modules_and_packages", "pip_virtualenv"]
    },
    {
        "id": "name_main",
        "topic": "Modules & Packaging",
        "patterns": [
            "What is if __name__ == '__main__' in Python?",
            "Explain if __name__ == '__main__'",
            "Why use __name__ in Python scripts?",
            "What is __name__ variable?"
        ],
        "keywords": ["__name__", "__main__", "entry point", "boilerplate", "script execution"],
        "answer": "`__name__` is a built-in variable. When a file is run directly from the command line, Python sets `__name__` to `'__main__'`. If the file is imported into another script, `__name__` is set to the module's actual filename.\n\n`if __name__ == '__main__':` ensures that execution code runs only when executed directly as a script, not when imported as a library.",
        "code_example": "def main():\n    print('Running program!')\n\nif __name__ == '__main__':\n    main()",
        "related_topics": ["modules_and_packages"]
    },
    {
        "id": "pip_virtualenv",
        "topic": "Environment & Packages",
        "patterns": [
            "What is pip and virtualenv in Python?",
            "How to create a virtual environment in Python?",
            "Explain package management in Python",
            "What is venv in Python?"
        ],
        "keywords": ["pip", "virtualenv", "venv", "package manager", "install", "environment", "requirements.txt"],
        "answer": "- **pip**: The official package installer for Python, downloading libraries from the Python Package Index (PyPI).\n- **venv / virtualenv**: An isolated environment with its own Python interpreter and site-packages, preventing dependency version conflicts across multiple projects.",
        "code_example": "# Terminal commands:\n# 1. Create virtual environment\n# python -m venv myenv\n\n# 2. Activate (Windows)\n# myenv\\Scripts\\activate\n\n# 3. Install packages\n# pip install requests flask",
        "related_topics": ["modules_and_packages"]
    },
    {
        "id": "gil",
        "topic": "Internals & Concurrency",
        "patterns": [
            "What is GIL in Python?",
            "Explain Global Interpreter Lock",
            "Why does Python have a GIL?",
            "How does GIL affect multithreading in Python?"
        ],
        "keywords": ["gil", "global interpreter lock", "multithreading", "concurrency", "cpython", "thread safe"],
        "answer": "The Global Interpreter Lock (GIL) is a mutex used by CPython to ensure only one native thread executes Python bytecode at a time. It prevents race conditions in CPython's reference-counted memory management.\n\n**Consequence**: Python threads do not speed up CPU-bound tasks. However, multithreading is still effective for **I/O-bound** tasks (e.g., networking, disk access). For CPU-bound tasks, use `multiprocessing`.",
        "code_example": "# For CPU-bound parallel execution:\nfrom multiprocessing import Pool\n\ndef square(x):\n    return x * x\n\nif __name__ == '__main__':\n    with Pool() as p:\n        print(p.map(square, [1, 2, 3, 4]))",
        "related_topics": ["multithreading_vs_multiprocessing", "asyncio_concurrency"]
    },
    {
        "id": "multithreading_vs_multiprocessing",
        "topic": "Internals & Concurrency",
        "patterns": [
            "Difference between multithreading and multiprocessing in Python",
            "Multithreading vs multiprocessing",
            "When to use threads vs processes in Python",
            "Concurrency in Python"
        ],
        "keywords": ["multithreading", "multiprocessing", "threading", "process", "cpu-bound", "io-bound"],
        "answer": "- **Multithreading (`threading` module)**: Multiple threads share the same process memory space. Restricted by the GIL; best suited for **I/O-bound** tasks (API requests, disk reads).\n- **Multiprocessing (`multiprocessing` module)**: Spawns independent operating system processes, each with its own memory space and Python interpreter, bypassing the GIL; best for **CPU-bound** tasks (data science, image processing).",
        "code_example": "import threading\n\ndef worker(num):\n    print(f'Thread {num} running')\n\nthreads = [threading.Thread(target=worker, args=(i,)) for i in range(3)]\nfor t in threads: t.start()\nfor t in threads: t.join()",
        "related_topics": ["gil", "asyncio_concurrency"]
    },
    {
        "id": "asyncio_concurrency",
        "topic": "Internals & Concurrency",
        "patterns": [
            "What is asyncio in Python?",
            "How does async and await work in Python?",
            "Asynchronous programming in Python",
            "Explain event loop and coroutines"
        ],
        "keywords": ["asyncio", "async", "await", "coroutine", "event loop", "asynchronous"],
        "answer": "`asyncio` is a standard library for writing concurrent code using the `async`/`await` syntax. It uses a single-threaded **event loop** that cooperatively switches between coroutines during I/O wait periods, offering high performance and scaling to thousands of concurrent network connections without thread overhead.",
        "code_example": "import asyncio\n\nasync def fetch_data(id_num):\n    print(f'Start task {id_num}')\n    await asyncio.sleep(1) # Non-blocking sleep\n    print(f'Done task {id_num}')\n    return id_num * 10\n\nasync def main():\n    results = await asyncio.gather(fetch_data(1), fetch_data(2))\n    print('Results:', results)\n\n# asyncio.run(main())",
        "related_topics": ["multithreading_vs_multiprocessing", "gil"]
    },
    {
        "id": "memory_management_gc",
        "topic": "Internals & Concurrency",
        "patterns": [
            "How does memory management work in Python?",
            "Explain garbage collection in Python",
            "What is reference counting in Python?",
            "How Python frees memory and circular references"
        ],
        "keywords": ["garbage collection", "memory management", "reference counting", "gc", "cyclic references", "sys.getrefcount"],
        "answer": "Python manages memory through two main mechanisms:\n1. **Reference Counting**: Every object tracks how many references point to it. When an object's reference count drops to 0, its memory is deallocated immediately.\n2. **Generational Garbage Collector (`gc` module)**: Detects and cleans up circular reference cycles (e.g., object A refers to B, and B refers to A) by categorizing objects into 3 generations.",
        "code_example": "import sys, gc\n\nx = []\nprint('Ref count:', sys.getrefcount(x)) # Includes temporary ref by getrefcount\n\n# Manually run cyclic garbage collection\ngc.collect()",
        "related_topics": ["gil", "mutability_immutability"]
    },
    {
        "id": "pep8",
        "topic": "Best Practices",
        "patterns": [
            "What is PEP 8 in Python?",
            "Python style guide PEP 8",
            "What are the main coding standards in PEP 8?",
            "How to write clean Python code?"
        ],
        "keywords": ["pep 8", "style guide", "indentation", "naming conventions", "clean code"],
        "answer": "PEP 8 is the official Python style guide. Key principles:\n1. **Indentation**: 4 spaces per level (never tabs).\n2. **Naming Conventions**:\n   - Functions & variables: `snake_case`\n   - Classes: `PascalCase`\n   - Constants: `UPPER_SNAKE_CASE`\n3. **Line Length**: Max 79 characters.\n4. **Imports**: At top of file, grouped into Standard Library, Third-Party, and Local imports.\n5. **Whitespace**: Spaces around operators and after commas.",
        "code_example": "# PEP 8 Compliant\nimport os\n\nMAX_RETRIES = 5\n\nclass DataService:\n    def fetch_record(self, record_id: int) -> dict:\n        return {'id': record_id, 'status': 'active'}",
        "related_topics": ["zen_of_python", "what_is_python"]
    }
]

with open("knowledge_base.json", "w", encoding="utf-8") as f:
    json.dump(entries, f, indent=2, ensure_ascii=False)

print(f"Successfully generated knowledge_base.json with {len(entries)} comprehensive entries!")
