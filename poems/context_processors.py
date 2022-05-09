
from . models import Author, Genre, Book, Poem
from django.db.models import Q


def author (request):
    num_authors = Author.objects.all().filter(~Q(id=1)).count()
    num_poems = Poem.objects.all().filter(~Q(author_id=1)).count()

    name_authors = "Усього авторів:"
    name_poems = "віршів:"

    return{'author_list': Author.objects.all(),
           'num_authors': Author.objects.all().filter(~Q(id=1)).count(),
           'num_poems': Poem.objects.all().filter(~Q(author_id=1)).count(),
           'name_library': "Бібліотека поезій Анатолія Гуськова",
           'name_tytle': "Автори Поезії війни",
           'name_authors': "Усього авторів:",
           'name_poems': "віршів:"

           }

def lists (request):

    return{'genre_list': Genre.objects.all(),
           'book_list': Book.objects.all(),
           'last_poem_list': Poem.objects.all().filter(author_id = 1).order_by('-date')[:7]
           }



