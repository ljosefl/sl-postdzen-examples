# Пример кода для управления несколькими ботами в одном OpenClaw

# Импортируем необходимые библиотеки
from bot1 import Bot1
from bot2 import Bot2
from bot3 import Bot3

# Создаем экземпляры ботов
bot1 = Bot1()
bot2 = Bot2()
bot3 = Bot3()

# Функция для управления ботами
def manage_bots(bot1, bot2, bot3):
    # Добавьте здесь логику управления ботами
    bot1.send_message('Привет!')
    bot2.send_message('Здравствуйте!')
    bot3.send_message('Hello!')

# Вызов функции для управления ботами
manage_bots(bot1, bot2, bot3)