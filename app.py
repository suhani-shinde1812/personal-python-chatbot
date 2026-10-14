"""
Flask Web Application for Python QA Chatbot
"""

import os
from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
from chatbot import PythonChatbot

app = Flask(__name__)
CORS(app)

# Initialize chatbot instance
KB_PATH = os.path.join(os.path.dirname(__file__), "knowledge_base.json")
chatbot = PythonChatbot(kb_path=KB_PATH)


@app.route("/")
def index():
    """Renders the main web chat interface."""
    return render_template("index.html")


@app.route("/api/chat", methods=["POST"])
def chat():
    """Endpoint to answer a user's question."""
    data = request.get_json() or {}
    query = data.get("query", "").strip()

    if not query:
        return jsonify({
            "error": "Query cannot be empty.",
            "matched": False
        }), 400

    response = chatbot.ask(query)
    return jsonify({
        "success": True,
        "query": query,
        "response": response
    })


@app.route("/api/topics", methods=["GET"])
def topics():
    """Returns all topics and knowledge base statistics."""
    kb = chatbot.engine.knowledge_base
    topic_map = {}
    for item in kb:
        t = item.get("topic", "General")
        topic_map[t] = topic_map.get(t, 0) + 1

    return jsonify({
        "total_entries": len(kb),
        "topics": topic_map
    })


@app.route("/api/sample-questions", methods=["GET"])
def sample_questions():
    """Returns a list of sample questions."""
    samples = []
    for item in chatbot.engine.knowledge_base:
        if item.get("patterns"):
            samples.append({
                "id": item["id"],
                "topic": item.get("topic", "General"),
                "question": item["patterns"][0]
            })
    return jsonify({
        "samples": samples
    })


@app.route("/api/clear", methods=["POST"])
def clear_history():
    """Clears chatbot conversation history."""
    chatbot.clear_history()
    return jsonify({"status": "cleared"})


if __name__ == "__main__":
    import sys
    if sys.stdout.encoding != "utf-8":
        try:
            sys.stdout.reconfigure(encoding="utf-8")
        except AttributeError:
            pass
    port = int(os.environ.get("PORT", 5500))
    print(f"[*] Starting Python QA Chatbot server at http://127.0.0.1:{port}")
    app.run(host="127.0.0.1", port=port, debug=False)

