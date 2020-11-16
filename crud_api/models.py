from django.db import models

# Create your models here.


class Author(models.Model):
    # id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=200, null=True, blank=True)
    last_name = models.CharField(max_length=200, null=True, blank=True)
    nickname = models.CharField(max_length=200)
    birthdate = models.DateField(
        null=True, blank=True, help_text='Date of birth')
    books = models.ManyToManyField('Book', blank=True)

    def __str__(self):
        return self.nickname


class Book(models.Model):
    # id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    pages_num = models.IntegerField(blank=True, null=True)
    cover_image = models.URLField(null=True, blank=True)
    publisher = models.ForeignKey('Publisher', on_delete=models.CASCADE)
    authors = models.ManyToManyField('Author', blank=True)

    def __str__(self):
        return self.title


class Publisher(models.Model):
    # id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=300)

    def __str__(self):
        return self.name
