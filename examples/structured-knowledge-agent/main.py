from langchain.chains import RetrievalQA
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import FAISS
from langchain.text_splitter import CharacterTextSplitter
from langchain.document_loaders import TextLoader
from langchain.llms import HuggingFaceHub
import os

# Загрузка данных и их разбиение на части
loader = TextLoader("agents.md")
documents = loader.load()
text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
texts = text_splitter.split_documents(documents)

# Создание векторной базы данных
db = FAISS.from_documents(texts, HuggingFaceEmbeddings())

# Инициализация модели
llm = HuggingFaceHub(repo_id="google/flan-t5-xxl", model_kwargs={"temperature":0.6, "max_length":64})

# Создание системы RAG
qa = RetrievalQA.from_chain_type(llm=llm, chain_type="stuff", retriever=db.as_retriever())

# Запрос к системе
query = "Какие знания используются для обучения AI-агента?"
result = qa.run(query)
print(result)