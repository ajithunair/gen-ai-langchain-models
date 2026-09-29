from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate, load_prompt
from regex import template
import streamlit as st


load_dotenv()

modelname = "gpt-4.1-mini"      
model = ChatOpenAI(model=modelname)

st.header(f"Ask a question to {modelname}")

target_role = st.selectbox(
    "Target Role:",
    [
        "Generative AI Engineer",
        "Data Scientist",
        "DevOps Engineer",
        "Full-Stack Developer",
        "Cloud Solutions Architect",
    ],
)
current_level = st.radio(
    "Current Experience Level:",
    ["Absolute Beginner", "Junior (1-2 yrs)", "Mid-Level (3-5 yrs)"],
    horizontal=True,
)

time_commitment = st.slider("Weekly Commitment (Hours):", min_value=5, max_value=40, value=15, step=5)

focus_areas = st.multiselect(
    "Key Focus Areas:",
    ["LangChain / LLM Frameworks", "System Design", "Cloud & Deployment", "RAG & Vector DBs", "Open-Source Models"],
    default=["LangChain / LLM Frameworks", "RAG & Vector DBs"],
)

preferred_tone = st.selectbox(
    "Coaching Tone:",
    ["Action-Oriented & Direct", "Academic & Theoretical", "Mentorship & Encouraging"],
)

loaded_prompt = load_prompt("Prompts/prompt_template.json")


# Format into a prompt string ready for LLM invocation
prompt_text = loaded_prompt.format(
    target_role=target_role,
    current_level=current_level,
    time_commitment=time_commitment,
    focus_areas=", ".join(focus_areas),
    preferred_tone=preferred_tone,
)
if st.button("Ask a question"):
    result = model.invoke(prompt_text)
    st.write(result.content)
