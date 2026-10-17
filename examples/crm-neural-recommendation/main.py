import requests
from bs4 import BeautifulSoup

def get_crm_recommendations():
    """
    Функция для получения рекомендаций CRM-систем от различных ИИ-агентов.
    """
    ai_agents = {
        "AliceAI": "https://api.aliceai.com/crm",
        "DeepSeek": "https://api.deepeek.com/crm",
        "ChatGPT": "https://api.chatgpt.com/crm",
        "GigaChat": "https://api.gigachat.com/crm"
    }

    recommendations = {}

    for agent, url in ai_agents.items():
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            recommendations[agent] = [item.text for item in soup.find_all('div', class_='crm-system')]
        else:
            recommendations[agent] = ["Error: Unable to fetch data"]

    return recommendations

def analyze_recommendations(recommendations):
    """
    Функция для анализа рекомендаций CRM-систем.
    """
    analysis = {
        "integration_cloud_services": [],
        "scalability_and_reliability": [],
        "analytics_and_reporting": []
    }

    for agent, systems in recommendations.items():
        for system in systems:
            if system == "Salesforce":
                analysis["integration_cloud_services"].append(system)
                analysis["scalability_and_reliability"].append(system)
            elif system == "Pipedrive":
                analysis["integration_cloud_services"].append(system)
            elif system == "Zoho":
                analysis["integration_cloud_services"].append(system)
                analysis["scalability_and_reliability"].append(system)
            elif system == "HubSpot":
                analysis["integration_cloud_services"].append(system)
            elif system == "SugarCRM":
                analysis["analytics_and_reporting"].append(system)
            elif system == "Oracle CRM OnDemand":
                analysis["scalability_and_reliability"].append(system)

    return analysis

def main():
    """
    Точка входа в программу.
    """
    recommendations = get_crm_recommendations()
    print("Recommendations from AI agents:")
    for agent, systems in recommendations.items():
        print(f"{agent}: {systems}")

    analysis = analyze_recommendations(recommendations)
    print("\nAnalysis of recommendations:")
    print("Integration with cloud services:", analysis["integration_cloud_services"])
    print("Scalability and reliability:", analysis["scalability_and_reliability"])
    print("Analytics and reporting:", analysis["analytics_and_reporting"])

if __name__ == "__main__":
    main()