import webbrowser
# Movie class to store movie information
class Movie():
    def __init__(self,title,storyline,poster_image_url,trailer_youku_url):
        self.title=title
        self.storyline=storyline
        self.poster_image_url=poster_image_url
        self.trailer_url=trailer_youku_url

  # open webbrowser to show trailer
    def show_trailer(self):
        webbrowser.open(self.trailer_url)


