# Импорт необходимых библиотек
from camera import Camera
from accounting import Accounting
from reporting import Reporting

# Функция для запуска системы автоматизации
def main():
    # Инициализация камер
    cameras = [Camera(f'camera_{i}') for i in range(10)]

    # Инициализация касс
    accountings = [Accounting(f'accounting_{i}') for i in range(10)]

    # Инициализация отчетности
    reporting = Reporting()

    # Запуск камер и касс
    for camera, accounting in zip(cameras, accountings):
        camera.start()
        accounting.start()

    # Анализ данных
    reporting.analyze()

    # Завершение работы
    for camera in cameras:
        camera.stop()
    for accounting in accountings:
        accounting.stop()

if __name__ == '__main__':
    main()