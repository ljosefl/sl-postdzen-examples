import pymongo
from pymongo import MongoClient
from sklearn.ensemble import RandomForestClassifier
import json

# Подключение к MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["medical_records"]
collection = db["patient_records"]

# Загрузка данных из MongoDB
def load_data():
    records = collection.find()
    data = []
    for record in records:
        data.append({
            "date": record["date"],
            "diagnosis": record["diagnosis"],
            "treatment": record["treatment"]
        })
    return data

# Обучение модели машинного обучения
def train_model(data):
    X = [record["diagnosis"] for record in data]
    y = [record["treatment"] for record in data]
    model = RandomForestClassifier()
    model.fit(X, y)
    return model

# Анализ данных
def analyze_data(model, patient_data):
    prediction = model.predict([patient_data["diagnosis"]])
    return {"prediction": prediction[0]}

# Пример использования
if __name__ == "__main__":
    data = load_data()
    model = train_model(data)
    patient_data = {"date": "2023-01-01", "diagnosis": "Flu"}
    prediction = analyze_data(model, patient_data)
    print(json.dumps(prediction, indent=2))