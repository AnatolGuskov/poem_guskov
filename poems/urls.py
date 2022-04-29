from django.urls import path
from django.urls import include
from django.views.generic import RedirectView
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url

from . import views

app_name = 'poems'

urlpatterns = [
    path(r'^/eng$', views.index_eng, name='index_eng'),
    path(r'', views.index, name='index'),

    path(r'^authors/$', views.author_list, name='authors'),
    path(r'^authors/ukr$', views.author_list_ukr, name='authors_ukr'),
    path(r'^authors/(?P<pk>\d+)$', views.AuthorDetailView.as_view(), name='author-detail'),

    # path(r'^genres/$', views.GenreListView.as_view(), name='genres'),
    path(r'^genres/$', views.genre_list, name='genres'),
    path(r'^genres/ukr$', views.genre_list_ukr, name='genres_ukr'),
    # path(r'^genres/(?P<pk>\d+)$', views.GenreDetailView.as_view(), name='genre-detail'),
    path(r'^genres/(?P<pk>\d+)$', views.genre_detail, name='genre-detail'),

    path(r'^books/$', views.book_list, name='books'),
    path(r'^books/ukr$', views.book_list_ukr, name='books_ukr'),
    path(r'^book/(?P<pk>\d+)$', views.BookDetailView.as_view(), name='book-detail'),

    # path(r'^poems/$', views.PoemListView.as_view(), name='poem'),
    path(r'^poems/$', views.poem_list, name='poem_tytle'),
    path(r'^poems/ukr$', views.poem_list_ukr, name='poem_tytle_ukr'),
    path(r'^poems/rus$', views.poem_list_rus, name='poem_tytle_rus'),

    path(r'^poems/str/$', views.poem_list_string, name='poem_string'),
    path(r'^poems/str/ukr$', views.poem_list_string_ukr, name='poem_string_ukr'),
    path(r'^poems/str/rus$', views.poem_list_string_rus, name='poem_string_rus'),

    path(r'poems/<pk>', views.PoemDetailView.as_view(), name='poem-detail'),

]


urlpatterns += [
    path('', RedirectView.as_view(url='/poems/', permanent=True)), #from M-django
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) #from M-django



