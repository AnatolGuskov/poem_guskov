from django.shortcuts import render
#render - функция, которая генерирует HTML-файлы
# при помощи шаблонов страниц и соответствующих данных.

# Create your views here.
from django.template import loader
from django.http import HttpResponse
from django.http import Http404
from django.views import generic
from django.db.models import Q

from . models import Author, Genre, Book, Poem
# D:\\web\\dj\\mytestsite\\poems\\

# ================== INDEX MDN Web Docs part 5 ===========================
def index_eng(request):
    # Функция отображения для домашней страницы сайта.
    # Генерация "количеств" некоторых главных объектов

    num_genres = Genre.objects.all().count()
    num_books = Book.objects.all().count()
    num_poems_guskov = Poem.objects.all().filter(author=1).count()
    num_authors = Author.objects.all().count() - 1
    num_poems_authors = Poem.objects.all().count() - num_poems_guskov

    # Number of visits to this view, as counted in the session variable.
    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1

    name_tytle = "Poetry library by Anatolij Guskov"
    name_text = "The poetry library has the following record counts:"
    name_book = "Books"
    name_genre = "Genres"
    name_poems_guskov = "Poems by A. Guskov"
    name_authors = "Another Authors"
    name_poems_authors = "Poems by Another Authors"
    # Отрисовка HTML-шаблона index.html с данными
    # внутри переменной контекста context
    return render(
        request, 'poems/index.html',
        context={'num_genres': num_genres,
                 'num_poems_guskov': num_poems_guskov,
                 'num_poems_authors': num_poems_authors, 'num_authors': num_authors,
                 'num_books': num_books, 'num_visits': num_visits,
                 'name_tytle': name_tytle, 'name_text': name_text, 'name_authors': name_authors,
                 'name_book': name_book, 'name_genre': name_genre,
                 'name_poems_guskov': name_poems_guskov, 'name_poems_authors': name_poems_authors}
    )

# =============== AUTHORS Пользовательское представление ================
def author_list(request):
    author_list = Author.objects.all().filter(~Q(id=1))
    num_authors = Author.objects.all().filter(~Q(id=1)).count()
    num_poems = Poem.objects.all().filter(~Q(author_id=1)).count()

    name_tytle = "Another Author"
    name_authors = "There are authors:"
    name_poems = "poems:"
    name_library = "Poetry library by Anatoliy Guskov"
    name_poem_list = "Choose an author to see his poems"

    return render(
        request,
        'poems/author_list.html',
        context={'author_list': author_list, 'num_authors': num_authors,
                 'name_tytle': name_tytle, 'name_authors': name_authors,
                 'name_poems': name_poems, 'num_poems': num_poems,
                 'name_library': name_library, 'name_poem_list': name_poem_list}
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
                 'name_poem': name_poem, 'name_library': name_library,
                 }
    )

#================= BOOK =====================

def book_list(request):
    book_list = Book.objects.all().order_by("-public_date")

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

# # ===============================
# def genre_poems(request):
#     genre_name = Genre.objects.get(pk = id)
#     poems_list = Poem.objects.all().filter(genre = genre_name)
#
#     return render(
#         request, 'poems/genre_poems.html',
#         context={'poems_list' : poems_list, 'poems_num' : len(poems_list),
#                  'genre_name' : genre_name,
#                  }
#     )

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


