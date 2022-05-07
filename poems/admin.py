
from django.contrib import admin

from .models import Language, Author, Genre, Poem, Book

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'middl_name', 'date_of_birth', 'id' )
admin.site.register(Author, AuthorAdmin)


class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'id', 'public_date', 'author', )
admin.site.register(Book, BookAdmin)


class PoemAdmin(admin.ModelAdmin):
    list_display = ('tytle', 'id', 'date', 'poem_lang', 'author',)
admin.site.register(Poem, PoemAdmin)


class GenreAdmin(admin.ModelAdmin):
    list_display = ('name', 'id', 'image_genre', 'genre_text_color', 'image_name')
admin.site.register(Genre, GenreAdmin)



admin.site.register(Language)

# admin.site.register(Author)




