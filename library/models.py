from django.db import models
from django.contrib.auth.models import AbstractUser


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
    )

    title = models.CharField(max_length=100)
    author = models.ForeignKey(
        to='Author', on_delete=models.CASCADE, related_name='author')
    date_published = models.DateField(blank=True, null=True)
    genre = models.CharField(choices=CHOICES, max_length=50)
    # featured =


class Author(models.Model):
    name = models.CharField(max_length=50)


# class Notes(models.Model):
#     pass
