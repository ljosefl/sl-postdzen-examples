import os
import requests

def check_code_quality(url):
    """
    Проверяет качество кода на сервере, используя инструмент ub-mode.
    """
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        if data['status'] == 'success':
            print("Код прошел проверку ub-mode.")
        else:
            print("Код не прошел проверку ub-mode:", data['message'])
    else:
        print("Не удалось получить данные о качестве кода:", response.status_code)

if __name__ == "__main__":
    # URL сервера, который предоставляет данные о качестве кода
    server_url = "http://localhost:8000/check_code_quality"
    check_code_quality(server_url)