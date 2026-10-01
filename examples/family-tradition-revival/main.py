import json
from flask import Flask, request, jsonify

app = Flask(__name__)

# Символы артефакта, которые отображают семейные истории
family_symbols = {
    "symbol1": "Символ любви",
    "symbol2": "Символ уважения",
    "symbol3": "Символ верности"
}

# Функция для обработки мыслей и эмоций пользователя
def process_thoughts(thoughts):
    # Простая обработка мыслей и эмоций
    if "love" in thoughts:
        return family_symbols["symbol1"]
    elif "respect" in thoughts:
        return family_symbols["symbol2"]
    elif "loyalty" in thoughts:
        return family_symbols["symbol3"]
    return None

@app.route('/react', methods=['POST'])
def react():
    data = request.json
    thoughts = data.get('thoughts', '')
    symbol = process_thoughts(thoughts)
    if symbol:
        return jsonify({"symbol": symbol})
    else:
        return jsonify({"error": "No matching symbol found"}), 400

if __name__ == "__main__":
    app.run(debug=True)