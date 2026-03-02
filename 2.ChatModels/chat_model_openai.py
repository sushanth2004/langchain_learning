from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI(model='gpt-4',temperature=0.3,max_completion_tokens=20)

"""
temperature : range is 0 to 2
              lower range --> deterministic/predictable response
              higher range --> creative / random response
max_completion_tokens : can limit the token usage (can consider tokens==words)
"""


response = model.invoke("write a poem on cricket")

print(response)
print(response.content)