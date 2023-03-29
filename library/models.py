from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser


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
            models.UniqueConstraint(
                fields=['author', 'title'],
                name='unique_constraint')
        ]
        ordering = ['title']

    def __str__(self):
        return f"{self.title} by {self.author}"


class Author(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['name'],
                name='unique_author_name')
        ]

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
        constraints = [
            models.UniqueConstraint(
                fields=['genre_name'],
                name='unique_genre_name'
            )
        ]

    def __str__(self):
        return self.genre_name


class Tracking(models.Model):
    CHOICES = (
        ('want to read', 'Want To Read'),
        ('reading', 'Reading'),
        ('read/done', 'Read/Done'),
    )
    status = models.CharField(choices=CHOICES, max_length=50)
    user = models.ForeignKey(
        to=User, on_delete=models.CASCADE, related_name="tracking_instances")
    book = models.ForeignKey(
        to=Book, on_delete=models.CASCADE, related_name="tracking_instances")

    class Meta:
        verbose_name = "Tracking"
        verbose_name_plural = "Tracking"

        constraints = [
            models.UniqueConstraint(
                fields=[
                    'user',
                    'book'
                ],
                name='unique_user_book'
            )
        ]

    def __str__(self):
        return f"{self.user.username} - {self.book.title}: {self.status}"


class Notes(models.Model):
    book = models.ForeignKey(to=Book, on_delete=models.CASCADE)
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now)
    note_body = models.TextField()
    is_public = models.BooleanField(default=True)
    page_number = models.IntegerField(blank=True, null=True)

    class Meta:
        verbose_name = "Note"
        verbose_name_plural = "Notes"

    def __str__(self):
        return f"Notes on - {self.book.title}"
