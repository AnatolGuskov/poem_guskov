
from django.contrib import admin

from .models import Language, Author, Genre, Poem, Book

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'middl_name', 'date_of_birth', )

admin.site.register(Author, AuthorAdmin)

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'display_genre')

admin.site.register(Language)
admin.site.register(Genre)
# admin.site.register(Author)
admin.site.register(Poem)
admin.site.register(Book)


