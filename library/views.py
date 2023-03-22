from django.shortcuts import render
from django.http import JsonResponse
from .models import Book
from .serializers import BookSerializer


def list_books_json(request):
    all_books = Book.objects.all()
    book_data = {'books': []}

    for book in all_books:
        serializer = BookSerializer(book)
        new_book_dict = serializer.serialize()
        book_data['books'].append(new_book_dict)

    return JsonResponse(book_data)
