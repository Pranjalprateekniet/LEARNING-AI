from langchain_community.document_loaders import DirectoryLoader,PyPDFLoader

loader=DirectoryLoader(
    path='.',
    glob='*.pdf',
    loader_cls=PyPDFLoader
)

docs=loader.lazy_load()

# print(len(docs))

# print(docs[55].page_content)

# print(docs[55].metadata)
# print(docs[23].page_content)
# print(docs[23].metadata)

for document in docs:
    print(document.page_content)
