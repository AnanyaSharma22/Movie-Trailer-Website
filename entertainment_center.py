import fresh_tomatoes
import media

shawshank_redemption = media.Movie("Shawshank Redemption",
                                   "Andy Dufresne, a successful banker, is arrested
                                    for the murders of his wife and her lover, and is 
                                    sentenced to life imprisonment at the Shawshank 
                                    prison.He becomes the most unconventional prisoner.",
                                   "http://t0.gstatic.com/images?q=tbn:ANd9GcSkmMH-bEDUS2TmK8amBqgIMgrfzN1_mImChPuMrunA1XjNTSKm", #noqa
                                   "https://www.youtube.com/watch?v=6hB3S9bIaco")


inception = media.Movie("Inception",
                        "Cobb steals information from his targets by 
                         entering their dreams. He is wanted for his 
                         alleged role in his wife's murder and his only 
                         chance at redemption is to perform the impossible, an inception.",
                        "http://t2.gstatic.com/images?q=tbn:ANd9GcRo9vfJCM6dzPkZHIHBVCtlJnAnew9Ai26kEdrli0-tfmatmciD", #noqa
                        "https://www.youtube.com/watch?v=8hP9D6kZseM")


predestination = media.Movie("Predestination",
                            "An agent is tasked to travel back in time to 
                             prevent a bomb attack in New York in 1975.",
                            "http://t3.gstatic.com/images?q=tbn:ANd9GcTp-yv1Vq_eoOYzyQPRghPbWKAmT3kAP-hGgI-9B8exr5R3uhbU", #noqa
                            "https://www.youtube.com/watch?v=UVOpfpYijHA")


arrival = media.Movie("Arrival",
                      "Linguistics professor Louise Banks (Amy Adams) leads
                       an elite team of investigators when gigantic spaceships 
                       touch down in 12 locations around the world.",
                      "http://t0.gstatic.com/images?q=tbn:ANd9GcSMztVicsYXcHHWNkejxIoFcW4H1eKhjSghAVixeAueuPEXmSKN", #noqa
                      "https://www.youtube.com/watch?v=tFMo3UJ4B4g")

about_time = media.Movie("About time",
                         "Like all the men in his family, Tim Lake possesses 
                          the power to travel in time. With the advice of his 
                          father, he uses his special ability to pursue his romantic interest, Mary.",
                         "http://t2.gstatic.com/images?q=tbn:ANd9GcRfwt52UbEpXfHM_tl69MNpqOQwAoVZrA2KY02pJSve0BUvyOr2", #noqa
                         "https://www.youtube.com/watch?v=7OIFdWk83no")

interstellar = media.Movie("Interstellar",
                           "In the future, Earth is slowly becoming uninhabitable. 
                            Ex-NASA pilot Cooper, along with a team of researchers, 
                            is sent on a planet exploration mission to report which planet can sustain life.",
                           "http://t1.gstatic.com/images?q=tbn:ANd9GcRf61mker2o4KH3CbVE7Zw5B1-VogMH8LfZHEaq3UdCMLxARZAB", #noqa
                           "https://www.youtube.com/watch?v=zSWdZVtXT7E")

# make movies array by assigning individual movies.
movies = [shawshank_redemption, inception, predestination,
          arrival, about_time, interstellar]

# call movie trailer page method and pass movies array to it.
fresh_tomatoes.open_movies_page(movies)

                            
