import requests
import json

class DotAssistant:
    def __init__(self, api_url):
        self.api_url = api_url

    def create_task(self, task_description):
        payload = {
            "task_description": task_description,
            "access_level": "private"
        }
        response = requests.post(f"{self.api_url}/tasks", json=payload)
        if response.status_code == 201:
            return response.json()
        else:
            raise Exception(f"Failed to create task: {response.status_code}")

    def get_tasks(self):
        response = requests.get(f"{self.api_url}/tasks")
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(f"Failed to get tasks: {response.status_code}")

if __name__ == "__main__":
    assistant = DotAssistant("http://localhost:8000/api/v1")
    try:
        task = assistant.create_task("Buy groceries")
        print("Task created:", task)
        tasks = assistant.get_tasks()
        print("Tasks:", tasks)
    except Exception as e:
        print(e)