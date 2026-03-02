from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

model = ChatGoogleGenerativeAI(model = 'gemini-2.5-flash' , max_output_tokens=200, temperature=1.5)

response = model.invoke("give me 5 indian men names")

print(response.content)