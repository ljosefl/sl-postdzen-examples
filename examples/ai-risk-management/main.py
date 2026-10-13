import requests
from flask import Flask, request
from flask_cors import CORS
import json

app = Flask(__name__)
CORS(app)

# Simulated AI agent endpoint
AI_AGENT_URL = "http://localhost:5001/api/ai-agent"

@app.route('/test-ai-agent', methods=['POST'])
def test_ai_agent():
    try:
        data = request.json
        response = requests.post(AI_AGENT_URL, json=data)
        response.raise_for_status()
        result = response.json()
        print("AI Agent Response:", result)
        return "Test successful", 200
    except Exception as e:
        print("Error testing AI agent:", e)
        return "Test failed", 500

if __name__ == "__main__":
    app.run(port=5000)