from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models import UniqueConstraint


class User(AbstractUser):
    pass


class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(
        to='Author',
        on_delete=models.CASCADE,
    )
    year_published = models.IntegerField(blank=True, null=True)
    genre = models.ManyToManyField(to='Genre', related_name='genre')
    featured = models.BooleanField(default=False)

    class Meta:
        constraints = [
            UniqueConstraint(
                fields=['author', 'title'],
                name='unique_constraint')
        ]
        ordering = ['title']

    def __str__(self):
        return f"{self.title} by {self.author}"


class Author(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        constraints = [models.UniqueConstraint(
            fields=['name'], name='unique_author_name')]

    def __str__(self):
        return self.name


class Genre(models.Model):
    CHOICES = (
        ('education', 'Education'),
        ('graphic novel', 'Graphic Novel'),
        ('horror', 'Horror'),
        ('romance', 'Romance'),
        ('fantasy', 'Fantasy'),
        ('thriller', 'Thriller'),
        ('mystery', 'Mystery'),
        ("children's literature", "Children's Literature"),
        ('biography', 'Biograpy'),
        ('adventure', 'Adventure'),
        ('cookbook', 'Cookbook'),
        ('historical', 'Historical'),
        ('fiction', 'Fiction'),
        ('nonfiction', 'Non-fiction'),
        ('science fiction', 'Science Fiction'),
    )
    genre_name = models.CharField(choices=CHOICES, max_length=50)

    class Meta:
        constraints = [models.UniqueConstraint(
            fields=['genre_name'], name='unique_genre_name')]

    def __str__(self):
        return self.genre_name

# class Notes(models.Model):
#     pass
