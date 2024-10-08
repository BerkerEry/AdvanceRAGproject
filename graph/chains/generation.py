from langchain import hub
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser


llm = ChatOpenAI(temperature=0)
prompt = hub.pull("rlm/rag-prompt") #langsmith link

generation_chain = prompt | llm | StrOutputParser()
