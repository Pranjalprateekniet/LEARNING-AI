import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableSequence,RunnableParallel,RunnablePassthrough,RunnableLambda,RunnableBranch

load_dotenv()

model = ChatGroq(model="openai/gpt-oss-20b")

prompt1=PromptTemplate(
    template='Generate a report on {topic}',
    input_variables=['topic']
)

prompt2=PromptTemplate(
    template='Summarise the following {text}',
    input_variables=['text']   
)

parser=StrOutputParser()

report_gen_chain=RunnableSequence(prompt1,model,parser)

branch_chain=RunnableBranch(
    (lambda x: len(x.split())>100,RunnableSequence(prompt2,model,parser)),
    RunnablePassthrough()
)

final_chain=RunnableSequence(report_gen_chain,branch_chain)

result=final_chain.invoke({'topic':'captain america vs iron man'})

print(result)