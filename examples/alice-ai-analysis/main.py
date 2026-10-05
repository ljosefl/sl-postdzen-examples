import requests
from bs4 import BeautifulSoup
import json

# Функция для получения отзывов и рейтингов Алисы AI
def get_alice_reviews_and_ratings():
    url = "https://example.com/alice-reviews"  # Заглушка URL для примера
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    reviews = soup.find_all('div', class_='review')
    ratings = soup.find_all('div', class_='rating')
    
    alice_reviews = []
    alice_ratings = []
    
    for review, rating in zip(reviews, ratings):
        alice_reviews.append(review.text.strip())
        alice_ratings.append(int(rating.text.strip()))
    
    return alice_reviews, alice_ratings

# Функция для сравнения с конкурентами
def compare_with_competitors():
    competitors = {
        "Google Assistant": {"url": "https://example.com/google-assistant-reviews", "rating": 4.5},
        "Amazon Alexa": {"url": "https://example.com/amazon-alexa-reviews", "rating": 4.3},
        "Siri": {"url": "https://example.com/siri-reviews", "rating": 4.2}
    }
    
    for name, data in competitors.items():
        url = data["url"]
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        reviews = soup.find_all('div', class_='review')
        ratings = soup.find_all('div', class_='rating')
        
        reviews_count = len(reviews)
        average_rating = sum(int(rating.text.strip()) for rating in ratings) / reviews_count
        
        print(f"{name}: {reviews_count} отзывов, средний рейтинг {average_rating:.1f}")

# Функция для анализа пользовательского опыта
def analyze_user_experience(reviews, ratings):
    positive_reviews = [review for review, rating in zip(reviews, ratings) if rating >= 4]
    negative_reviews = [review for review, rating in zip(reviews, ratings) if rating < 4]
    
    print(f"Положительные отзывы: {len(positive_reviews)}")
    print(f"Отрицательные отзывы: {len(negative_reviews)}")

if __name__ == "__main__":
    alice_reviews, alice_ratings = get_alice_reviews_and_ratings()
    compare_with_competitors()
    analyze_user_experience(alice_reviews, alice_ratings)