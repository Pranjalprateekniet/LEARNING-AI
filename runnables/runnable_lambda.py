import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableSequence,RunnableParallel,RunnablePassthrough,RunnableLambda

load_dotenv()

def wordcount(text):
    return len(text.split())


model = ChatGroq(model="openai/gpt-oss-20b")

prompt=PromptTemplate(
    template='Generate a joke about the {topic}',
    input_variables=['topic']
)
parser=StrOutputParser()

joke_gen_chain=RunnableSequence(prompt,model,parser)

parallel_chain=RunnableParallel({
    'joke':RunnablePassthrough(),
    'wordcount':RunnableLambda(wordcount)
    }
)

final_chain=RunnableSequence(joke_gen_chain,parallel_chain)

result=final_chain.invoke({'topic':'jarvis'})

final_result="""
{} \n word count - {}
""".format(result['joke'],result['wordcount'])

print(final_result)
