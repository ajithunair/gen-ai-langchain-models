from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import streamlit as st

load_dotenv()

st.title("AI Chat Assistant")

USER_AVATAR = "👤"
AI_AVATAR = "✨"

model = ChatOpenAI(model="gpt-4.1-mini")

if "chat_history" not in st.session_state:
    st.session_state.chat_history = [SystemMessage(content="You are a helpful assistant.")]

for message in st.session_state.chat_history:
    if isinstance(message, HumanMessage):
        with st.chat_message("user", avatar=USER_AVATAR):
            st.markdown(message.content)
    elif isinstance(message, AIMessage):
        with st.chat_message("assistant", avatar=AI_AVATAR):
            st.markdown(message.content)

if user_input := st.chat_input("You:"):
    with st.chat_message("user", avatar=USER_AVATAR):
        st.markdown(user_input)

    st.session_state.chat_history.append(HumanMessage(content=user_input))

    with st.chat_message("assistant", avatar=AI_AVATAR):
        with st.spinner("Thinking..."):
            response = model.invoke(st.session_state.chat_history)
            st.markdown(response.content)

    st.session_state.chat_history.append(AIMessage(content=response.content))