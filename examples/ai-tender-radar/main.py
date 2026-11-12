import requests
from memshelf import MemShelf

class TenderRadar:
    def __init__(self):
        self.data_store = MemShelf("tenders.db")

    def fetch_tenders(self):
        url = "https://api.goszakupov.ru/tenders"
        response = requests.get(url)
        response.raise_for_status()
        return response.json()

    def analyze_tender(self, tender):
        # Пример анализа: проверка наличия IT-оборудования
        if "IT" in tender.get("description", ""):
            return True
        return False

    def filter_tenders(self, tenders):
        filtered_tenders = []
        for tender in tenders:
            if self.analyze_tender(tender):
                filtered_tenders.append(tender)
        return filtered_tenders

    def process_tenders(self):
        tenders = self.fetch_tenders()
        filtered_tenders = self.filter_tenders(tenders)
        for tender in filtered_tenders:
            print(f"Processing tender: {tender['title']}")

if __name__ == "__main__":
    radar = TenderRadar()
    radar.process_tenders()