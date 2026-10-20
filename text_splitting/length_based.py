from langchain_text_splitters import CharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader

loader=PyPDFLoader('SIH2026_dead_final_draft.pdf')

docs=loader.load()



text="""
The UnstructuredLoader does not support mode as parameter for grouping text like the older loader UnstructuredFileLoader and others did. It instead supports “chunking”. Chunking in unstructured differs from other chunking mechanisms you may be familiar with that form chunks based on plain-text features—character sequences like “\n\n” or “\n” that might indicate a paragraph boundary or list-item boundary. Instead, all documents are split using specific knowledge about each document format to partition the document into semantic units (document elements) and we only need to resort to text-splitting when a single element exceeds the desired maximum chunk size. In general, chunking combines consecutive elements to form chunks as large as possible without exceeding the maximum chunk size. Chunking produces a sequence of CompositeElement, Table, or TableChunk elements. Each “chunk” is an instance of one of these three types.
See this page for more details about chunking options, but to reproduce the same behavior as mode="single", you can set chunking_strategy="basic", max_characters=<some-really-big-number>, and include_orig_elements=False.
"""

spliiter=CharacterTextSplitter(
    chunk_size=130,
    chunk_overlap=0,
    separator=''
)

result=spliiter.split_documents(docs)

print (result[0].page_content)