from langchain_community.document_loaders import WebBaseLoader
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

model = ChatGroq(model="openai/gpt-oss-20b")

prompt=PromptTemplate(
    template='Answer the following question \n {question} from the following text -\n {text}',
    input_variables=['question','text']
)

parser =StrOutputParser()
url='https://www.flipkart.com/apple-macbook-air-m4-16-gb-256-gb-ssd-macos-sequoia-mc6t4hn-a/p/itm7c1831ce25509'

loader=WebBaseLoader(url)

docs=loader.load()


# print(len(docs))

# print(docs[0].page_content)

chain=prompt | model | parser

result=chain.invoke({'question':'What is the processor of this particular product ?','text':docs[0].page_content})

print(result)