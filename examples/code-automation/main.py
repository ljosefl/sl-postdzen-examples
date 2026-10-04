import requests
import json

class CodeAgent:
    def __init__(self, api_url):
        self.api_url = api_url

    def fix_code(self, resource_id, chunk_name, error_message):
        payload = {
            "resource_id": resource_id,
            "chunk_name": chunk_name,
            "error_message": error_message
        }
        response = requests.post(f"{self.api_url}/fix-code", json=payload)
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(f"Error fixing code: {response.text}")

    def check_results(self, resource_id):
        response = requests.get(f"{self.api_url}/check-results/{resource_id}")
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(f"Error checking results: {response.text}")

if __name__ == "__main__":
    agent = CodeAgent("https://api.code-automation.com/v1")
    try:
        # Example task: Fix an error in a specific chunk of a resource
        fixed_code = agent.fix_code(resource_id=123, chunk_name="header", error_message="Incorrect syntax")
        print("Fixed code:", fixed_code)

        # Check the results
        results = agent.check_results(resource_id=123)
        print("Results:", results)
    except Exception as e:
        print(f"An error occurred: {e}")