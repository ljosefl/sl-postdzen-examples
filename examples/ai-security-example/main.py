import logging
from typing import Any

# Конфигурация логирования
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def process_data(data: Any) -> None:
    """
    Пример функции обработки данных с базовой проверкой и логированием.
    """
    if not isinstance(data, str):
        logging.error("Некорректный тип данных. Ожидается строка.")
        return

    # Пример обработки данных
    logging.info(f"Обработка данных: {data}")

def main() -> None:
    """
    Точка входа в программу.
    """
    try:
        # Пример входных данных
        input_data = "Пример данных"
        process_data(input_data)
    except Exception as e:
        logging.error(f"Произошла ошибка: {e}")

if __name__ == "__main__":
    main()