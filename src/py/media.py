import webbrowser
import connect
import json
import httplib

class Movie:
    def __init__(self, movie_id, movie_title, movie_storyline, poster_image, trailer_youtube_url, genres_ids):
        self.id = movie_id
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube_url
        self.genres_ids = genres_ids,
        self.genres_names = []

    # Using https://julien.danjou.info/guide-python-static-class-abstract-methods/ explanation about abstract methods
    @staticmethod 
    def get_api_genres():
        # connect to API and get the GENRES
        data_genres = connect.Connect("GET", "/3/genre/movie/list?language=en-US&api_key=","genres")       
        return data_genres.decoded_list

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
    
    def get_trailer_url(self):
        #set the video key in youtube by API database
        video_results = connect.Connect("GET", "/3/movie/" + str(self.id) + "/videos?language=en-US&api_key=", 'results')
        for x in video_results.decoded_list:               
            self.trailer_youtube_url = "https://www.youtube.com/watch?v=" + x["key"]
            break #Ending loop before continue because we need only one URL               
        
    # return the name of IDs in the Movie DB Api
    def get_genre_names(self):
        for movie_genre_id in self.genres_ids: #  for each movie genre id, search the name of this id in the api list
            for genre_api in self.get_api_genres():
                if (genre_api['id'] == movie_genre_id): # if isthe same ID, get the name genre
                    name = str(genre_api['name'])
                    self.genres_names.append(name)