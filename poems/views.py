from django.shortcuts import render
#render - функция, которая генерирует HTML-файлы
# при помощи шаблонов страниц и соответствующих данных.

# Create your views here.
from django.template import loader
from django.http import HttpResponse
from django.http import Http404
from django.views import generic

from . models import Author, Genre, Book, Poem
# D:\\web\\dj\\mytestsite\\poems\\

# ================== INDEX MDN Web Docs part 5 ===========================
def index_eng(request):
    # Функция отображения для домашней страницы сайта.
    # Генерация "количеств" некоторых главных объектов

    num_genres = Genre.objects.all().count()
    num_poems  = Poem.objects.all().count()
    num_books  = Book.objects.all().count()
    num_authors = Author.objects.all().count()
    # Number of visits to this view, as counted in the session variable.
    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1

    name_tytle = "Poetry library by Anatolij Guskov"
    name_text = "The poetry library has the following record counts:"
    name_book = "Books"
    name_genre = "Genres"
    name_poem = "Poems"
    name_author = "Authors"
    # Отрисовка HTML-шаблона index.html с данными
    # внутри переменной контекста context
    return render(
        request, 'poems/index.html',
        context={'num_genres': num_genres, 'num_poems': num_poems, 'num_authors': num_authors,
                 'num_books': num_books, 'num_visits': num_visits,
                 'name_tytle': name_tytle, 'name_text': name_text,
                 'name_book': name_book, 'name_genre': name_genre,
                 'name_poem': name_poem, 'name_author': name_author},
    )

# ================== INDEX UKR MDN Web Docs part 5 ===========================
def index(request):
    # Функция отображения для домашней страницы сайта.
    # Генерация "количеств" некоторых главных объектов

    num_genres = Genre.objects.all().count()
    num_poems  = Poem.objects.all().count()
    num_books  = Book.objects.all().count()
    num_authors = Author.objects.all().count()
    # Number of visits to this view, as counted in the session variable.
    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits - 1

    name_tytle = "Бібліотека поезій Анатолія Гуськова"
    name_text = "Поетична бібліотека містить:"
    name_book = "Книг"
    name_genre = "Жанрів"
    name_poem = "Віршів"
    name_author = "Авторів"
    # Отрисовка HTML-шаблона index.html с данными
    # внутри переменной контекста context
    return render(
        request, 'poems/index.html',
        context={'num_genres': num_genres, 'num_poems': num_poems, 'num_authors': num_authors,
                 'num_books': num_books, 'num_visits': num_visits,
                 'name_tytle': name_tytle, 'name_text': name_text, 'name_author': name_author,
                 'name_book': name_book, 'name_genre': name_genre, 'name_poem': name_poem},
    )

# =============== AUTHORS Пользовательское представление ================
def author_list(request):
    author_list = Author.objects.all()

    name_tytle = "Author List"
    name_text = "There are authors:"
    name_library = "Poetry library by Anatoliy Guskov"
    name_poem_list = "Poem List of Author"

    return render(
        request,
        'poems/author_list.html',
        context={'author_list': author_list,
                 'name_tytle': name_tytle, 'name_text': name_text,
                 'name_library': name_library, 'name_poem_list': name_poem_list }
    )

# =======================================
def author_list_ukr(request):
    author_list = Author.objects.all()

    name_tytle = "Перелік Авторів"
    name_text = "Усього авторів:"
    name_library = "Бібліотека поезій Анатолія Гуськова"
    name_poem_list = "Перелік віршів автора"

    return render(
        request,
        'poems/author_list.html',
        context={'author_list': author_list,
                 'name_tytle': name_tytle, 'name_text': name_text,
                 'name_library': name_library, 'name_poem_list': name_poem_list }
    )

# ===============================
class AuthorDetailView(generic.DetailView):
    model = Author


# =============== GENRE Пользовательское представление ================
def genre_list(request):
    genre_list = Genre.objects.all()

    name_tytle = "Genre List"
    name_text = "There are genres:"
    name_poem = "poems:"
    name_library = "Poetry library by Anatoliy Guskov"

    return render(
        request,
        'poems/genre_list.html',
        context={'genre_list': genre_list,
                 'name_tytle': name_tytle, 'name_text': name_text,
                 'name_poem': name_poem, 'name_library': name_library }
    )

#  ====================================
def genre_list_ukr(request):
    genre_list = Genre.objects.all()

    name_tytle = "Перелік жанрів"
    name_text = "Усьго жанрів:"
    name_poem = "віршів:"
    name_library = "Бібліотека поезій Анатолія Гуськова"

    return render(
        request,
        'poems/genre_list.html',
        context={'genre_list': genre_list,
                 'name_tytle': name_tytle, 'name_text': name_text,
                 'name_poem': name_poem, 'name_library': name_library }
    )
#======================================
def genre_detail(request, pk):

    genre_id = Genre.objects.get(pk=pk)
    name_tytle = "Перелік жанрів"
    name_text = "Усьго жанрів:"
    name_poem = "віршів:"
    name_library = "Бібліотека поезій Анатолія Гуськова"

    return render(
        request,
        'poems/genre_detail.html',
        context={'genre': genre_id,
                 'name_tytle': name_tytle, 'name_text': name_text,
                 'name_poem': name_poem, 'name_library': name_library }
    )
#======================================

def book_list(request):
    book_list = Book.objects.all()

    name_tytle = "Book List"
    name_text = "The are books:"
    name_from = "from"
    name_poem = "poems"
    name_library = "Poetry library by Anatoliy Guskov"

    return render(
        request,
        'poems/book_list.html',
        context={'book_list': book_list,
                 'name_tytle': name_tytle, 'name_text': name_text,
                 'name_from': name_from,
                 'name_poem': name_poem, 'name_library': name_library}
    )
#======================================
def book_list_ukr(request):
    book_list = Book.objects.all()

    name_tytle = "Перелік Книг"
    name_text = "Усього книг:"
    name_from = "із"
    name_poem = "віршів"
    name_library = "Бібліотека поезій Анатолія Гуськова"

    return render(
        request,
        'poems/book_list.html',
        context={'book_list': book_list,
                 'name_tytle': name_tytle, 'name_text': name_text,
                 'name_library': name_library, 'name_from': name_from,
                 'name_poem': name_poem}
    )

# =============== POEMS LIST TYTLE ================
def poem_list(request):
    poem_list = Poem.objects.all()

    name_tytle_poem = "Перелік Віршів"
    name_text_poem = "Усьго віршів"
    name_library = "Бібліотека поезій Анатолія Гуськова"

    return render(
        request,
        'poems/poem_list.html',
        context={'poem_list' : poem_list, 'len' : len(poem_list),
                 'name_tytle_poem': name_tytle_poem, 'name_text_poem': name_text_poem,
                 'name_library': name_library,
                 }
    )
# ===============================
def poem_list_ukr(request):
    poem_list = Poem.objects.all().filter(poem_lang = 'укр.')

    name_tytle_poem = "Перелік Віршів"
    name_text_poem = "Віршів українською"
    name_library = "Бібліотека поезій Анатолія Гуськова"

    return render(
        request,
        'poems/poem_list.html',
        context={'poem_list' : poem_list, 'len' : len(poem_list),
                 'name_tytle_poem': name_tytle_poem, 'name_text_poem': name_text_poem,
                 'name_library': name_library,
                 }
    )
# ===============================
def poem_list_rus(request):
    poem_list = Poem.objects.all().filter(poem_lang = 'рос.')

    name_tytle_poem = "Перелік Віршів"
    name_text_poem = "Віршів російською"
    name_library = "Бібліотека поезій Анатолія Гуськова"

    return render(
        request,
        'poems/poem_list.html',
        context={'poem_list' : poem_list, 'len' : len(poem_list),
                 'name_tytle_poem': name_tytle_poem, 'name_text_poem': name_text_poem,
                 'name_library': name_library,
                 }
    )

# ====================================
def poem_list_string(request):
    poem_list_str = Poem.objects.order_by("headline")

    name_tytle_poem = "Перелік Віршів"
    name_text_poem = "Усьго віршів"
    name_library = "Бібліотека поезій Анатолія Гуськова"


    return render(
            request,
            'poems/poem_list_string.html',
            context={'poem_list_str': poem_list_str, 'len': len(poem_list_str),
                     'name_tytle_poem': name_tytle_poem, 'name_text_poem': name_text_poem,
                     'name_library': name_library,
                     }
        )

# ===============================================
def poem_list_string_ukr(request):
    poem_list_str = Poem.objects.order_by("headline").filter(poem_lang = 'укр.')

    name_tytle_poem = "Перелік Віршів"
    name_text_poem = " Віршів українською"
    name_library = "Бібліотека поезій Анатолія Гуськова"


    return render(
            request,
            'poems/poem_list_string.html',
            context={'poem_list_str': poem_list_str, 'len': len(poem_list_str),
                     'name_tytle_poem': name_tytle_poem, 'name_text_poem': name_text_poem,
                     'name_library': name_library,
                     }
        )

# ==================================================
def poem_list_string_rus(request):
    poem_list_str = Poem.objects.order_by("headline").filter(poem_lang = 'рос.')

    name_tytle_poem = "Перелік Віршів"
    name_text_poem = "Віршів російською"
    name_library = "Бібліотека поезій Анатолія Гуськова"


    return render(
            request,
            'poems/poem_list_string.html',
            context={'poem_list_str': poem_list_str, 'len': len(poem_list_str),
                     'name_tytle_poem': name_tytle_poem, 'name_text_poem': name_text_poem,
                     'name_library': name_library,
                     }
        )


# ===============================
def genre_poems(request):
    genre_name = Genre.objects.get(pk = id)
    poems_list = Poem.objects.all().filter(genre = genre_name)

    return render(
        request, 'poems/genre_poems.html',
        context={'poems_list' : poems_list, 'poems_num' : len(poems_list),
                 'genre_name' : genre_name,
                 }
    )

# ===============================

# =============== Обобщенные представление (архив) ================
class GenreListView(generic.ListView):
    model = Genre

# ===============================
class GenreDetailView(generic.DetailView):
    model = Genre
#======================================
class BookListView(generic.ListView):
    model = Book

# ===============================
class BookDetailView(generic.DetailView):
    model = Book
    # context_object_name = 'my_books'

# =================================
class PoemListView(generic.ListView):
    model = Poem

# ===============================
class PoemDetailView(generic.DetailView):
    model = Poem


