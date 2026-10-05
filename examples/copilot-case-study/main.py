import requests
from copilot import Copilot

def main():
    # Инициализация Copilot
    copilot = Copilot(api_key="YOUR_API_KEY")

    # Загрузка исходного кода
    with open("original_code.py", "r") as file:
        original_code = file.read()

    # Переписывание кода ИИ-агентом
    new_code = copilot.rewrite_code(original_code)

    # Сохранение нового кода
    with open("rewritten_code.py", "w") as file:
        file.write(new_code)

    # Проверка качества кода
    quality_check_passed = copilot.check_code_quality(new_code)

    if quality_check_passed:
        print("Код успешно переписан и прошел проверку качества.")
    else:
        print("Код переписан, но не прошел проверку качества.")

if __name__ == "__main__":
    main()