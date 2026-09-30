import requests
from dotenv import load_dotenv
import os

load_dotenv()

def get_gpt_response(prompt):
    url = "https://api.openai.com/v1/engines/davinci-codex/completions"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {os.getenv('OPENAI_API_KEY')}"
    }
    data = {
        "prompt": prompt,
        "max_tokens": 150
    }
    response = requests.post(url, headers=headers, json=data)
    return response.json().get("choices", [{}])[0].get("text", "")

def main():
    print("Привет! Я ваш персональный агент Dots. Как я могу вам помочь?")
    while True:
        user_input = input("Вы: ")
        if user_input.lower() in ["выход", "exit"]:
            print("До свидания!")
            break
        response = get_gpt_response(user_input)
        print(f"Dots: {response}")

if __name__ == "__main__":
    main()