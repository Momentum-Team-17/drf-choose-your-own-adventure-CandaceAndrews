from django.shortcuts import render
from django.http import JsonResponse
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse

from .models import Book
from .serializers import BookSerializer


@api_view(["GET"])
def api_root(request, format=None):
    return Response(
        {
            "Books": reverse('book-list', request=request, format=format),
        }
    )


class BookList(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
