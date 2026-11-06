import requests
from langchain import LangChain
from transformers import pipeline

# Инициализация LangChain
langchain = LangChain()

# Инициализация модели Hugging Face для анализа текста
text_classifier = pipeline("text-classification", model="distilbert-base-uncased-finetuned-sst-2-english")

# Инициализация модели Hugging Face для анализа изображений
image_classifier = pipeline("image-classification", model="microsoft/resnet-50")

def analyze_company_info(url):
    # Используем LangChain для сбора информации о компании
    company_info = langchain.get_company_info(url)
    
    # Анализ текста из информации о компании
    text_analysis = text_classifier(company_info['description'])
    
    # Анализ изображений из информации о компании
    image_analysis = image_classifier(company_info['logo_url'])
    
    return text_analysis, image_analysis

if __name__ == "__main__":
    url = "https://example.com"
    text_analysis, image_analysis = analyze_company_info(url)
    print("Text Analysis:", text_analysis)
    print("Image Analysis:", image_analysis)