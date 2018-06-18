import webbrowser
import connect


class Movie:
    '''Movie create the movie object, giving informations about each one
        and about movies genres. The methods defined are:

        show_trailer(): open youtube trailer

        get_api_genres(): Connect to API and return all genres.

        get_genre_names(self): Return the name of a genre by Id.

        show_trailer(self): open the browser with the youtube trailer

        get_trailer_url(self): get url trailer video by API database

        get_genre_names(self): Set the variable self.genre_names

     '''

    def __init__(self, movie_id, movie_title, movie_storyline,
                 poster_image, trailer_youtube_url, genres_ids):
        self.id = movie_id
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube_url
        self.genres_ids = genres_ids,
        self.genres_names = []

    ''' Using https://julien.danjou.info/
                guide-python-static-class-abstract-methods/ explanation about
                abstract methods'''
    @staticmethod
    def get_api_genres():
        # connect to API and get the GENRES
        query_string = "/3/genre/movie/list?language=en-US&api_key="
        data_genres = connect.Connect("GET", query_string, "genres")
        return data_genres.decoded_list

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)

    def get_trailer_url(self):
        # set the video key in youtube by API database
        youtube_string = "https://www.youtube.com/watch?v="
        query_string = "/3/movie/" + \
            str(self.id) + "/videos?language=en-US&api_key="
        video_results = connect.Connect("GET", query_string, 'results')
        for x in video_results.decoded_list:
            self.trailer_youtube_url = youtube_string + x["key"]
            # Ending loop before continue because we need only one URL
            break

    # return the name of IDs in the Movie DB Api
    def get_genre_names(self):
        # for each movie genre id, search the name of this id in the api list
        for movie_genre_id in self.genres_ids:
            for genre_api in self.get_api_genres():
                # if isthe same ID, get the name genre
                if (genre_api['id'] == movie_genre_id):
                    name = str(genre_api['name'])
                    self.genres_names.append(name)
