from itertools import chain
import my_movies
import media
import connect

''' connect to the API and get the data of (top rated, my favorite)
movies in json format by the Connect class'''
query = "/3/movie/top_rated?page=1&language=en-US&api_key="
data_movies = connect.Connect("GET", query, 'results')

movies = []
genre_list = []
all_genres_presents = []
img_string = "https://image.tmdb.org/t/p/w500/"
for x in data_movies.decoded_list:
    img_path = img_string + x['poster_path']
    movie = media.Movie(x['id'],
                        x['title'],
                        x['overview'],
                        img_path, " ",
                        x['genre_ids'])

    # converting genre ids in a list
    movie.genres_ids = list(movie.genres_ids)[0]

    # get the trailers by youtube key and genre names
    movie.get_trailer_url()
    movie.get_genre_names()

    # creating a list to get only used genres
    all_genres_presents.append(movie.genres_names)

    # adding actual instance to movies list
    movies.append(movie)


# return unique genre names present in the retrieved movies (using intertools)
def flatten(listOfLists):
    return set(chain.from_iterable(listOfLists))


all_genres_presents_uniques = flatten(all_genres_presents)

# call the function to creat the html page
my_movies.open_movies_page(movies, all_genres_presents_uniques)
