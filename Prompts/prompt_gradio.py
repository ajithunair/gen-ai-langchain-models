from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import gradio as gr

load_dotenv()

model = ChatOpenAI(model="gpt-4.1-mini")

def ask_question(prompt):
    if not prompt:
        return ""
    result = model.invoke(prompt)
    return result.content

with gr.Blocks() as demo:
    gr.Markdown("## Ask a question to the AI model")
    prompt_input = gr.Textbox(label="Enter your question:")
    submit_btn = gr.Button("Ask a question")
    output = gr.Label(label="Response")

    submit_btn.click(fn=ask_question, inputs=prompt_input, outputs=output)

if __name__ == "__main__":
    demo.launch()