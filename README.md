# Movie-Trailer-Website
A simple movie trailer website project.

![image1](https://github.com/AnanyaSharma22/Movie-Trailer-Website/blob/master/images/movie1.PNG)

# Table of contents

-  Quickstart
-  Documentation
-  Installation
-  Usage

# Quickstart

After downloading the project files, a movie trailer page can be created by importing [media.py](https://github.com/AnanyaSharma22/Movie-Trailer-Website/blob/master/media.py) and [fresh_tomatoes.py](https://github.com/AnanyaSharma22/Movie-Trailer-Website/blob/master/fresh_tomatoes.py) at the start of your Python script. Then create idividual Movie objects by calling  media.Movie() and supplying it with four arguments which are  movie_title, movie_storyline, poster_image, and trailer_youtube. Lastly, to generate the movie trailers page, call fresh_tomatoes.open_movies_page() and supply it with an array of the movie objects you created. 

```
import fresh_tomatoes
import media

#information for object arguments
movie_title = "Predestination"
movie_storyline = "An agent is tasked to travel back in time to 
                   prevent a bomb attack in New York in 1975."
poster_image = "http://t3.gstatic.com/images?q=tbn:ANd9GcTp-yv1Vq_eoOYzyQPRghPbWKAmT3kAP-hGgI-9B8exr5R3uhbU"
trailer_youtube = "https://www.youtube.com/watch?v=UVOpfpYijHA"

#Create Movie object
Predestination = media.Movie(movie_title, movie_storyline, poster_image, trailer_youtube)

#Create movie trailer page with array of one movie
fresh_tomatoes.open_movies_page([Predestination])
```
A  more detailed example with multiple movie objects, can be found in [entertainment_center.py](https://github.com/AnanyaSharma22/Movie-Trailer-Website/blob/master/entertainment_center.py).


# Steps required to successfully run the application.

1 - Open **entertainment_center.py**.

2 - From the **menu**, choose **Run** and then **Run module**. If you use **windows**, just press **F5**.

3 - A file named **fresh_tomatoes.html** will be opened in your default **web browser**.

# Documentation

This is a server-side code to store a list of your own favourite movies, including box art imagery and a movie trailer URL. This code is then used to generate a static web page allowing visitors to browse their movies and watch the trailers.

# Installation
 - Install [Python](https://www.python.org/downloads/)
 
# Usage

The project demonstrates the use of a Movie object class in Python to generate a static webpage, which displays a list of favourite movies and links  each movie to its trailers video on YouTube. You will understand the role of a simple web server has in receiving a request, executing a block of code and generating a response.
