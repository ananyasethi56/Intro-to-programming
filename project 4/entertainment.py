import webbrowser

class Movie():# this is a class where we are calling movie function
    def __init__(self,movie_title,movie_storyline,poster_image,youtube_trailer):#this function is inbuilt where we are we are passing an arguments of movie storyline,movie poster,movie trailer
        self.title=movie_title
        self.storyline=movie_storyline
        self.poster_image=poster_image
        self.trailer_youtube_url=youtube_trailer


    def show_trailer(self):#this function will pass an argument self from which trailer of movie will start
        webbrowser.open(self.trailer_youtube_url)
