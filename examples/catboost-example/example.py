import numpy as np
from catboost import CatBoostClassifier

# Создание модели CatBoost
model = CatBoostClassifier(iterations=100, learning_rate=0.1)

# Обучение модели на датасете
model.fit(X_train, y_train)

# Предсказание на тестовом датасете
predictions = model.predict(X_test)

# Сравнение результатов
print(predictions)

# Завершение
print('Обучение и предсказание завершены. Результаты: ', predictions)