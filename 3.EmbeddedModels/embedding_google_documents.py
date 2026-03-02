from langchain_google_genai import GoogleGenerativeAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

embedding = GoogleGenerativeAIEmbeddings( model="gemini-embedding-001")

documents = [
    "Capital of India is New Delhi",
    "Capital of France is Paris",
    "Capital of Australia is Canbera"
]

result = embedding.embed_documents(documents)

print(str(result))
print(len(result[0]))