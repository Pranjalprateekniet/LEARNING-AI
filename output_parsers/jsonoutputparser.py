from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.output_parsers import JsonOutputParser
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
parser=JsonOutputParser()

template= PromptTemplate(
    template='Give me the name age and city of a fictional person \n {format_instruction}',
    input_variables=[],
    partial_variables={'format_instruction': parser.get_format_instructions()}
)
# prompt=template.format()
# result=model.invoke(prompt)
# final_result=parser.parse(result.content)

chain=template | model | parser
result=chain.invoke({})

print(result)
print(type(result))
print(result['name'])

