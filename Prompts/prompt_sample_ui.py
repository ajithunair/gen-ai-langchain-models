from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import streamlit as st

load_dotenv()

model = ChatOpenAI(model="gpt-4.1-mini")

st.header("Ask a question to the AI model")
prompt = st.text_input("Enter your question:")  

if st.button("Ask a question"):
    result = model.invoke(prompt)
    st.write(result.content)