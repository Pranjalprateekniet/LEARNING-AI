import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableSequence,RunnableParallel

load_dotenv()

prompt1=PromptTemplate(
    template='Generate a tweet about the {topic}',
    input_variables=['topic']
)

prompt2=PromptTemplate(
    template='Generate a linkdin post about {topic}',
    input_variables=['topic']
)


model = ChatGroq(model="openai/gpt-oss-20b")

parser=StrOutputParser()

parallel_chain=RunnableParallel(
    {
        'tweet':RunnableSequence(prompt1,model,parser),
        'linkdin':RunnableSequence(prompt2,model,parser)
    }
)

result=parallel_chain.invoke({'topic':'ai'})

print(result['tweet'])
print(result['linkdin'])
