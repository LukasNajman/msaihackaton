 
from typing import List
import numpy as np
from examples.netflix.pg_db_client import get_pg_db_client
from oai import get_embedding_client


pg_client = get_pg_db_client()

embeddinng_client = get_embedding_client()

def get_similar_movies(embedding: np.ndarray, limit: int) -> List[tuple[str, str]]:
        query = """
            SELECT title, description, (embedding <=> %s) AS cosine_similarity
            FROM netflixmovies 
            ORDER BY cosine_similarity ASC LIMIT %s;
        """
        result = pg_client.execute_with_result(query, (embedding, limit))
        return [(row[0], row[1], ) for row in result]


def get_description_embedding(description: str) -> np.ndarray:
    embedding = embeddinng_client.embeddings.create(
        input=description,
        model="text-embedding-3-large",
        dimensions=512,
    )

    return np.array(embedding.data[0].embedding)


def get_similar_movies_by_description(description: str, limit: int) -> List[tuple[str, str]]:
    embedding = get_description_embedding(description)
    return get_similar_movies(embedding, limit)


if __name__ == "__main__":
    description = "A film about a group of friends who go on a road trip to find the best burger in town."
    similar_movies = get_similar_movies_by_description(description, 5)
    for movie in similar_movies:
        print(movie)