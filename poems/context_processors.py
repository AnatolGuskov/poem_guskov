
from . models import Author, Genre, Book, Poem


def author (request):
    name_tytle = "Інші Автори"
    name_text = "Усього авторів:"
    # name_library = "Бібліотека поезій Анатолія Гуськова"
    # name_poem_list = "Перелік віршів автора"
    name_genre_text = "У цьому жанрі віршів:"

    return{'author_list': Author.objects.all(),
           'name_tytle': name_tytle, 'name_text': name_text,
           'name_genre_text': name_genre_text }