from langchain_anthropic import ChatAnthropic
from dotenv import load_dotenv

load_dotenv()

model = ChatAnthropic(model ='claude-sonnet-4-6')
response = model.invoke("What is the captal of Australia ?")

print(response.content)