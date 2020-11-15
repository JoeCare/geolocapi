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
    # @property
    # def general_data(self):
    #     return {'id': self.id, 'first_name': self.first_name, 'last_name': self.last_name, 'nickname': self.nickname, 'birthdate': self.birthdate}

    # @property
    # def detail_data(self):
    #     return {'id': self.id, 'first_name': self.first_name, 'last_name': self.last_name, 'nickname': self.nickname, 'birthdate': self.birthdate, 'books': }

    def __str__(self):
        return self.nickname


class Book(models.Model):
    # id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    pages_num = models.IntegerField(blank=True, null=True)
    cover_image = models.URLField(null=True, blank=True)
    publisher = models.ForeignKey('Publisher', on_delete=models.CASCADE)
    authors = models.ManyToManyField('Author', blank=True)

    # publisher_name = Book.objects.filter(id=self.publisher)
    # def get_publisher_data(self):
    #     for atr in publisher:...   # which goes to:
    # publisher_name = [name for name in self.publisher if 'name' in name]

    # def get_book_authors(self):
    #     authors =
    #     pass

    def __str__(self):
        return self.title

    # def __repr__(self):
    #     return self.title

    # @property
    # def general_data(self):
    #     return {'id': self.id, 'title': self.title, 'cover_image': self.cover_image, 'publisher': self.publisher.name}

    # from rest_framework.reverse import reverse
    # def get_url_api(self, request=None):
    #     # hosts --> subdomains
    #     return reverse('api-postings:post-rud', kwargs={'id': self.id}, request=request)


class Publisher(models.Model):
    # id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=300)

    def __str__(self):
        return self.name
