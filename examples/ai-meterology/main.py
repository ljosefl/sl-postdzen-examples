import requests
from bs4 import BeautifulSoup
from typing import List, Tuple

def fetch_data(url: str) -> List[Tuple[str, float]]:
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    table = soup.find('table')
    rows = table.find_all('tr')[1:]  # Skip header row
    data = [(row.find_all('td')[0].text.strip(), float(row.find_all('td')[1].text.strip()))
            for row in rows]
    return data

def check_data_quality(data: List[Tuple[str, float]]) -> bool:
    for item in data:
        if not isinstance(item[0], str) or not isinstance(item[1], float):
            return False
    return True

def verify_output(data: List[Tuple[str, float]]) -> bool:
    if not check_data_quality(data):
        return False
    
    # Dummy check: ensure all values are positive
    if any(value <= 0 for _, value in data):
        return False
    
    return True

def main():
    url = "https://example.com/data"  # Example URL
    data = fetch_data(url)
    if verify_output(data):
        print("Output is verified.")
    else:
        print("Output verification failed.")

if __name__ == "__main__":
    main()