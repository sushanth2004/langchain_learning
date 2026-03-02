from langchain_huggingface import HuggingFaceEmbeddings

embedding = HuggingFaceEmbeddings(model_name = "sentence-transformers/all-MiniLM-L6-v2")

documents = [
    "Capital of India is New Delhi",
    "Capital of France is Paris",
    "Capital of Australia is Canbera"
]

text = "Capital of India is New Delhi"

vector = embedding.embed_documents(documents)

print(str(vector))
print(len(vector[0]))