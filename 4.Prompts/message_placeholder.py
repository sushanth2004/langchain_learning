from langchain_core.prompts import ChatPromptTemplate,MessagesPlaceholder

#create chat_template

chat_template = ChatPromptTemplate ( [

    ('system', 'You are a helpful customer support Agent'),
    MessagesPlaceholder(variable_name='chat_history'),
    ('human' , '{query}')
])

#load chat_history
chat_history = []
with open('./4.Prompts/chat_history.txt') as f:
    chat_history.extend(f.readlines())

#create prompt

prompt = chat_template.invoke({'chat_history':chat_history, 'query':'what is status of my refund?'})

print(prompt)