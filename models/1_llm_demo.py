from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os

load_dotenv()

llm=ChatOpenAI(model="openai/gpt-oss-20b",
               api_key=os.getenv("NVIDIA_API_KEY"),
               base_url="https://integrate.api.nvidia.com/v1",
               temperature=1)

result = llm.invoke("Write a 5 line poem on cricket")
print(result.content)
