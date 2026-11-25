import requests
from bs4 import BeautifulSoup

def fetch_posts(url):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        posts = soup.find_all('div', class_='post')
        return [post.text for post in posts]
    return []

def detect_ai_bots(posts):
    ai_bots_count = 0
    for post in posts:
        if "как результат спланированной кибератаки" in post or "слухи о кибератаке" in post:
            ai_bots_count += 1
    return ai_bots_count

def main():
    url = "https://example.com/posts"  # URL для получения постов
    posts = fetch_posts(url)
    ai_bots_count = detect_ai_bots(posts)
    print(f"ИИ-боты создали {ai_bots_count} из {len(posts)} постов.")

if __name__ == "__main__":
    main()