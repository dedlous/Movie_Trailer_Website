import media
import fresh_tomatoes

def init_my_favourite_movie():
    '''
    #init my favourite movie list
    #output: a movie list
    '''
    my_favourite_movie_list = []
    avenger3 = media.Movie("avenger3",
                        ''''Four years after the events of Guardians of the Galaxy Vol.
2,[1] the Avengers have been torn apart following the events of Captain America: Civil War.
When Thanos arrives on Earth to collect the Infinity Stones for a gauntlet that will allow him to bend reality to his will,
the Avengers must join forces with the Guardians of the Galaxy to stop him''',
                        "https://img3.doubanio.com/view/photo/l/public/p2506296392.webp",
                        "http://v.youku.com/v_show/id_XMjgwNzY5OTEyOA==.html?spm=a2h1n.8261147.0.0")

    wonder_woman = media.Movie("Wonder Woman",
                              " an Amazonian warrior in training, leaves home to fight a war, discovering her full powers and true destiny",
                              "https://img1.doubanio.com/view/photo/l/public/p2460196938.webp",
                              "http://v.youku.com/v_show/id_XMTgwNTAwOTI2MA==.html?spm=a2h0j.8191423.chasing.1~3!29~A")

    iron_man_3 = media.Movie(" Iron Man 3",
                           "When Tony Stark's world is torn apart by a formidable terrorist called the Mandarin, he starts an odyssey of rebuilding and retribution",
                           "https://img3.doubanio.com/view/photo/l/public/p1955027305.webp",
                           "http://v.youku.com/v_show/id_XNTMyMDk2OTU2.html?spm=a2h1n.8261147.around_2.5~5~5~5~A")

    my_favourite_movie_list = [avenger3,wonder_woman,iron_man_3]

    return my_favourite_movie_list


#init my favourite movie list
init_my_favourite_movie()

#create a html to show movies
fresh_tomatoes.open_movies_page(init_my_favourite_movie())

