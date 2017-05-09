import webbrowser


class Movie():
    
    """ Movie class for representing movies """
    
    def __init__(self, movie_title, movie_storyline, 
                 poster_image, trailer_youtube):
        """ Initialises a Movie object 
        Arguments:
        movie_title = a string of the movie's title
        movie_storyline = a string of the movie's story
        poster_image = a string containing a URL to a poster image
        trailer_youtube = a string containing a youtube URL of the movie's trailer
        """
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        """ Open up trailer in a web browser """
        webbrowser.open(self.trailer_youtube_url)
