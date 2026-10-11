import logging
from cosmos_harness.checklist import Checklist

def setup_logging():
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def main():
    setup_logging()
    checklist = Checklist()
    checklist.add_item("Настройка логирования и отслеживания действий ИИ-агентов")
    checklist.add_item("Создание правил для управления ИИ-агентами")
    checklist.add_item("Разработка алгоритмов для оптимизации работы ИИ-агентов")
    checklist.add_item("Проверка и тестирование ИИ-агентов на различных сценариях")
    checklist.add_item("Настройка системы уведомлений для оперативного реагирования на возможные проблемы")
    checklist.run()

if __name__ == "__main__":
    main()