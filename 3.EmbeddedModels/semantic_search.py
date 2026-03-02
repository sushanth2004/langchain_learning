from langchain_google_genai import GoogleGenerativeAIEmbeddings
from dotenv import load_dotenv
from sklearn.metrics.pairwise import cosine_similarity


load_dotenv()

documents = [
    "Virat Kohli is an Indian cricketer known for his aggresive batting and leadership.",
    "MS Dhoni is a former Indian captain famous for his calm demeanor and finishing skills.",
    "Sachin Tendulkar , also known as the 'God of Cricket', holds many batting records.",
    "Rohit Sharma is known for his elegant batting and record breaking double centuries.",
    "Jasprit Bumrah is an Indian fast bowler kown for his unorthodox action and yorkers",
    "Bhuwaneshwar Kumar, also known as 'Swing king', has many bowling records"
]

query = "who is Virat Kohli?"


embedding_model= GoogleGenerativeAIEmbeddings(model="gemini-embedding-001")

document_embeddings= embedding_model.embed_documents(documents)
query_embbeding = embedding_model.embed_query(query)

scores = cosine_similarity([query_embbeding], document_embeddings)[0]

index, score = sorted(list(enumerate(scores)), key = lambda x : x[1])[-1]

print(query)
print(documents[index])
print("similary score is : " ,str(score))