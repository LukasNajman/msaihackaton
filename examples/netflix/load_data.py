from dataclasses import dataclass
import csv
from typing import List


@dataclass
class NetflixMovie:
    show_id: str
    title: str
    description: str
    director: str
    genres: str
    cast: str
    production_country: str
    release_date: str
    rating: str
    duration: str
    imdb_score: str
    content_type: str
    date_added: str
    
def load_netflix_movies() -> List[NetflixMovie]:
    csv_file_path = './resources/netflixData.csv'
    netflix_movies = []

    with open(csv_file_path, 'r') as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            movie = NetflixMovie(
                show_id=row[0],
                title=row[1],
                description=row[2],
                director=row[3],
                genres=row[4],
                cast=row[5],
                production_country=row[6],
                release_date=row[7],
                rating=row[8],
                duration=row[9],
                imdb_score=row[10],
                content_type=row[11],
                date_added=row[12]
            )

            netflix_movies.append(movie)

    return netflix_movies

if __name__ == '__main__':
    netflix_movies = load_netflix_movies()
    print(f"Loaded {len(netflix_movies)} Netflix movies.")
    print(netflix_movies[0])
    print(netflix_movies[-1])