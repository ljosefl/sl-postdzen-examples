import sonarqube

def main():
    # Инициализация клиента SonarQube
    sonar = sonarqube.SonarQubeClient(
        server='http://localhost:9000',
        token='your_api_token'
    )
    
    # Проверка проекта
    project_key = 'my_project_key'
    analysis = sonar.get_analysis(project_key)
    issues = sonar.get_issues(project_key)
    
    print("Analysis details:")
    print(analysis)
    
    print("\nIssues found:")
    for issue in issues:
        print(f"Rule: {issue['rule']}, Severity: {issue['severity']}, Message: {issue['message']}")

if __name__ == "__main__":
    main()