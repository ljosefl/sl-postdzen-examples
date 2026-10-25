import requests
from langchain import LangChain
from openai import OpenAI
from copilot import Copilot

def compare_agents():
    """
    Сравнивает эффективность различных ИИ-агентов для автоматизации задач разработки.
    """

    # Инициализация агентов
    langchain = LangChain()
    openai = OpenAI()
    copilot = Copilot()

    # Задача для тестирования
    task = "Write a function to calculate the factorial of a number."

    # Генерация кода с помощью каждого агента
    langchain_code = langchain.generate_code(task)
    openai_code = openai.generate_code(task)
    copilot_code = copilot.generate_code(task)

    # Отправка кода на проверку качества
    def check_code(implementation):
        response = requests.post("https://api.qualitychecker.com/validate", json={"code": implementation})
        return response.json()

    langchain_result = check_code(langchain_code)
    openai_result = check_code(openai_code)
    copilot_result = check_code(copilot_code)

    # Вывод результатов
    print("LangChain Result:", langchain_result)
    print("OpenAI Result:", openai_result)
    print("Copilot Result:", copilot_result)

if __name__ == "__main__":
    compare_agents()