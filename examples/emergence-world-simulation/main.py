import requests

class SimpleAgent:
    def __init__(self):
        self.memory = []

    def observe(self, observation):
        self.memory.append(observation)
        return self.make_decision()

    def make_decision(self):
        # Простая логика на основе последних наблюдений
        if len(self.memory) > 2:
            last_two = self.memory[-2:]
            if "crisis" in last_two[0] and "crisis" in last_two[1]:
                return "prepare"
            elif "crisis" in last_two[0] and "recovery" in last_two[1]:
                return "adapt"
        return "wait"

def run_simulation(agent):
    base_url = "http://localhost:8000/api"
    for i in range(10):
        response = requests.get(f"{base_url}/status")
        status = response.json().get("status", "")
        decision = agent.observe(status)
        print(f"Status: {status}, Decision: {decision}")

if __name__ == "__main__":
    agent = SimpleAgent()
    run_simulation(agent)