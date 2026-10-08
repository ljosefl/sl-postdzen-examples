import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

def load_data(file_path):
    """Загружает данные из CSV файла."""
    return pd.read_csv(file_path)

def preprocess_data(data):
    """Обрабатывает данные: удаляет пропущенные значения и нормализует."""
    data.dropna(inplace=True)
    data = (data - data.mean()) / data.std()
    return data

def train_model(X_train, y_train):
    """Обучает модель линейной регрессии."""
    model = LinearRegression()
    model.fit(X_train, y_train)
    return model

def evaluate_model(model, X_test, y_test):
    """Оценивает модель на тестовых данных."""
    predictions = model.predict(X_test)
    mse = mean_squared_error(y_test, predictions)
    return mse

def main():
    """Основная функция для отладки AI-агента."""
    # Загрузка данных
    data = load_data('data.csv')
    print("Данные загружены.")
    
    # Проверка входных данных
    if not all(data.dtypes == 'float64'):
        raise ValueError("Входные данные должны быть числовыми.")
    
    # Предобработка данных
    data = preprocess_data(data)
    X = data.drop('target', axis=1)
    y = data['target']
    
    # Разделение на тренировочную и тестовую выборки
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # Обучение модели
    model = train_model(X_train, y_train)
    print("Модель обучена.")
    
    # Проверка логики обработки
    if model.coef_.shape != (X_train.shape[1],):
        raise ValueError("Коэффициенты модели неверного размера.")
    
    # Оценка модели
    mse = evaluate_model(model, X_test, y_test)
    print(f"Среднеквадратическая ошибка: {mse}")
    
    # Обзор финальных ответов
    predictions = model.predict(X_test)
    if not all(predictions >= 0):
        raise ValueError("Прогнозы модели отрицательны, что неверно.")
    
if __name__ == "__main__":
    main()