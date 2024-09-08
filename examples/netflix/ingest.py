from examples.netflix.load_data import load_netflix_movies
from examples.netflix.pg_db_client import PgDbClient, get_pg_db_client
from oai import get_embedding_client


pg_client = get_pg_db_client()

embeddinng_client = get_embedding_client()
data = load_netflix_movies()

num_of_movies = len(data)
for i, movie in enumerate(data):
    print(f"Ingesting {movie.title} ({i}/{num_of_movies})...")
    embedding = embeddinng_client.embeddings.create(
        input=movie.description,
        model="text-embedding-3-large",
        dimensions=512,
    )

    embedding = embedding.data[0].embedding

    pg_client.execute(
        "INSERT INTO netflixmovies (title, description, embedding) VALUES (%s, %s, %s)",
        (movie.title, movie.description, embedding),
    )
