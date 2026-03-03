from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import streamlit as st
from langchain_core.prompts import PromptTemplate,load_prompt

load_dotenv()

model = ChatGoogleGenerativeAI(model = 'gemini-2.5-flash')

st.header("Research Tool")

paper_input = st.selectbox("Select the Research Paper Name", [
    "Attention Is All You Need",
    "Bert : pre-training of Deep Bidirectional Transformers",
    "GPT-3 : language models are few shot learners",
    "Diffusions models Beat GANs on Image synthesis"
])

style_input = st.selectbox("Select Explanation Style", [
    "Beginner friendly",
    "Technical ",
    "Code Oriented",
    "Mathematical"
])

length_input = st.selectbox("Select Explanation length", [
    "Short(1-2 paragraphs)",
    "medium (3-5 paragraphs)",
    "Long (detailed explanation)"
])

template = load_prompt('./4.Prompts/template.json')


button = st.button("Summarize")
 
if button :
    chain = template | model
    result =chain.invoke({
       'paper_input':paper_input,
       'style_input':style_input,
       'length_input':length_input
    })
    st.write(result.content)

