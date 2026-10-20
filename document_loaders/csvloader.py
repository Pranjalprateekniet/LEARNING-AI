from langchain_community.document_loaders import CSVLoader

loader=CSVLoader(file_path='food_nutrition_cleaned.csv')

docs=loader.load()

print(len(docs))

print(docs[51].page_content)