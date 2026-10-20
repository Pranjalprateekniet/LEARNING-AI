from langchain_text_splitters import RecursiveCharacterTextSplitter,Language

text="""
import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableSequence,RunnableParallel,RunnablePassthrough

load_dotenv()


model = ChatGroq(model="openai/gpt-oss-20b")


prompt1=PromptTemplate(
    template='Generate a tweet about the {topic}',
    input_variables=['topic']
)

prompt2=PromptTemplate(
    template='Generate a linkdin post about {topic}',
    input_variables=['topic']
)


parser=StrOutputParser()


joke_gen_chain=RunnableSequence(prompt1,model,parser)

parallel_chain=RunnableParallel({
    'joke':RunnablePassthrough(),
    'explanation':RunnableSequence(prompt2,model,parser)
    }
)

final_Chain=RunnableSequence(joke_gen_chain,parallel_chain)

result=final_Chain.invoke({'topic':'cricket'})

print(result)

"""

splitter=RecursiveCharacterTextSplitter.from_language(
    language=Language.PYTHON,
    chunk_size=600,
    chunk_overlap=0
)

chunks=splitter.split_text(text)
print(len(chunks))
print(chunks)