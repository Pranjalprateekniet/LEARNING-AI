from langchain_community.document_loaders import PyPDFLoader

loader=PyPDFLoader('SIH2026_dead_final_draft.pdf')

docs=loader.load()

print(docs)

print(len(docs))

print(docs[3].page_content)

print(docs[5].metadata)