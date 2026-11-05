import requests
from langchain.chains import RetrievalAugmentedGenerationChain
from langchain.prompts import PromptTemplate
from langchain.cache import InMemoryCache

# Инициализация кэша
InMemoryCache()

# Пример данных для анализа
data = "Пример данных для анализа"

# Инициализация RAG-цепочки
rag_chain = RetrievalAugmentedGenerationChain.from_llm(
    llm=requests.Session(), 
    prompt=PromptTemplate(template="Разберитесь с {data}", input_variables=["data"])
)

# Пример запроса
response = rag_chain.run(data)

print(f"Результат анализа: {response}")