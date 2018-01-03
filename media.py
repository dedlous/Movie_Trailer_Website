import webbrowser
# Movie class to store movie information
class Movie():
    def __init__(self,title,storyline,poster_image_url,trailer_youku_url):
        '''
        init Movie class with input parameter

        title               movie title
        storyline           movie storyline
        poster_image_url    movie poster image url
        trailer_youku_url   movie traile on youku
        '''
        self.title = title
        self.storyline = storyline
        self.poster_image_url = poster_image_url
        self.trailer_url = trailer_youku_url


    def show_trailer(self):
        '''
        open webbrowser to show trailer
        '''
        webbrowser.open(self.trailer_url)


