from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
load_dotenv()

embeddings = OpenAIEmbeddings(model="text-embedding-3-large", dimensions=500)
result = embeddings.embed_query("The capital of Armenia is Yerevan.")

print(result)