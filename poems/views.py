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


# ================== INDEX UKR MDN Web Docs part 5 ===========================
def index(request):
    # Функция отображения для домашней страницы сайта.
    # Генерация "количеств" некоторых главных объектов

    num_genres = Genre.objects.all().count()
    num_books  = Book.objects.all().count()
    num_poems_guskov = Poem.objects.all().filter(author = 1).count()
    num_authors = Author.objects.all().count() + 1
    num_poems_authors = Poem.objects.all().count() - num_poems_guskov

    # Number of visits to this view, as counted in the session variable.
    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits - 1

    name_tytle = "Бібліотека поезій Анатолія Гуськова"
    name_text = "Поетична бібліотека містить:"
    name_book = "Книг"
    name_genre = "Жанрів"
    name_poems_guskov = "Віршів А. Гуськова"
    name_authors = "Інших авторів"
    name_poems_authors = "Віршів інших авторів"
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

# =======================  AUTHOR LIST UKR ================
def author_list_ukr(request):
    author_list = Author.objects.all().filter(~Q(id=1))
    num_authors = Author.objects.all().filter(~Q(id=1)).count()
    num_poems = Poem.objects.all().filter(~Q(author_id=1)).count()

    name_tytle = "Інші Автори"
    name_authors = "Усього авторів:"
    name_poems = "віршів:"
    name_library = "Бібліотека поезій Анатолія Гуськова"
    name_poem_list = "Обири автора, щоб побачити його вірші"

    return render(
        request,
        'poems/author_list.html',
        context={'author_list': author_list, 'num_authors': num_authors,
                 'name_tytle': name_tytle, 'name_authors': name_authors,
                 'name_poems': name_poems, 'num_poems': num_poems,
                 'name_library': name_library, 'name_poem_list': name_poem_list }
    )

# ===============================
class AuthorDetailView(generic.DetailView):
    model = Author

# =============== GENRE Пользовательское представление ================

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
    color1 = genre_id.genre_text_color[0]
    color2 = genre_id.genre_text_color[1]
    color3 = genre_id.genre_text_color[2]
    color4 = genre_id.genre_text_color[3]

    return render(
        request,
        'poems/genre_detail.html',
        context={'genre': genre_id,
                 'name_tytle': name_tytle, 'name_text': name_text,
                 'name_poem': name_poem, 'name_library': name_library,
                 'color1': color1, 'color2': color2, 'color3': color3, 'color4': color4,
                 }
    )

#==================== genre_image_lst ===========
def genre_image_list(request):
    genre_image_list = Genre.objects.all().order_by('image_name')

    return render(
        request,
        'poems/genre_image_list.html',
        context={'genre_image_list': genre_image_list,

                  }
    )

#================= BOOK =====================
#=============== book_list_ukr
def book_list_ukr(request):
    book_list = Book.objects.all().order_by("-public_date")

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

# ============================= POEMS LIST TITLE ================
def poem_list_all(request):
    poem_list = Poem.objects.all().filter(author_id = 1)
    poem_list_authors = Poem.objects.all().filter(~Q(author_id = 1))

    name_tytle_poem = "Перелік Віршів"
    name_num = "Усього віршів"
    name_num_poems = "Вірші А. Гуськова"
    name_library = "Бібліотека поезій Анатолія Гуськова"
    name_num_poems_authors = "Вірші інших авторів"

    return render(
        request,
        'poems/poem_list.html',
        context={'poem_list_guskov': poem_list, 'poem_list_authors': poem_list_authors,
                 'num_guskov': len(poem_list), 'num_authors': len(poem_list_authors),
                 'num': len(poem_list) + len(poem_list_authors),
                 'name_tytle_poem': name_tytle_poem, 'name_num_poems': name_num_poems,
                 'name_num_poems_authors': name_num_poems_authors,
                 'name_library': name_library, 'name_num': name_num,
                 }
    )
# =============================== poem_list_ukr
def poem_list_ukr(request):
    poem_list = Poem.objects.all().filter(author_id=1, poem_lang = 'укр.')
    poem_list_authors = Poem.objects.all().filter(~Q(author_id=1),poem_lang = 'укр.')

    name_tytle_poem = "Вірші українською"
    name_library = "Бібліотека поезій Анатолія Гуськова"
    name_num = "Усього віршів"
    name_num_poems = "Вірші А. Гуськова"
    name_num_poems_authors = "Вірші інших авторів"

    return render(
        request,
        'poems/poem_list.html',
        context={'poem_list_guskov': poem_list, 'poem_list_authors': poem_list_authors,
                 'num_guskov': len(poem_list), 'num_authors': len(poem_list_authors),
                 'num': len(poem_list) + len(poem_list_authors),
                 'name_tytle_poem': name_tytle_poem, 'name_num_poems': name_num_poems,
                 'name_num_poems_authors': name_num_poems_authors,
                 'name_library': name_library, 'name_num': name_num,
                 }
    )
# =============================== poem_list_rus
def poem_list_rus(request):
    poem_list = Poem.objects.all().filter(author_id=1, poem_lang='рос.')
    poem_list_authors = Poem.objects.all().filter(~Q(author_id=1), poem_lang='рос.')

    name_tytle_poem = "Вірші російською"
    name_library = "Бібліотека поезій Анатолія Гуськова"
    name_num = "Усього віршів"
    name_num_poems = "Вірші А. Гуськова"
    name_num_poems_authors = "Вірші інших авторів"

    return render(
        request,
        'poems/poem_list.html',
        context={'poem_list_guskov': poem_list, 'poem_list_authors': poem_list_authors,
                 'num_guskov': len(poem_list), 'num_authors': len(poem_list_authors),
                 'num': len(poem_list) + len(poem_list_authors),
                 'name_tytle_poem': name_tytle_poem, 'name_num_poems': name_num_poems,
                 'name_num_poems_authors': name_num_poems_authors,
                 'name_library': name_library, 'name_num': name_num,
                 }
    )
# ============================== POEMS LIST STRING =====+++++==========
def poem_list_string_all(request):
    poem_list = Poem.objects.all().filter(author_id=1).order_by("headline")
    poem_list_authors = Poem.objects.all().filter(~Q(author_id=1)).order_by("headline")

    name_tytle_poem = "Перелік Віршів"
    name_num = "Усього віршів"
    name_num_poems = "Вірші А. Гуськова"
    name_library = "Бібліотека поезій Анатолія Гуськова"
    name_num_poems_authors = "Вірші інших авторів"

    return render(
        request,
        'poems/poem_list_string.html',
        context={'poem_list_guskov': poem_list, 'poem_list_authors': poem_list_authors,
                 'num_guskov': len(poem_list), 'num_authors': len(poem_list_authors),
                 'num': len(poem_list) + len(poem_list_authors),
                 'name_tytle_poem': name_tytle_poem, 'name_num_poems': name_num_poems,
                 'name_num_poems_authors': name_num_poems_authors,
                 'name_library': name_library, 'name_num': name_num,
                 }
    )
# ================================ poem_list_string_ukr ===============
def poem_list_string_ukr(request):
    poem_list = Poem.objects.all().filter(author_id=1, poem_lang = 'укр.').order_by("headline")
    poem_list_authors = Poem.objects.all().filter(~Q(author_id=1), poem_lang = 'укр.').order_by("headline")

    name_tytle_poem = "Вірші українською"
    name_num = "Усього віршів"
    name_num_poems = "Вірші А. Гуськова"
    name_library = "Бібліотека поезій Анатолія Гуськова"
    name_num_poems_authors = "Вірші інших авторів"

    return render(
        request,
        'poems/poem_list_string.html',
        context={'poem_list_guskov': poem_list, 'poem_list_authors': poem_list_authors,
                 'num_guskov': len(poem_list), 'num_authors': len(poem_list_authors),
                 'num': len(poem_list) + len(poem_list_authors),
                 'name_tytle_poem': name_tytle_poem, 'name_num_poems': name_num_poems,
                 'name_num_poems_authors': name_num_poems_authors,
                 'name_library': name_library, 'name_num': name_num,
                 }
    )
# ================================ poem_list_string_rus ==================
def poem_list_string_rus(request):
    poem_list = Poem.objects.all().filter(author_id=1, poem_lang='рос.').order_by("headline")
    poem_list_authors = Poem.objects.all().filter(~Q(author_id=1), poem_lang='рос.').order_by("headline")

    name_tytle_poem = "Вірші російською"
    name_num = "Усього віршів"
    name_num_poems = "Вірші А. Гуськова"
    name_library = "Бібліотека поезій Анатолія Гуськова"
    name_num_poems_authors = "Вірші інших авторів"

    return render(
        request,
        'poems/poem_list_string.html',
        context={'poem_list_guskov': poem_list, 'poem_list_authors': poem_list_authors,
                 'num_guskov': len(poem_list), 'num_authors': len(poem_list_authors),
                 'num': len(poem_list) + len(poem_list_authors),
                 'name_tytle_poem': name_tytle_poem, 'name_num_poems': name_num_poems,
                 'name_num_poems_authors': name_num_poems_authors,
                 'name_library': name_library, 'name_num': name_num,
                 }
    )




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


