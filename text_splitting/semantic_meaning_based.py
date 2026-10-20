
import os
from dotenv import load_dotenv
from langchain_experimental.text_splitter import SemanticChunker
from langchain_openai import OpenAIEmbeddings

load_dotenv()

embeddings = OpenAIEmbeddings(
    model="nomic-embed-text-v1_5",
    api_key=os.getenv("GROQ_API_KEY"),
    base_url="https://api.groq.com/openai/v1",
)

text_splitter = SemanticChunker(
    embeddings,
    breakpoint_threshold_type="standard_deviation",
    breakpoint_threshold_amount=3,
)

sample = """
Farmers were working hard in the fields, preparing the soil and
planting seeds for the next season. The sun was bright, and the
air smelled of earth and fresh grass.

The Indian Premier League (IPL) is the biggest cricket league
in the world. People all over the world watch the matches and
cheer for their favourite teams.

Terrorism is a big danger to peace and safety. It causes harm
to people and creates fear in cities and villages. To fight
terrorism, we need strong laws, alert security forces, and
support from people who care about peace and safety.
"""

docs = text_splitter.create_documents([sample])

print("Number of chunks:", len(docs))

for i, doc in enumerate(docs, start=1):
    print(f"\n--- Chunk {i} ---")
    print(doc.page_content)
