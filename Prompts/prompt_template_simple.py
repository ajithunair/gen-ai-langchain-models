from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate


load_dotenv()

modelname = "gpt-4.1-mini"      
model = ChatOpenAI(model=modelname)


template = PromptTemplate(
    input_variables=["name"],
    template="Wish {name} good morning in 5 different indian languages."
)

prompt = template.format(name="Ajith")
result = model.invoke(prompt)
print(result)