import requests
from datetime import datetime
from time import sleep

class TokenMonitor:
    def __init__(self, api_url):
        self.api_url = api_url

    def fetch_token_usage(self):
        response = requests.get(self.api_url)
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(f"Failed to fetch token usage: {response.status_code}")

    def monitor_token_usage(self, interval=60):
        while True:
            usage = self.fetch_token_usage()
            print(f"Token usage at {datetime.now()}: {usage['tokens']} tokens")
            sleep(interval)

class AlgorithmOptimizer:
    def __init__(self, algorithm):
        self.algorithm = algorithm

    def optimize(self):
        # Placeholder for actual optimization logic
        print("Optimizing algorithm...")
        # Simulate optimization by reducing token usage by 10%
        self.algorithm['token_usage'] *= 0.9
        print(f"Optimized algorithm token usage: {self.algorithm['token_usage']} tokens")

def main():
    api_url = "http://localhost:8000/api/token_usage"
    monitor = TokenMonitor(api_url)
    optimizer = AlgorithmOptimizer({'token_usage': 1000000})

    print("Starting token usage monitoring...")
    monitor.monitor_token_usage()

    print("Starting algorithm optimization...")
    optimizer.optimize()

if __name__ == "__main__":
    main()