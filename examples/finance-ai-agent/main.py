import requests
import json
from datetime import datetime

class FinanceAgent:
    def __init__(self, memshelf_url):
        self.memshelf_url = memshelf_url

    def log_expense(self, amount, category):
        data = {
            'timestamp': datetime.now().isoformat(),
            'amount': amount,
            'category': category
        }
        response = requests.post(f"{self.memshelf_url}/expenses", json=data)
        if response.status_code != 201:
            raise Exception(f"Failed to log expense: {response.text}")

    def get_expenses(self):
        response = requests.get(f"{self.memshelf_url}/expenses")
        if response.status_code != 200:
            raise Exception(f"Failed to get expenses: {response.text}")
        return response.json()

def main():
    memshelf_url = "http://localhost:8000"  # Заглушка для примера
    agent = FinanceAgent(memshelf_url)
    
    # Пример логирования расходов
    agent.log_expense(150, "food")
    agent.log_expense(20, "transport")
    
    # Получение всех расходов
    expenses = agent.get_expenses()
    print("Expenses:", expenses)

if __name__ == "__main__":
    main()