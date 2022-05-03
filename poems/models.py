from django.db import models
from django.urls import reverse
import datetime
import uuid  # Required for unique book instances

#POEM_GUSKOV

# =========================== LANGUAGE ========================
class Language(models.Model):
    """Model representing a Language (e.g. English, French, Japanese, etc.)"""
    name = models.CharField(max_length=200,
                            help_text="Enter the book's natural language (e.g. English, French, Japanese etc.)")

    def __str__(self):
        return self.name





# ================ Author ===============================
class Author(models.Model):
    class Meta:
        ordering = ["last_name"]
    author = models.CharField(default="Гуськов", max_length=25)
    first_name = models.CharField(null=True, blank = True, max_length=25)
    middl_name = models.CharField(null=True, blank = True, max_length=25)
    last_name = models.CharField(max_length=45)
    date_of_birth = models.DateField(null=True, blank=True)
    date_of_death = models.DateField(null=True, blank=True)
    city = models.CharField(max_length=25, null=True, blank = True)


    # date_of_death = models.DateField('Died', null=True, blank=True)
    # def full_name(self):
    #     return self.first_name + " " + self.last_name

    def get_absolute_url(self):
        return reverse('poems:author-detail', args=[str(self.id)])

    def __str__(self):
        return (self.last_name+ " " + self.first_name)
    # def get_absolute_url(self):
    #     return reverse('author-detail', args=[str(self.id)])


# ================ Genre ===============================
class Genre(models.Model):
    class Meta:
        ordering = ["name"]
    name = models.CharField(max_length=30,
                            help_text="Enter a book genre (e.g. Бог, Війна, Любов etc.)")

    def __str__(self):
        return str(self.name)

    def get_absolute_url(self):
        return reverse('poems:genre-detail', args=[str(self.id)])


# ================ BOOK ===============================
class Book(models.Model):
    public_date = models.DateField(null = True , blank = True)
    name_book = models.CharField(null=True, max_length=20)
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True)
    author_status = models.CharField(null=True, blank = True, max_length=30)
    summary = models.TextField(null=True, blank = True, max_length=1000, help_text="Enter a brief description")
    isbn = models.CharField(default='ISBN', max_length=17, help_text='17 Character <a href="https://www.isbn-international.org/content/what-isbn">ISBN number</a>')
    # language = models.ForeignKey(Language, on_delete=models.SET_NULL, null=True)
    pages = models.IntegerField(default=0)
    poems_count = models.IntegerField(default=0)
    image = models.ImageField(null=True, blank = True, upload_to='images/')

    def __str__(self):
        return str(str.upper(self.title))

    def get_absolute_url(self):
        return reverse('poems:book-detail', args=[str(self.id)])


# ================ Poem ===============================
class Poem(models.Model):
    class Meta:
        ordering = ["tytle"]
    date = models.DateField(null = True, blank = True, )
    author = models.ForeignKey(Author, on_delete=models.SET_NULL,
                               default = "Анатолій Гуськов", null = True, blank=True)
    tytle = models.CharField(default=" ", max_length=100)
    poem_lang = models.CharField(default="укр.", max_length=4)
    headline = models.CharField(max_length=200)
    content = models.TextField()
    genre = models.ManyToManyField(Genre, help_text="Select a genre for this poem")
    book = models.ManyToManyField(Book, help_text="Enter books, where ware this poem")
    summary = models.TextField(blank = True, max_length=1000,
                               default="", help_text="Enter a poem description")
    # collage = models.ImageField(blank = True, upload_to='collages/', default = "")

    def __str__(self):
        return str(self.tytle)

    def get_absolute_url(self):
        return reverse('poems:poem-detail', args=[str(self.id)])

#===========================================python manage.py migratepython manage.py migratepython manage.py migrate
