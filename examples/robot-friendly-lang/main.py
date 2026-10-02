import json

# Функция для преобразования данных в формат, понятный роботам
def to_robot_format(data):
    return json.dumps(data, ensure_ascii=False)

# Функция для обработки данных от роботов
def from_robot_format(data):
    return json.loads(data)

# Пример использования
if __name__ == "__main__":
    # Исходные данные для робота
    human_data = {
        "name": "RobotFriendlyLang",
        "version": "1.0",
        "features": ["AI", "Flexibility"]
    }
    
    # Преобразуем данные в формат, понятный роботам
    robot_data = to_robot_format(human_data)
    print("Отправленные данные роботу:", robot_data)
    
    # Получаем данные от робота
    robot_response = '{"name": "RobotFriendlyLang", "version": "1.0", "features": ["AI", "Flexibility"]}'
    human_response = from_robot_format(robot_response)
    print("Данные от робота:", human_response)