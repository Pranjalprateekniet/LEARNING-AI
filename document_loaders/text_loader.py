import os
from langchain_community.document_loaders import TextLoader
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

model = ChatGroq(model="openai/gpt-oss-20b")
prompt=PromptTemplate(
    template='write a summary of the following poem \n {poem}',
    input_variables=['poem']
)

parser=StrOutputParser()

loader=TextLoader('cricket.txt',encoding="utf-8")
documents=loader.load()
# print(documents)
# print(type(documents))
# print(len(documents))
# print(documents[0].page_content)
# print(documents[0].metadata)

chain=prompt | model | parser

print(chain.invoke({'poem':documents[0].page_content}))
