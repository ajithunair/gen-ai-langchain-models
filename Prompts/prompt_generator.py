from langchain_core.prompts import PromptTemplate

prompt_template = """
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
    template=prompt_template,
    validate_template=True
)

template.save("Prompts/prompt_template.json")