import webbrowser
import os
import re
import media


# Styles and scripting for the page
main_page_head = '''
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="utf-8">
    <title>My Favorite Movies</title>
    <script src="./index.js"></script>
</head>
'''


# The main page layout and title bar
main_page_content = '''
  <body>
    <!-- Navbar with Genres -->
    <nav class="navbar navbar-expand-lg navbar-light bg-light">
        <a class="navbar-brand" href="#">My Favorite Movies</a>
        <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarTogglerDemo01" aria-controls="navbarTogglerDemo01" aria-expanded="false" aria-label="Toggle navigation">
            <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="navbarTogglerDemo01">
            <ul class="navbar-nav mr-auto mt-2 mt-lg-0">
            <li class="nav-item active">
                <a class="nav-link All" href="#">All <span class="sr-only">(current)</span></a>
            </li>
            {menu_genres}
            </ul>
        </div>
        </nav>
    
    <!-- Trailer Video Modal -->
    <div class="modal" id="trailer">
      <div class="modal-dialog">
        <div class="modal-content">
          <a href="#" class="hanging-close" data-dismiss="modal" aria-hidden="true">
            <img src="https://lh5.ggpht.com/v4-628SilF0HtHuHdu5EzxD7WRqOrrTIDi_MhEG6_qkNtUK5Wg7KPkofp_VJoF7RS2LhxwEFCO1ICHZlc-o_=s0#w=24&h=24"/>
          </a>
          <div class="scale-media" id="trailer-video-container">
          </div>
        </div>
      </div>
    </div>

    <!-- Main Page Content -->
    <div class="container">
        <div class="movies">
            <h4 id="showing" role="alert" class="All alert alert-secondary">Showing All Movies</h4>
            {movie_tiles}
        </div>
    </div>

  </body>
</html>
'''


# A single movie entry html template
movie_tile_content = '''
<div class="movies__item movie-tile {movie_classes}" data-trailer-youtube-id="{trailer_youtube_id}" data-toggle="modal" data-target="#trailer">
    <img class="movies__item__poster" src="{poster_image_url}">
    
    <h3 class="movies__item__title">{movie_title}</h3>
    <h6 class="movies__item__button">{movie_genres}</h6>
    <p class="movies__item__storyline">{movie_storyline}</p>
    <a class="btn btn-outline-primary movies__item__button movie-tile" href="#">Show&nbsp;Trailer</a>
</div>
'''

menu_content='''
{menu_items}
'''

def create_item_menu(item):
    item = '<li class="nav-item"><a class="nav-link ' + item +'">' + item + '</a></li>'
    return str(item)

def create_menu_content(movies):
    menu = []
    menu_list = media.all_genre_names()
    
    menu = menu_content.format(
        menu_items=' '.join(map(create_item_menu, menu_list))
        )
    
    return menu


def create_movie_tiles_content(movies):
    # The HTML content for this section of the page
    content = ''
    for movie in movies:
        # Extract the youtube ID from the url
        youtube_id_match = re.search(
            r'(?<=v=)[^&#]+', movie.trailer_youtube_url)
        youtube_id_match = youtube_id_match or re.search(
            r'(?<=be/)[^&#]+', movie.trailer_youtube_url)
        trailer_youtube_id = (youtube_id_match.group(0) if youtube_id_match
                              else None)
        
        # Append the tile for the movie with its content filled in
        content += movie_tile_content.format(
            movie_title=movie.title,
            poster_image_url=movie.poster_image_url,
            trailer_youtube_id=trailer_youtube_id,
            movie_storyline=movie.storyline.encode('utf-8').strip(),
            movie_genres='<span class="badge badge-secondary">'+'</span> <span class="badge badge-secondary">'.join(map(str, movie.genres))+'</span>',
            movie_classes= ' '.join(map(str, movie.genres))
        )
    return content

def open_movies_page(movies):
    # Create or overwrite the output file
    output_file = open('my_movies.html', 'w')

    
    # Replace the movie tiles placeholder generated content
    rendered_content = main_page_content.format(
        movie_tiles=create_movie_tiles_content(movies),
        menu_genres=create_menu_content(movies)
    )

    # Output the file
    output_file.write(main_page_head + rendered_content)
    output_file.close()

    # open the output file in the browser (in a new tab, if possible)
    url = os.path.abspath(output_file.name)
    webbrowser.open('file://' + url, new=2)
