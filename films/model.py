import pickle
import os


class Film:
    def __init__(self, title, director, genre, studio):
        self.title = title
        self.director = director
        self.genre = genre
        self.studio = studio

    def __str__(self):
        return f"{self.title} ({self.director})"

class FilmModel:
    def __init__(self):
        self.db_name = "db.txt"
        self.films = self.load_data()  # {}

    def add_film(self, dict_film):
        film = Film(*dict_film.values())
        self.films[film.title] = film

    def get_all_films(self):
        return self.films.values()

    def get_single_film(self, user_title):
        film = self.films[user_title]
        dict_film = {
            "название": film.title,
            "режиссер": film.director,
            "жанр": film.genre,
            "студия": film.studio
        }
        return dict_film

    def remove_film(self, user_title):
        return self.films.pop(user_title)

    def save_data(self):
        with open(self.db_name, "wb") as f:
            pickle.dump(self.films, f)

    def load_data(self):
        if os.path.exists(self.db_name):
            with open(self.db_name, "rb") as f:
                return pickle.load(f)
        else:
            return dict()