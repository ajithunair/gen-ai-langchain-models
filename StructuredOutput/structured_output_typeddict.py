from langchain_openai import ChatOpenAI
from typing import TypedDict
from dotenv import load_dotenv

load_dotenv()

class Review(TypedDict):
    Summary: str
    Sentiment: str

model = ChatOpenAI(model="gpt-4.1-mini")

prompt = """I recently upgraded to the Samsung Galaxy S24 Ultra, and I must say, it’s an absolute powerhouse! The Snapdragon 8 Gen 3 processor makes everything lightning fast—whether I’m gaming, multitasking, or editing photos. The 5000mAh battery easily lasts a full day even with heavy use, and the 45W fast charging is a lifesaver."""

structured_output = model.with_structured_output(Review)

result = structured_output.invoke(prompt)

print(result)