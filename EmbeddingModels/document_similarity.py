from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
from sklearn.metrics.pairwise import cosine_similarity

load_dotenv()

embeddings = OpenAIEmbeddings(model="text-embedding-3-large", dimensions=500)

documents = [
    "Asia is the largest continent on Earth.",
    "Africa is the second largest continent.",
    "Europe is known for its rich history and culture.",
    "North America is home to diverse landscapes and wildlife.",
    "South America is famous for the Amazon rainforest.", 
    "smallest continent on Earth is Australia, which is also a country and an island. It is located in the Southern Hemisphere and is known for its unique wildlife, beautiful beaches, and vast deserts."
]

query = "Which continent is the smallest on Earth?"

document_embeddings = embeddings.embed_documents(documents)
query_embedding = embeddings.embed_query(query)

scores = cosine_similarity([query_embedding], document_embeddings)[0]

index, score = sorted(list(enumerate(scores)), key=lambda x: x[1], reverse=True)[0]

print(query)
print(documents[index])
print(f"Similarity Score: {score:.4f}")