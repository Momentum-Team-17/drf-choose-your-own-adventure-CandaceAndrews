from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models import UniqueConstraint


class User(AbstractUser):
    pass


class Book(models.Model):
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

    title = models.CharField(max_length=100)
    author = models.ForeignKey(
        to='Author',
        on_delete=models.CASCADE,
    )
    year_published = models.IntegerField(blank=True, null=True)
    genre = models.CharField(choices=CHOICES, max_length=50)
    featured = models.BooleanField(default=False)

    class Meta:
        constraints = [
            UniqueConstraint(fields=['author', 'title'],
                             name='unique_constraint')
        ]
        ordering = ['title']

    def __str__(self):
        return f"{self.title} by {self.author}"


class Author(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

# class Notes(models.Model):
#     pass
