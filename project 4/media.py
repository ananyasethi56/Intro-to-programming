import fresh_tomatoes
import media
# we have to define media and fresh_tomatoes that we have installed

avatar = media.Movie("Avatar","A blue man",
                         "https://www.movieposter.com/posters/archive/main/98/MPW-49246",
                         "https://www.youtube.com/watch?v=cRdxXPV9GNQ")
twostates = media.Movie("2 states","A  true love story by not focusing on their religion",
                      "http://www.filmapia.com/sites/default/files/filmapia/pub/movie/posters/1401170120_12fe3cbe_2-states-poster-612x884.jpg",
                      "https://www.youtube.com/watch?v=CGyAaR2aWcA")
threeidiots = media.Movie("3 idiots","A motivational movie",
                        "http://www.indicine.com/movies/img/2009/10/threeidiots2.jpg",
                        "https://www.youtube.com/watch?v=K0eDlFX9GMc")
rustom = media.Movie("Rustom","a story based on lovestory of india navy",
                   "https://www.google.co.in/search?q=movie+poster&biw=1366&bih=589&source=lnms&tbm=isch&sa=X&ved=0ahUKEwj2mb-Gj9HPAhXBvI8KHd_ACVwQ_AUIBigB#tbm=isch&q=rustom+poster+link&imgrc=aRvqVrXuwxT0tM%3A",
                   "https://www.youtube.com/watch?v=L83qMnbJ198")
gabbar = media.Movie("Gabbar","An emotional love storyof gabbar",
                   "https://www.google.co.in/search?q=movie+poster&biw=1366&bih=589&source=lnms&tbm=isch&sa=X&ved=0ahUKEwj2mb-Gj9HPAhXBvI8KHd_ACVwQ_AUIBigB#tbm=isch&q=gabbar+poster&imgrc=eVfDlwgw0ilh2M%3A",
                   "https://www.youtube.com/watch?v=T95zFC4Z2pY")
airlift = media.Movie("Airlift","A story based on army officer",
                    "https://www.google.co.in/search?q=movie+poster&biw=1366&bih=589&source=lnms&tbm=isch&sa=X&ved=0ahUKEwj2mb-Gj9HPAhXBvI8KHd_ACVwQ_AUIBigB#tbm=isch&q=airlift+poster&imgrc=2CFF3sKdD7VR1M%3A",
                    "https://www.youtube.com/watch?v=vb5xCMbMfZ0")
movies = [avatar, twostates, threeidiots, rustom, gabbar, airlift]#movies is a array created where we have provided all the movies
fresh_tomatoes.open_movies_page(movies)
