import sqlite3
from memshelf import MemShelf

class IIAgent:
    def __init__(self):
        self.memshelf = MemShelf()

    def load_data(self):
        conn = sqlite3.connect('data.db')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM data")
        rows = cursor.fetchall()
        conn.close()
        return rows

    def save_data(self, data):
        conn = sqlite3.connect('data.db')
        cursor = conn.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS data (id INTEGER PRIMARY KEY, value TEXT)")
        cursor.executemany("INSERT INTO data (value) VALUES (?)", [(d,) for d in data])
        conn.commit()
        conn.close()

    def process_data(self, data):
        processed_data = [f"Processed {d}" for d in data]
        self.memshelf.save(processed_data)
        return processed_data

if __name__ == "__main__":
    agent = IIAgent()
    data = agent.load_data()
    if data:
        processed_data = agent.process_data(data)
        agent.save_data(processed_data)