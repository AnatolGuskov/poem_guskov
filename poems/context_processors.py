
from . models import Author, Genre, Book, Poem


def author (request):
    name_tytle = "Інші Автори"
    name_text = "Усього авторів:"
    # name_library = "Бібліотека поезій Анатолія Гуськова"
    # name_poem_list = "Перелік віршів автора"
    name_genre_text = "У цьому жанрі віршів:"

    return{'author_list': Author.objects.all(),
           'genre_list': Genre.objects.all(),
           'book_list': Book.objects.all(),
           'name_tytle': name_tytle, 'name_text': name_text,
           'name_genre_text': name_genre_text,
           'last_poem_list': Poem.objects.all().filter(author_id = 1).order_by('-date')[:7]
           }


def last_poem (request):
    last_poem_list = Poem.object.all().order_by('-date')[:7]

    return {'last_poem_list': Poem.object.all().order_by('-date')[:7]

            }