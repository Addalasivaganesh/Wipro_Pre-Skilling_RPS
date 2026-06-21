from langchain_community.document_loaders import TextLoader
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS



#Load Data
loader = TextLoader("data.txt")
documents = loader.load()

#Convert to Embeddings
embeddings = HuggingFaceEmbeddings()

db = FAISS.from_documents(documents,embeddings)

# Create Retriever
retriever = db.as_retriever()

query = "What is machine learning?"
result = retriever.invoke(query)
print("query:", query)
print("\nAnswer:")
for doc in result:
    print(doc.page_content)