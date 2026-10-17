from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel,Field
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

class Person(BaseModel):
    name: str=Field(description='Name of the person')
    age:  int=Field(description='Age of the person')
    city: str=Field(description='Name of the city the person belongs to')

parser=PydanticOutputParser(pydantic_object=Person)
template=PromptTemplate(
    template='Generate the name,age and city of a fictional {place} person \n {format_instruction}',
    input_variables=['place'],
    partial_variables={'format_instruction': parser.get_format_instructions()}
)

# prompt=template.invoke({'place': 'indian'})
# print(prompt)

# result=model.invoke(prompt)

# final_result=parser.parse(result.content)

chain = template|model|parser

final_result=chain.invoke({'place' : 'Russian'})

print(final_result)

