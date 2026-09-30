import os
from langchain.chains import ConversationChain
from langchain.chains.conversation.memory import ConversationSummaryMemory
from langchain.llms import GoogleBard
from langchain.prompts import PromptTemplate

# Заглушка для Google Bard API
class MockGoogleBard(GoogleBard):
    def __call__(self, *args, **kwargs):
        return "Mock response from Google Bard"

# Инициализация LLM и памяти для агента
llm = MockGoogleBard()
memory = ConversationSummaryMemory(llm=llm)

# Шаблон для запросов к агенту
prompt = PromptTemplate(
    input_variables=["question"],
    template="Q: {question}\nA:"
)

# Инициализация агента
agent = ConversationChain(
    llm=llm,
    prompt=prompt,
    memory=memory
)

def main():
    # Пример работы агента
    question = "Какие цвета используются в FinAI?"
    response = agent(question)
    print(response)

if __name__ == "__main__":
    main()