
from django.contrib import admin

from .models import Language, Author, Genre, Poem, Book

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'middl_name', 'date_of_birth', )
admin.site.register(Author, AuthorAdmin)


class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author')
admin.site.register(Book, BookAdmin)


class PoemAdmin(admin.ModelAdmin):
    list_display = ('date', 'title', 'author')
admin.site.register(Poem, PoemAdmin)


admin.site.register(Language)
admin.site.register(Genre)
# admin.site.register(Author)




