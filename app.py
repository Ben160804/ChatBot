from flask import Flask, request, jsonify
from services.groq_service import get_groq_response
from config import GROQ_API_KEY
import os

# Load prompt from file
with open("prompts/travel_prompt.txt", "r", encoding="utf-8") as f:
    TRAVEL_PROMPT = f.read()

app = Flask(__name__)

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    user_input = data.get("message", "").strip()

    if not user_input:
        return jsonify({"error": "No message provided"}), 400

    try:
        reply = get_groq_response(TRAVEL_PROMPT, user_input)
        return jsonify({"reply": reply})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
