def add_title(title):
    def wrapper(func):
        def wrap(*args, **kwargs):
            print(f" {title} ".center(50, "="))
            output = func(*args, **kwargs)
            print("=" * 50)
            return output
        return wrap
    return wrapper

class UserInterface:
    @add_title("Ввод пользовательских данных")
    def wait_user_answer(self):
        # print(" Ввод пользовательских данных ".center(50, "="))
        print("Действие с фильмами:")
        print("1 - создание записи о фильме"
              "\n2 - просмотр каталога фильмов"
              "\n3 - просмотр записи определенного фильма"
              "\n4 - удаление записи о фильме"
              "\nq - выход из программы")
        user_answer = input("Выберите вариант действия: ")
        # print("=" * 50)
        return user_answer

    @add_title("Создание записи о фильме:")
    def add_user_article(self):
        dict_film = {
            "название": None,
            "режиссер": None,
            "жанр": None,
            "студия": None
        }

        for key in dict_film:
            dict_film[key] = input(f"Введите {key} фильма:")
        # print("=" * 50)
        return dict_film

    @add_title("каталог фильмов:")
    def show_all_films(self, films):
        # print(" Список фильмов: ".center(50, "="))
        for ind, film in enumerate(films, 1):
            print(f"{ind}. {film}")
        print("=" * 50)

    @add_title("Ввод названия фильма:")
    def get_user_film(self):
        return input("Введите название фильма: ")

    @add_title("Просмотр записи о фильме:")
    def show_single_film(self, film):
        for key in film:
            print(f"{key} фильма - {film[key]}")

    @add_title("Сообщение об ошибке:")
    def show_incorrect_title_error(self, user_title):
        print(f"Фильма с названием {user_title} не существует")

    @add_title("Удаление фильма:")
    def remove_single_film(self, film):
        print(f"фильм {film} - был удален.")

    @add_title("Сообщение об ошибке:")
    def show_incorrect_answer_error(self, answer):
        print(f"Варианта {answer} не существует")