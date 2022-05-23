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


# ================================ poem_context ==================
poem_context_art = "1"
poem_context_name = "2"
poem_context_list = []


# ================== INDEX UKR MDN Web Docs part 5 ===========================
def index(request):
    # Функция отображения для домашней страницы сайта.
    # Генерация "количеств" некоторых главных объектов

    num_genres = Genre.objects.all().count()
    num_books  = Book.objects.all().count()
    num_poems_guskov = Poem.objects.all().filter(author = 1).count()
    num_authors = Author.objects.all().count() + 1
    num_poems_authors = Poem.objects.all().count() - num_poems_guskov
    num_collage = Poem.objects.filter(image_poem__contains = "collage").count()

    # Number of visits to this view, as counted in the session variable.
    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1

    name_tytle = "Бібліотека поезій Анатолія Гуськова"
    name_text = "Поетична бібліотека містить:"
    name_book = "Книг"
    name_genre = "Жанрів"
    name_poems_guskov = "Віршів А. Гуськова"
    name_authors = "Інших авторів"
    name_poems_authors = "Віршів інших авторів"
    name_collage = "Віршів з колажами"

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
                 'name_poems_guskov': name_poems_guskov, 'name_poems_authors': name_poems_authors,
                 'name_collage': name_collage, 'num_collage': num_collage,
                }
    )

# =======================  AUTHOR LIST UKR ================
def author_list_ukr(request):
    author_list = Author.objects.all().filter(~Q(id=1))
    num_authors = Author.objects.all().filter(~Q(id=1)).count()
    num_poems = Poem.objects.all().filter(~Q(author_id=1)).count()

    name_tytle = "Автори Поезії війни"
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
    name_genre_text = "У цьому жанрі віршів:"
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
                 'name_tytle': name_tytle, 'name_genre_text': name_genre_text,
                 'name_poem': name_poem, 'name_library': name_library,
                 'color1': color1, 'color2': color2, 'color3': color3, 'color4': color4,
                 }
    )

#==================== genre_image_lst ===========
def genre_image_list(request):

    genre_image_list = Genre.objects.all().order_by('image_name')

    image_list = \
        [{"image_genre": "images/authors_from Bakla.png", "image_name": "гора Чатир-Даг"},
         {"image_genre": "images/poems_from_Tepe.png", "image_name": "гори з Тепе-Кермену"},
         {"image_genre": "images/genre_from_Chufut.png", "image_name": "плато Бурунчак"},
         {"image_genre": "images/books_from Bakla.png", "image_name": "ранок на Баклі"},
         {"image_genre": "images/index_from_Bakla.png", "image_name": "долини навколо Бакли"},
         {"image_genre": "images/collage_from_Kacha.png", "image_name": "долина Качі, скала Фицкі"},
         ]
    for i in range (len(genre_image_list)):
        image_list.append({"image_genre": genre_image_list[i].image_genre,
                           "image_name": genre_image_list[i].image_name})

    # image_list.sort("image_name")
    num_image = len(image_list)

    return render(
        request,
        'poems/genre_image_list.html',
        context={'image_list': image_list,
                 'num_image': num_image,

                  }
    )

#================= BOOK Пользовательское представление =================
#=============== book_list_ukr =======================
def book_list(request):
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

#=============== book_detail_ukr =======================
def book_detail (request, pk):
    book = Book.objects.get(pk=pk)

    return render(
        request,
        'poems/book_detail.html',
        context={'book': book,

                 }
    )

# ================ POEMS LIST TITLE =====================================
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

# ================================ poem_collage ==================
def collage_poem (request, pk):
    collage_list = Poem.objects.filter(image_poem__contains = "collage")

    collage = Poem.objects.get(pk=pk)
    pos_image = collage.image_poem[18]

    return render(
        request,
        'poems/poem_collage.html',
        context={'collage': collage,
                 'pos_image': pos_image,
                 'collage_list': collage_list,

                 }
    )

# ================================ collage_list ==================
def collage_list (request):
    collage_list = Poem.objects.filter(image_poem__contains = "collage")

    name_tytle_collage = "Колажі віршів"
    name_library = "Бібліотека поезій Анатолія Гуськова"
    name_num = "Усього колажів"

    return render(
        request,
        'poems/collage_list.html',
        context={'collage_list': collage_list,
                 'name_tytle_collage': name_tytle_collage,
                 'name_library': name_library, 'name_num': name_num,
                 }
    )

# ================================= poem_detail ==================
def poem_detail (request, pk):
    poem = Poem.objects.get(pk=pk)

    return render(
        request,
        'poems/poem_detail.html',
        context={'poem': poem,

                 }
    )

# ================================= poem_detail_book Вірші по книзі ==================
def poem_detail_book (request, poem_pk, book_id):
    poem = Poem.objects.get(pk=poem_pk)
    poem_list = Poem.objects.all().filter(book = book_id)
    book = Book.objects.get(id = book_id)

    return render(
        request,
        'poems/poem_detail.html',
        context={'poem': poem,
                 'poem_list': poem_list,
                 'list_art': "вірші із книги",
                 # 'list_name': book.title,
                 'art_image': book.image_book,
                 'art_id': book_id,
                 'art': "book",
                 }
    )

# ================================= poem_detail_genre Вірші по жанру ==================
def poem_detail_genre (request, poem_pk, genre_id):
    poem = Poem.objects.get(pk= poem_pk)
    poem_list = Poem.objects.all().filter(genre = genre_id)
    genre = Genre.objects.get(id = genre_id)

    return render(
        request,
        'poems/poem_detail.html',
        context={'poem': poem,
                 'poem_list': poem_list,
                 'list_art': "вірші із жанру",
                 'list_name': genre.name,
                 'art_image': genre.image_genre,
                 'art_id': genre_id,
                 'art': "genre",
                 }
    )

# ================================= poem_detail_lang Вірші по мові ==================
def poem_detail_lang (request, poem_pk, lang):
    poem = Poem.objects.get(pk= poem_pk)
    poem_list = Poem.objects.all().filter(poem_lang = lang)
    if lang == 'укр.':
        list_name = 'вірші українською'
    else:
        list_name = 'вірші російською'

    return render(
        request,
        'poems/poem_detail.html',
        context={'poem': poem,
                 'poem_list': poem_list,
                 'list_name': list_name,
                 'art_image': 'images/poems_from_Tepe.png',
                 'art_id': lang,
                 'art': "lang"
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


