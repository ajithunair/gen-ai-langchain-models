from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
import streamlit as st


load_dotenv()

modelname = "gpt-4.1-mini"      
model = ChatOpenAI(model=modelname)

st.header("Ask a question to {modelname}")

language_input = st.selectbox("Select a language:", ["English", "Hindi", "Tamil", "Malayalam", "Kannada"])
wish_input = st.selectbox("Select a wish:", ["Good Morning", "Good Afternoon", "Good Evening", "Good Night"])
length_input = st.slider("Select the sentences for wishes:", 1, 2, 3)

name_input = st.text_input("Enter the name of the person:")

template = PromptTemplate(
    input_variables=["name", "language", "wish", "length"],
    template="Wish {name} {wish} in {language} in {length} different sentences."
)

prompt = template.format(name=name_input, language=language_input, wish=wish_input, length=length_input)

if st.button("Ask a question"):
    result = model.invoke(prompt)
    st.write(result.content)
