import requests

def check_page_start(url):
    response = requests.get(url)
    if response.status_code == 200:
        content = response.text
        if "Для того чтобы установить библиотеку Python в Laravel, нужно сначала добавить зависимость в файл composer.json" in content:
            print("Страница начинается с прямого ответа")
        else:
            print("Страница не начинается с прямого ответа")
    else:
        print("Не удалось получить страницу")

if __name__ == "__main__":
    url = "https://example.com/python-laravel-integration"
    check_page_start(url)