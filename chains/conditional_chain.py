import os
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_nvidia_ai_endpoints import ChatNVIDIA
from langchain_core.runnables import RunnableParallel,RunnableBranch,RunnableLambda
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel,Field
from typing import Literal

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

parser=StrOutputParser()

class Feedback(BaseModel):

    sentiment: Literal['pos','neg']=Field(description='Give the sentiment of the feedback')

parser2=PydanticOutputParser(pydantic_object=Feedback)

prompt1=PromptTemplate(
    template='Classify the feedback text into any one of the two categrories positive or negative\n {feedback} \n {format_instruction}',
    input_variables=['feedback'],
    partial_variables={'format_instruction':parser2.get_format_instructions()}
)

classifier_chain=prompt1|model|parser2

# result= classifier_chain.invoke({'feedback':'This is a terrible smartphone'}).sentiment

# print(result)

prompt2=PromptTemplate(
    template='Write an appropriate to this postive feedback \n {feedback}',
    input_variables=['feedback']
)
prompt3=PromptTemplate(
    template='Write an appropriate to this negative feedback \n {feedback}',
    input_variables=['feedback']
)

branch_chain=RunnableBranch(
    (lambda x: x.sentiment =='pos',prompt2|model|parser),
    (lambda x: x.sentiment =='neg',prompt3|model|parser),
    RunnableLambda(lambda x: 'could not find sentiment')
)

chain=classifier_chain|branch_chain

result=chain.invoke({'feedback':'this phone has a really nice performance'})

print(result)

chain.get_graph().print_ascii()
