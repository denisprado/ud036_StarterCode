import webbrowser
import connect
import json
import httplib

class Movie:
        
    def __init__(self, movie_id, movie_title, movie_storyline, poster_image, trailer_youtube_url, genre_list):
        self.id = movie_id
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube_url
        self.genres = genre_list
        
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)

    
    def get_trailer_url(self, movie_id):

        data_videos = connect.Connect("GET", "/3/movie/" + movie_id + "/videos?language=en-US&api_key=")

        try:
            decoded = json.loads(data_videos.data)
            results = decoded['results']
            for x in results:               
                self.trailer_youtube_url = "https://www.youtube.com/watch?v=" + x["key"]
                break #Ending loop before continue because we need only on URL
                
        except (ValueError, KeyError, TypeError):
            print("Video JSON format error")
    


    # return the name of IDs in the Movie DB Api
    def get_genre_names(self, movie_genres):

        # connect to API and get the response
        data_genres = connect.Connect("GET", "/3/genre/movie/list?language=en-US&api_key=")
        
        self.genres = [] # clear the genre list of APIs

        try:
            decoded = json.loads(data_genres.data)
            genres_api = decoded['genres']
            
            for movie_genre_id in movie_genres: #  for each movie genre id, search the name of this id in the api list
                for genre_api in genres_api:
                    if (genre_api['id'] == movie_genre_id):
                        name = str(genre_api['name'])
                        self.genres.append(name)

        except (ValueError, KeyError, TypeError):
            print("Genre JSON format error")
