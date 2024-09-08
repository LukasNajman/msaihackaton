CREATE TABLE IF NOT EXISTS netflixmovies
(
    id              bigserial PRIMARY KEY,
    title           text,
    description     text,
    embedding       vector(512)
);
