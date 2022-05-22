from django.urls import path
from django.urls import include
from django.views.generic import RedirectView
from django.conf import settings
from django.conf.urls.static import static
# from django.conf.urls import url

from . import views, views_archiv

app_name = 'poems'

#POEM_GUSKOV

urlpatterns = [
    # path('eng', views.index_eng, name='index_eng'),
    path('', views.index, name='index'),

    # path('authors/', views.author_list, name='authors'),
    path('authors/ukr', views.author_list_ukr, name='authors_ukr'),
    path('authors/<pk>', views.AuthorDetailView.as_view(), name='author-detail'),

    # path(r'^genres/$', views.GenreListView.as_view(), name='genres'),
    # path('genres/', views.genre_list, name='genres'),
    path('genres/ukr', views.genre_list_ukr, name='genres_ukr'),
    # path(r'^genres/(?P<pk>\d+)$', views.GenreDetailView.as_view(), name='genre-detail'),
    path('genres/<pk>', views.genre_detail, name='genre-detail'),
    path('image/', views.genre_image_list, name='genre_image'),

    path('books/ukr', views.book_list, name='books'),
    # path('book/<pk>', views.BookDetailView.as_view(), name='book-detail'),
    path('book/<pk>', views.book_detail, name='book-detail'),

    # path(r'^poems/$', views.PoemListView.as_view(), name='poem'),
    path('poems/', views.poem_list_all, name='poem_tytle'),
    path('poems/ukr', views.poem_list_ukr, name='poem_tytle_ukr'),
    path('poems/rus', views.poem_list_rus, name='poem_tytle_rus'),

    path('poems/str/', views.poem_list_string_all, name='poem_string'),
    path('poems/str/ukr', views.poem_list_string_ukr, name='poem_string_ukr'),
    path('poems/str/rus', views.poem_list_string_rus, name='poem_string_rus'),

    # path('poems/<pk>', views.PoemDetailView.as_view(), name='poem-detail'),
    path('poems/<pk>', views.poem_detail, name='poem-detail'),
    path('genre/<poem_pk>/<genre_id>', views.poem_detail_genre, name='poem-genre'),
    path('book/<poem_pk>/<book_id>', views.poem_detail_book, name='poem-book'),
    path('lang/<poem_pk>/<lang>', views.poem_detail_lang, name='poem-lang'),

    path('collage/', views.collage_list, name='poem-collage-list'),
    path('collage/<pk>', views.collage_poem, name='poem-collage'),

]
urlpatterns += [

]

urlpatterns += [

    path('', RedirectView.as_view(url='/poems/', permanent=True)), #from M-django
]

# urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) #from M-django


