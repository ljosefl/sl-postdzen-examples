import requests
from datetime import datetime

# Функция для покупки авиабилета
def buy_flight_ticket(api_key, flight_details):
    url = "https://api.airline.com/book"
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    response = requests.post(url, json=flight_details, headers=headers)
    if response.status_code == 200:
        print("Авиабилет успешно приобретен.")
    else:
        print(f"Ошибка при покупке авиабилета: {response.status_code}")

# Функция для заказа кофе
def order_coffee(api_key, coffee_details):
    url = "https://api.coffee_delivery.com/order"
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    response = requests.post(url, json=coffee_details, headers=headers)
    if response.status_code == 200:
        print("Кофе успешно заказан.")
    else:
        print(f"Ошибка при заказе кофе: {response.status_code}")

# Функция для проверки входных данных
def validate_input(data):
    if not data.get("address"):
        raise ValueError("Адрес не указан.")
    if not data.get("card_number"):
        raise ValueError("Номер карты не указан.")

# Точка входа
if __name__ == "__main__":
    # Пример данных для покупки авиабилета
    flight_details = {
        "flight_number": "AB123",
        "date": "2023-10-01",
        "passenger_name": "Alice",
        "card_number": "4111111111111111"
    }
    
    # Пример данных для заказа кофе
    coffee_details = {
        "address": "123 Main St, City",
        "coffee_type": "Espresso",
        "card_number": "4444444444444444"
    }
    
    try:
        # Проверка и валидация входных данных
        validate_input(flight_details)
        validate_input(coffee_details)
        
        # Покупка авиабилета
        buy_flight_ticket("YOUR_API_KEY", flight_details)
        
        # Накопление кофе
        order_coffee("YOUR_API_KEY", coffee_details)
    except ValueError as e:
        print(f"Ошибка валидации данных: {e}")