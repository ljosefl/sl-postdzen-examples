import requests
from vk_ai_space import VkAiSpace

# Инициализация VK AI Space
ai_space = VkAiSpace(api_key='your_api_key')

def load_documents():
    # Загрузка документов в VK AI Space
    documents = [
        {'file_name': 'policy1.pdf', 'content': 'Content of policy1'},
        {'file_name': 'manual1.pdf', 'content': 'Content of manual1'}
    ]
    for doc in documents:
        ai_space.upload_document(doc['file_name'], doc['content'])

def search_and_generate_answer(query):
    # Поиск и генерация ответа с использованием RAG
    response = ai_space.search(query)
    if response['success']:
        return response['answer']
    else:
        return "Информация не найдена"

if __name__ == "__main__":
    load_documents()
    query = "Какие есть внутренние положения компании?"
    answer = search_and_generate_answer(query)
    print(f"Ответ: {answer}")