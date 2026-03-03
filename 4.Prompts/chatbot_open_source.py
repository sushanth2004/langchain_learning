from langchain_huggingface import ChatHuggingFace,HuggingFacePipeline
from langchain_core.messages import HumanMessage,SystemMessage,AIMessage


llm = HuggingFacePipeline.from_model_id(
    model_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    task="text-generation",
    pipeline_kwargs=dict(
        temperature= 0.5,
        max_new_tokens= 100
    )
)

model = ChatHuggingFace(llm = llm)


chat_history = [
    SystemMessage(content='You are a helpful AI assistant')
]


while True:
    user_input = input('user : ')
    chat_history.append(HumanMessage(content=user_input))
    if user_input=='exit' :
        break

    result = model.invoke(chat_history)
    chat_history.append(AIMessage(content=result.content))
    print("AI : ",result.content)

print(chat_history)