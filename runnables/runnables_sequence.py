import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableSequence

load_dotenv()

model = ChatGoogleGenerativeAI(
    model="gemini-3.8-flash",
    google_api_key=os.getenv("GEMINI_API_KEY"),
    temperature=0,
    max_retries=3,
    timeout=120,
    max_output_tokens=512,
)

prompt = PromptTemplate(
    template="Write a short joke about {topic}. Return only the joke.",
    input_variables=["topic"],
)

prompt2 = PromptTemplate(
    template="Explain this joke briefly:\n{text}",
    input_variables=["text"],
)

parser = StrOutputParser()

chain = RunnableSequence(
    prompt,
    model,
    parser,
    prompt2,
    model,
    parser,
)

print(chain.invoke({"topic": "AI"}))