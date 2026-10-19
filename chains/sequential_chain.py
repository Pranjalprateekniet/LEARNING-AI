from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
import os
load_dotenv()

model = ChatOpenAI(
    model="openai/gpt-oss-20b",
    api_key=os.getenv("NVIDIA_API_KEY"),
    base_url="https://integrate.api.nvidia.com/v1",
    temperature=0,
    timeout=120,
    max_retries=1,
    max_tokens=4096,
)

prompt1=PromptTemplate(
    template='Generate a report of 100 words on the {topic}',
    input_variables=['topic']
)

prompt2=PromptTemplate(
    template='Generate a 5 pointer summary on the following text\n {text}',
    input_variables=['text']
)

parser=StrOutputParser()

chain=prompt1 | model| parser| prompt2 | model| parser

result=chain.invoke({'topic': 'Unemployment in india'})

print(result)

chain.get_graph().print_ascii()

