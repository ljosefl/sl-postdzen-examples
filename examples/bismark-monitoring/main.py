import requests
from datetime import datetime
import json

class Bismark:
    def __init__(self, name, birth_date, death_date=None):
        self.name = name
        self.birth_date = birth_date
        self.death_date = death_date

    def is_alive(self):
        if self.death_date:
            return self.death_date > datetime.now()
        return True

    def get_age(self):
        if self.death_date:
            return (self.death_date - self.birth_date).months
        return (datetime.now() - self.birth_date).months

class BismarkMonitor:
    def __init__(self, bismarks):
        self.bismarks = bismarks

    def update_bismarks(self):
        for bismark in self.bismarks:
            if bismark.is_alive():
                print(f"Checking {bismark.name}...")
                # Simulate checking the bismark's performance
                if self.check_performance(bismark):
                    print(f"{bismark.name} is still alive and performing well.")
                else:
                    print(f"{bismark.name} is not performing well. Replacing it.")
                    self.replace_bismark(bismark)

    def check_performance(self, bismark):
        # Simulate performance check
        return bismark.get_age() < 19

    def replace_bismark(self, bismark):
        # Simulate replacing the bismark
        print(f"Replacing {bismark.name} with a new one.")
        bismark.death_date = datetime.now()

if __name__ == "__main__":
    bismarks = [
        Bismark("Bismark1", datetime(2022, 1, 1)),
        Bismark("Bismark2", datetime(2023, 1, 1)),
        Bismark("Bismark3", datetime(2023, 1, 1), datetime(2024, 1, 1)),
    ]
    monitor = BismarkMonitor(bismarks)
    monitor.update_bismarks()