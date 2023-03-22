from .models import Book, Author


class BookSerializer():
    def __init__(self, instance):
        self.instance = instance

    class Meta:
        Book

    def serialize(self):
        book_as_dict = {
            'pk': self.instance.pk,
            'title': self.instance.title,
        }
        return book_as_dict
