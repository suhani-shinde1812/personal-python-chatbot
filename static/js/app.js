document.addEventListener("DOMContentLoaded", () => {
    loadTopics();
    loadSampleQuestions();

    document.getElementById("clear-chat-btn").addEventListener("click", clearChat);
});

async function loadTopics() {
    try {
        const res = await fetch("/api/topics");
        const data = await res.json();

        document.getElementById("total-kb-count").textContent = data.total_entries;
        document.getElementById("total-topics-count").textContent = Object.keys(data.topics).length;

        const topicsList = document.getElementById("topics-list");
        // Keep "All Topics" tag
        topicsList.innerHTML = `<span class="topic-tag active" onclick="filterByTopic('all', this)">All Topics</span>`;

        for (const [topicName, count] of Object.entries(data.topics)) {
            const span = document.createElement("span");
            span.className = "topic-tag";
            span.textContent = `${topicName} (${count})`;
            span.onclick = function() { filterByTopic(topicName, this); };
            topicsList.appendChild(span);
        }
    } catch (err) {
        console.error("Failed to load topics:", err);
    }
}

async function loadSampleQuestions() {
    try {
        const res = await fetch("/api/sample-questions");
        const data = await res.json();
        const container = document.getElementById("sidebar-samples");
        container.innerHTML = "";

        data.samples.slice(0, 7).forEach(item => {
            const btn = document.createElement("button");
            btn.className = "sample-item";
            btn.textContent = item.question;
            btn.title = `Topic: ${item.topic}`;
            btn.onclick = () => {
                document.getElementById("query-input").value = item.question;
                submitQuery(item.question);
            };
            container.appendChild(btn);
        });
    } catch (err) {
        console.error("Failed to load sample questions:", err);
    }
}

function filterByTopic(topic, element) {
    document.querySelectorAll(".topic-tag").forEach(el => el.classList.remove("active"));
    element.classList.add("active");

    const queryInput = document.getElementById("query-input");
    if (topic !== "all") {
        queryInput.value = `Tell me about ${topic} in Python`;
    }
    queryInput.focus();
}

function askSuggestion(button) {
    const text = button.textContent.trim();
    document.getElementById("query-input").value = text;
    submitQuery(text);
}

function handleSend(event) {
    event.preventDefault();
    const input = document.getElementById("query-input");
    const query = input.value.trim();
    if (!query) return;

    submitQuery(query);
    input.value = "";
}

async function submitQuery(query) {
    appendUserMessage(query);

    const typing = document.getElementById("typing-indicator");
    typing.classList.add("active");
    scrollToBottom();

    try {
        const response = await fetch("/api/chat", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({ query: query })
        });

        const data = await response.json();
        typing.classList.remove("active");

        if (data.success && data.response) {
            appendBotMessage(data.response);
        } else {
            appendBotMessage({
                answer: "Sorry, I encountered an error processing your query. Please try again.",
                topic: "Error",
                confidence: 0
            });
        }
    } catch (err) {
        typing.classList.remove("active");
        appendBotMessage({
            answer: "Network error: Unable to connect to the chatbot server.",
            topic: "Error",
            confidence: 0
        });
        console.error(err);
    }
}

function appendUserMessage(text) {
    const container = document.getElementById("messages-container");
    const msg = document.createElement("div");
    msg.className = "message user-message";

    const time = new Date().toLocaleTimeString([], { hour: "2-digit", minute: "2-digit" });

    msg.innerHTML = `
        <div class="msg-avatar">You</div>
        <div class="msg-content">
            <div class="msg-bubble">${escapeHtml(text)}</div>
            <span class="msg-timestamp">${time}</span>
        </div>
    `;

    container.appendChild(msg);
    scrollToBottom();
}

function appendBotMessage(resp) {
    const container = document.getElementById("messages-container");
    const msg = document.createElement("div");
    msg.className = "message bot-message";

    const time = new Date().toLocaleTimeString([], { hour: "2-digit", minute: "2-digit" });

    let metaBadges = "";
    if (resp.topic && resp.topic !== "Greeting" && resp.topic !== "Error") {
        const confPercent = resp.confidence ? Math.round(resp.confidence * 100) : 0;
        metaBadges = `
            <div class="meta-badge-row">
                <span class="topic-badge">${escapeHtml(resp.topic)}</span>
                ${confPercent > 0 ? `<span class="confidence-badge">${confPercent}% Match</span>` : ""}
            </div>
        `;
    }

    // Format Markdown-like text (bold, bullet points, inline code)
    const formattedAnswer = formatMarkdown(resp.answer);

    // Code snippet
    let codeHtml = "";
    if (resp.code_example && resp.code_example.trim()) {
        const codeId = "code-" + Math.random().toString(36).substring(2, 9);
        codeHtml = `
            <div class="code-container">
                <div class="code-header">
                    <span>Python Example</span>
                    <button class="copy-btn" onclick="copyCode('${codeId}', this)">
                        <svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                            <rect x="9" y="9" width="13" height="13" rx="2" ry="2"></rect>
                            <path d="M5 15H4a2 2 0 01-2-2V4a2 2 0 012-2h9a2 2 0 012 2v1"></path>
                        </svg>
                        Copy
                    </button>
                </div>
                <pre><code id="${codeId}">${escapeHtml(resp.code_example)}</code></pre>
            </div>
        `;
    }

    // Related suggestion chips
    let suggestionsHtml = "";
    if (resp.related_questions && resp.related_questions.length > 0) {
        suggestionsHtml = `
            <div class="suggestion-chips">
                ${resp.related_questions.map(q => `<button class="chip" onclick="askSuggestion(this)">${escapeHtml(q)}</button>`).join("")}
            </div>
        `;
    }

    msg.innerHTML = `
        <div class="msg-avatar">🐍</div>
        <div class="msg-content">
            <div class="msg-bubble">
                ${metaBadges}
                <div class="bot-answer-text">${formattedAnswer}</div>
                ${codeHtml}
                ${suggestionsHtml}
            </div>
            <span class="msg-timestamp">${time}</span>
        </div>
    `;

    container.appendChild(msg);
    scrollToBottom();
}

function formatMarkdown(text) {
    if (!text) return "";
    let s = escapeHtml(text);

    // Convert **bold**
    s = s.replace(/\*\*(.*?)\*\*/g, "<strong>$1</strong>");

    // Convert `code`
    s = s.replace(/`([^`]+)`/g, "<code style='background:rgba(255,255,255,0.08);padding:2px 5px;border-radius:4px;font-family:var(--font-mono);font-size:0.85em;color:#38bdf8;'>$1</code>");

    // Convert newlines to breaks or bullet format
    return s;
}

function copyCode(elementId, btn) {
    const codeEl = document.getElementById(elementId);
    if (!codeEl) return;

    navigator.clipboard.writeText(codeEl.textContent).then(() => {
        const originalText = btn.innerHTML;
        btn.innerHTML = `✓ Copied!`;
        btn.style.color = "#10b981";
        setTimeout(() => {
            btn.innerHTML = originalText;
            btn.style.color = "";
        }, 2000);
    });
}

async function clearChat() {
    if (!confirm("Are you sure you want to clear conversation history?")) return;

    try {
        await fetch("/api/clear", { method: "POST" });
        const container = document.getElementById("messages-container");
        container.innerHTML = `
            <div class="message bot-message">
                <div class="msg-avatar">🐍</div>
                <div class="msg-content">
                    <div class="msg-bubble">
                        <p><strong>Chat history cleared!</strong></p>
                        <p>Ask any new question about Python programming.</p>
                        <div class="suggestion-chips">
                            <button class="chip" onclick="askSuggestion(this)">What is Python?</button>
                            <button class="chip" onclick="askSuggestion(this)">Explain OOP concepts in Python</button>
                            <button class="chip" onclick="askSuggestion(this)">What is the difference between list and tuple?</button>
                        </div>
                    </div>
                    <span class="msg-timestamp">Just now</span>
                </div>
            </div>
        `;
    } catch (err) {
        console.error("Failed to clear chat:", err);
    }
}

function scrollToBottom() {
    const container = document.getElementById("messages-container");
    container.scrollTop = container.scrollHeight;
}

function escapeHtml(str) {
    if (!str) return "";
    return str
        .replace(/&/g, "&amp;")
        .replace(/</g, "&lt;")
        .replace(/>/g, "&gt;")
        .replace(/"/g, "&quot;")
        .replace(/'/g, "&#039;");
}
