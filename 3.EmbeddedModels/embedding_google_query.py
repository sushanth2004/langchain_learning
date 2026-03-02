from langchain_google_genai import GoogleGenerativeAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

embedding = GoogleGenerativeAIEmbeddings( model="gemini-embedding-001")

result = embedding.embed_query("The capital of India is New Delhi")

print(str(result))