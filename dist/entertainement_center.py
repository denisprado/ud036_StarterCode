import my_movies
import media
import connect
import json

data_movies = connect.Connect("GET", "/3/discover/movie?page=1&include_video=true&include_adult=false&language=en-US&sort_by=popularity.desc&api_key=")
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
    movie.get_genre_names(movie.genres)

    all_genres_presents.append(movie.genres)

def all(list2d):
        return(','.join(str(item) for innerlist in list2d for item in innerlist))
        print(','.join(str(item)
                       for innerlist in list2d for item in innerlist))
 # Using this solution: https://stackoverflow.com/questions/103844/how-do-i-merge-a-2d-array-in-python-into-one-string-with-list-comprehension

my_movies.open_movies_page(movies)


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
