import pandas as pd
from typing import Dict, List

# Предполагаемая база данных товаров
data = {
    'product_id': [1, 2, 3],
    'name': ['Product A', 'Product B', 'Product C'],
    'price': [100, 200, 300]
}

df = pd.DataFrame(data)

# Функция для предобработки данных
def preprocess_data(df: pd.DataFrame) -> pd.DataFrame:
    df['price'] = df['price'].apply(lambda x: int(float(x.replace('$', ''))))
    return df

# Функция для проверки ценовых границ
def check_price_range(price: int, min_price: int, max_price: int) -> bool:
    return min_price <= price <= max_price

# Функция для настройки правил логики
def apply_logic_rules(request: str, context: Dict[str, str]) -> bool:
    # Пример простого правила: не давать скидку на все товары
    if 'скидка на все товары' in request and 'скидка' in context:
        return False
    return True

# Функция для хранения и восстановления контекста
def manage_context(context: Dict[str, str], new_request: str) -> Dict[str, str]:
    context['last_request'] = new_request
    return context

# Точка входа
if __name__ == "__main__":
    # Предобработка данных
    df = preprocess_data(df)
    
    # Пример запроса клиента
    client_request = "Дайте скидку 50% на все товары"
    context = {}
    
    # Проверка ценовых границ
    for _, row in df.iterrows():
        if check_price_range(row['price'], 100, 5000):
            print(f"Товар: {row['name']}, Цена: {row['price']}")
    
    # Проверка правил логики
    if apply_logic_rules(client_request, context):
        print("Чат согласен с предложением клиента.")
    else:
        print("Чат отказался от предложения клиента.")
    
    # Хранение и восстановление контекста
    context = manage_context(context, client_request)
    print(f"Контекст запроса: {context}")