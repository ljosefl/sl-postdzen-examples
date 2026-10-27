import requests

def fetch_copilot_recommendations():
    """
    Функция для получения рекомендаций от Copilot.
    """
    url = "https://api.copilot.com/v1/recommendations"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Failed to fetch recommendations: {response.status_code}")

def fetch_mcp_analysis():
    """
    Функция для получения анализа от MCP.
    """
    url = "https://api.mcp.com/v1/analysis"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Failed to fetch analysis: {response.status_code}")

def main():
    """
    Главная функция для демонстрации интеграции Copilot и MCP.
    """
    try:
        recommendations = fetch_copilot_recommendations()
        print("Copilot Recommendations:", recommendations)

        analysis = fetch_mcp_analysis()
        print("MCP Analysis:", analysis)
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()