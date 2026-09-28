from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI(model="gpt-4.1-mini")
result = model.invoke("What is the capital of Armenia?")

print(result.content)