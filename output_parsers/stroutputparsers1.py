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

template1 = PromptTemplate(
    template="Write a detailed report on {topic} in about 200 characters.",
    input_variables=["topic"]
)

template2 = PromptTemplate(
    template=(
        "Summarize the following text in exactly 5 lines. "
        "Do not ask for more information.\n\nText:\n{text}"
    ),
    input_variables=["text"]
)
parser = StrOutputParser()

# First chain: Generate the report
chain1 = template1 | model | parser

print("Generating report...", flush=True)

report = chain1.invoke({"topic": "black hole"})

print("Report generated successfully.", flush=True)
print(report)

# Second chain: Summarize the report
chain2 = template2 | model | parser

print("\nGenerating summary...", flush=True)

summary = chain2.invoke({"text": report})

print("Summary generated successfully.", flush=True)
print(summary)