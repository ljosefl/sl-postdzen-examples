from langchain.agents import create_pandas_dataframe_agent
from langchain.prompts import PromptTemplate
from langchain.tools import run_tool
from langchain.callbacks.base import CallbackManager
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler
from langchain.chains import LLMChain
from langchain.llms import OpenAI
from langchain.vectorstores import FAISS
from langchain.embeddings import OpenAIEmbeddings
from pydantic import BaseModel, Field
import os
import pandas as pd

class Query(BaseModel):
    query: str = Field(description="Запрос пользователя")

class Tool(BaseModel):
    name: str = Field(description="Имя инструмента")
    description: str = Field(description="Описание инструмента")
    tool: str = Field(description="Команда для вызова инструмента")

class Agent:
    def __init__(self, llm, tool_names, tool_descriptions, callback_manager=None):
        self.llm = llm
        self.tool_names = tool_names
        self.tool_descriptions = tool_descriptions
        self.callback_manager = callback_manager or CallbackManager([StreamingStdOutCallbackHandler()])
        self.tools = [Tool(name=name, description=description, tool=tool) for name, description, tool in zip(tool_names, tool_descriptions, tool_names)]
        self.memory = FAISS.from_documents([], OpenAIEmbeddings())
        self.agent = create_pandas_dataframe_agent(
            pd.read_csv('data.csv'), llm, 
            verbose=True, 
            callbacks=self.callback_manager, 
            tool_names=tool_names, 
            tool_descriptions=tool_descriptions
        )

    def run(self, query: str) -> str:
        prompt_template = PromptTemplate(
            template="Пользователь: {query}\nАгент: ",
            input_variables=["query"]
        )
        llm_chain = LLMChain(llm=self.llm, prompt=prompt_template, callbacks=self.callback_manager)
        plan = llm_chain.run(query)
        for step in plan:
            result = run_tool(step, tool_names=self.tool_names, tool_descriptions=self.tool_descriptions)
            plan = llm_chain.run(plan)
        return plan

if __name__ == "__main__":
    llm = OpenAI(temperature=0.7)
    tool_names = ["search_web", "search_db", "calculate"]
    tool_descriptions = ["Поиск по сети", "Поиск в базе данных", "Вычисление"]
    agent = Agent(llm, tool_names, tool_descriptions)
    query = Query(query="Какие книги написал А.С. Пушкин?")
    result = agent.run(query.query)
    print(result)