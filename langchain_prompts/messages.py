from langchain_core.messages import SystemMessage,HumanMessage,AIMessage
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="openai/gpt-oss-20b",
    task="text-generation"
)

model=ChatHuggingFace(llm=llm)


message=[
    SystemMessage(content="You are helpful assistant"),
    HumanMessage(content="Tell me about langchain")
]

result=model.invoke(message)
message.append(AIMessage(content=result.content))
print(message)
