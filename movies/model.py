import pickle
import os.path


class Movie:
    def __init__(self, title, genre, director, year, duration, studio, cast):
        self.title = title
        self.genre = genre
        self.director = director
        self.year = year
        self.duration = duration
        self.studio = studio
        self.cast = cast

    def __str__(self):
        return f"{self.title} ({self.year})"


class MovieModel:
    def __init__(self):
        self.db_name = "db.txt"
        self.movies = self.load_data()

    def add_movie(self, dict_movie):
        movie = Movie(*dict_movie.values())
        self.movies[movie.title] = movie

    def get_all_movies(self):
        return self.movies.values()

    def get_single_movie(self, user_title):
        movie = self.movies[user_title]
        dict_movie = {
            "название": movie.title,
            "жанр": movie.genre,
            "режиссер": movie.director,
            "год выпуска": movie.year,
            "длительность": movie.duration,
            "студия": movie.studio,
            "актеры": movie.cast
        }
        return dict_movie

    def remove_movie(self, user_title):
        return self.movies.pop(user_title)

    def load_data(self):
        if os.path.exists(self.db_name):
            with open(self.db_name, 'rb') as f:
                return pickle.load(f)
        else:
            return dict()

    def save_data(self):
        with open(self.db_name, 'wb') as f:
            pickle.dump(self.movies, f)
