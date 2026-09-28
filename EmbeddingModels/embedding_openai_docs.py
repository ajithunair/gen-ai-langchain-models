from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
load_dotenv()

embeddings = OpenAIEmbeddings(model="text-embedding-3-large", dimensions=100)
documents = [
    "The capital of Armenia is Yerevan.",
    "The capital of France is Paris.",
    "The capital of Germany is Berlin.",
    "The capital of Italy is Rome.",
    "The capital of Spain is Madrid.",
]
result = embeddings.embed_documents(documents)

print(result)