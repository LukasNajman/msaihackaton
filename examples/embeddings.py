from pprint import pp
from oai import get_embedding_client


embeddings_client = get_embedding_client()

text = "Hello, world!"

result = embeddings_client.embeddings.create(
    input=text,
    model="text-embedding-3-large",
    dimensions=512,
)
embedding = result.data[0].embedding
usage = result.usage

print(f"Embedding length: {len(embedding)}")
pp(usage)
