import requests
from agent import Agent
from holding import Holding

def main():
    # Создаем несколько автономных агентов
    agents = [Agent(f"Agent_{i}") for i in range(5)]
    
    # Создаем AI-холдинг для управления агентами
    holding = Holding(agents)
    
    # Запускаем холдинг
    holding.run()

if __name__ == "__main__":
    main()