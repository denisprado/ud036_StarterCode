import my_movies
import media
import connect
import json
from itertools import chain

data_movies = connect.Connect("GET", "/3/movie/top_rated?page=1&language=en-US&api_key=")
# Using python tutorial from https://pythonspot.com/json-encoding-and-decoding-with-python/

try:
    decoded = json.loads(data_movies.data) # convert json results into Python

    # Access data and create instances of movies
    movies = [] 
    genre_list = []
    for x in decoded['results']:

        instance = media.Movie(x['id'],
                               x['title'],
                               x['overview'],
                               "https://image.tmdb.org/t/p/w500/" + x['poster_path'],
                               "",
                               x['genre_ids'])
        # adding actual instance to movies list
        movies.append(instance) #create an instance with each object result

except (ValueError, KeyError, TypeError):
    print("Movie JSON format error")

#for each movie get the trailers by youtube key and genres by genres ids list created

all_genres_presents = []

for movie in movies: 
    movie_id = str(movie.id)
    movie.get_trailer_url(movie_id)
    print(movie.genres)
    movie.get_genre_names(movie.genres)
    print(movie.title, movie.genres)
    all_genres_presents.append(movie.genres)

#return unique genre names present in the retrieved movies
def flatten(listOfLists):
    return set(chain.from_iterable(listOfLists))

all_genres_presents_uniques = flatten(all_genres_presents)


my_movies.open_movies_page(movies, all_genres_presents_uniques)

"""'vote_count',
'id',
'video',
'vote_average',
'title',
'popularity',
'poster_path',
'original_language',
'original_title',
'genre_ids',
'backdrop_path',
'adult',
'overview',
'release_date'
"""
