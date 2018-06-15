import my_movies
import media
import connect
import json
from itertools import chain

# connect to the API and get the data of (top rated, my favorite) movies in json format by the Connect class
data_movies = connect.Connect("GET", "/3/movie/top_rated?page=1&language=en-US&api_key=", 'results')

movies = [] 
genre_list = []
all_genres_presents = []

for x in data_movies.decoded_list:

    movie = media.Movie(x['id'],
                            x['title'],
                            x['overview'],
                            "https://image.tmdb.org/t/p/w500/" + x['poster_path'],
                            "",
                            x['genre_ids'])
    
    #converting genre ids in a list 
    movie.genres_ids = list(movie.genres_ids)[0] 
    
    #get the trailers by youtube key and genre names
    movie.get_trailer_url()   
    movie.get_genre_names()

    # creating a list to get only used genres
    all_genres_presents.append(movie.genres_names)
    
    # adding actual instance to movies list
    movies.append(movie) #create an instance with each object result
  
#return unique genre names present in the retrieved movies (using intertools package)
def flatten(listOfLists):
    return set(chain.from_iterable(listOfLists))
all_genres_presents_uniques = flatten(all_genres_presents)

# call the function to creat the html page
my_movies.open_movies_page(movies, all_genres_presents_uniques)