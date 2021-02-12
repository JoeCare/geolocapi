from django.db import models
from pygments.lexers import get_lexer_by_name, get_all_lexers
from pygments.styles import get_all_styles
from pygments.formatters.html import HtmlFormatter
from pygments import highlight
# Create your models here.

LEXERS = [item for item in get_all_lexers() if item[1]]  # if len(item)>1 take it
CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])  # for every item in L take first of the second row and
# first row and sort asc list of tuples?
STYLES = sorted([(item, item) for item in get_all_styles()])


class Author(models.Model):
    # id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=200, null=True, blank=True)
    last_name = models.CharField(max_length=200, null=True, blank=True)
    nickname = models.CharField(max_length=200)
    birthdate = models.DateField(
        null=True, blank=True, help_text='Date of birth')
    books = models.ManyToManyField('Book', blank=True)
    # book = models.ForeignKey('Book', related_name='authors', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Book(models.Model):
    # id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    pages_num = models.IntegerField(blank=True, null=True)
    cover_image = models.URLField(null=True, blank=True)
    publisher = models.ForeignKey('Publisher', on_delete=models.CASCADE)
    authors = models.ManyToManyField('Author', blank=True)
    owner = models.ForeignKey('Author', related_name='creations', on_delete=models.CASCADE)
    highlighted = models.TextField()

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        """
        Highlighted HTML repr of the books with pygments lib.
        """
        lexer = get_lexer_by_name(self.title)


class Publisher(models.Model):
    # id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=300)

    def __str__(self):
        return self.name
