import fresh_tomatoes
import media

shawshank_redemption = media.Movie("Shawshank Redemption",
                                   "Two imprisoned men, finding solace and eventual redemption through acts of common decency.",
                                   "http://t0.gstatic.com/images?q=tbn:ANd9GcSkmMH-bEDUS2TmK8amBqgIMgrfzN1_mImChPuMrunA1XjNTSKm", #noqa
                                   "https://www.youtube.com/watch?v=6hB3S9bIaco")


inception = media.Movie("Inception",
                        "A thief, who steals corporate secrets,is given the inverse task of planting an idea into the mind of a CEO.",
                        "http://t2.gstatic.com/images?q=tbn:ANd9GcRo9vfJCM6dzPkZHIHBVCtlJnAnew9Ai26kEdrli0-tfmatmciD", #noqa
                        "https://www.youtube.com/watch?v=8hP9D6kZseM")


predestination = media.Movie("Predestination",
                             "An agent is tasked to travel back in time to prevent a bomb attack in New York in 1975.",
                             "http://t3.gstatic.com/images?q=tbn:ANd9GcTp-yv1Vq_eoOYzyQPRghPbWKAmT3kAP-hGgI-9B8exr5R3uhbU", #noqa
                             "https://www.youtube.com/watch?v=UVOpfpYijHA")


arrival = media.Movie("Arrival",
                      "When linguistics professor Louise Banks was twelve mysterious spacecraft appear around the world.",
                      "http://t0.gstatic.com/images?q=tbn:ANd9GcSMztVicsYXcHHWNkejxIoFcW4H1eKhjSghAVixeAueuPEXmSKN", #noqa
                      "https://www.youtube.com/watch?v=tFMo3UJ4B4g")

about_time = media.Movie("About time",
                         "At the age of 21, Tim discovers he can travel in time and change what happens and has happened in his own life.",
                         "http://t2.gstatic.com/images?q=tbn:ANd9GcRfwt52UbEpXfHM_tl69MNpqOQwAoVZrA2KY02pJSve0BUvyOr2", #noqa
                         "https://www.youtube.com/watch?v=7OIFdWk83no")

interstellar = media.Movie("Interstellar",
                           "A team of explorers travel through a wormhole in space in an attempt to ensure humanity's survival.",
                           "http://t1.gstatic.com/images?q=tbn:ANd9GcRf61mker2o4KH3CbVE7Zw5B1-VogMH8LfZHEaq3UdCMLxARZAB", #noqa
                           "https://www.youtube.com/watch?v=zSWdZVtXT7E")

# make movies array by assigning individual movies.
movies = [shawshank_redemption, inception, predestination,
          arrival, about_time, interstellar]

# call movie trailer page method and pass movies array to it.
fresh_tomatoes.open_movies_page(movies)
