import requests
from ai_code_reviewer import generate_code, refactor_code

def main():
    # Исходный код для генерации
    original_code = """
def example_function(x, y):
    return x + y
"""

    # Генерация кода с помощью ИИ-агента
    generated_code = generate_code(original_code)
    print("Generated code:")
    print(generated_code)

    # Рефакторинг кода с помощью ИИ-агента
    refactored_code = refactor_code(generated_code)
    print("\nRefactored code:")
    print(refactored_code)

    # Проверка кода с помощью реального инструмента (например, PyLint)
    response = requests.post("https://pylint.pycqa.org/en/latest/online.html", data={"module": refactored_code})
    if response.status_code == 200:
        print("\nCode passed the check by PyLint:")
        print(response.json()["messages"])
    else:
        print("\nCode failed the check by PyLint:")

if __name__ == "__main__":
    main()