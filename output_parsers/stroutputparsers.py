from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
import os

load_dotenv()

model = ChatOpenAI(
    model="openai/gpt-oss-20b",
    api_key=os.getenv("NVIDIA_API_KEY"),
    base_url="https://integrate.api.nvidia.com/v1",
    temperature=0,
)

template1=PromptTemplate(
    template='Write a detailed report on the {topic}',
    input_variables=['topic']
)

template2=PromptTemplate(
    template='Write a 5 line summary on the following text\n {text}',
    input_variables=['text']
)

prompt1=template1.invoke({'topic':'blackhole'})

result=model.invoke(prompt1)

prompt2=template2.invoke({'text':result.content})

result1= model.invoke(prompt2)

print(result1.content)