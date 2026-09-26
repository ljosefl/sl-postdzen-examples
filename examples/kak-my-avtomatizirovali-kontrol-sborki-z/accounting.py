# Импорт необходимых библиотек
from threading import Thread
from time import sleep

# Класс для управления кассой
class Accounting:
    def __init__(self, name):
        self.name = name
        self.is_running = False
        self.sales = []

    def start(self):
        self.is_running = True
        thread = Thread(target=self.record_sales)
        thread.start()

    def stop(self):
        self.is_running = False
        sleep(1)  # Дождаться завершения записи
        self.sales.clear()

    def record_sales(self):
        while self.is_running:
            sale = record_sale()  # Здесь нужно реализовать функцию record_sale()
            self.sales.append(sale)

    def get_sales(self):
        return self.sales

# Функция для записи продажи
# В реальном коде это будет вызывать функцию, которая записывает продажу
# Например, с кассы или изображения
# В данном примере функция возвращает пустой список
# Для демонстрации
# def record_sale():
#     return []