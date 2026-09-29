from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
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

career_roadmap_template = """
You are an expert career architect and technical mentor. Design a realistic, step-by-step career transition plan based on the user's background and constraints.

### Candidate Profile:
- **Target Role:** {target_role}
- **Current Experience Level:** {current_level}
- **Available Time:** {time_commitment} hours/week
- **Priority Focus Areas:** {focus_areas}
- **Tone/Style:** {preferred_tone}

---

### Instructions & Output Structure:
Please format your response strictly using the following sections:

1. **Prerequisite Assessment:**
   - Briefly outline 2-3 core skills the candidate likely already knows vs. what critical skills are missing for a {current_level} targeting {target_role}.

2. **Phase-by-Phase Roadmap (4-Week Sprints):**
   - Present a Markdown table with the columns: `Phase`, `Sprint Goal`, `Key Concepts / Tools`, and `Deliverable / Mini-Project`.
   - Tailor the depth strictly to a commitment of {time_commitment} hours/week.
   - Emphasize: {focus_areas}.

3. **Capstone Project Proposal:**
   - Define a single end-to-end portfolio project suitable for resume showcase. Include architecture components (e.g., API, database/framework, deployment).

4. **Common Pitfalls to Avoid:**
   - 2-3 specific mistakes learners make when transitioning into {target_role}.

Ensure the output adheres to a {preferred_tone} voice throughout.
"""

template = PromptTemplate(
    input_variables=[
        "target_role",
        "current_level",
        "time_commitment",
        "focus_areas",
        "preferred_tone",
    ],
    template=career_roadmap_template,
)

# Format into a prompt string ready for LLM invocation
prompt_text = template.format(
    target_role=target_role,
    current_level=current_level,
    time_commitment=time_commitment,
    focus_areas=", ".join(focus_areas),
    preferred_tone=preferred_tone,
)
if st.button("Ask a question"):
    result = model.invoke(prompt_text)
    st.markdown(result.content)
