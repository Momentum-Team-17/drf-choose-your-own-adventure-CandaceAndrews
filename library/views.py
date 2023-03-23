from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, filters
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from django.forms.models import model_to_dict

from .models import Book, User, Tracking, Author, Genre
from .serializers import BookSerializer, UserSerializer, TrackingSerializer, AuthorSerializer, GenreSerializer


@api_view(["GET"])
def api_root(request, format=None):
    return Response(
        {
            "Books": reverse('book-list', request=request, format=format),
            "Book Search": reverse('book-search', request=request, format=format),
            "Featured Books": reverse('book-featured', request=request, format=format),
            "Users": reverse('users', request=request, format=format),
            "User Tracking": reverse('user-tracking', request=request, format=format),
            "Authors": reverse('author-list', request=request, format=format),
            "Genre": reverse('genre-list', request=request, format=format),
        }
    )


class BookList(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def create(self, request):

        author_id = request.data.get("author").get("id")
        author = Author.objects.get(id=author_id)
        title = request.data.get('title')
        # genres = request.data.get('genre')
        # writable nested serializer, update queryset, manytomany diff than one to many
        # pre-fetch related
        book = Book.objects.create(
            author=author, title=title)
        book_serializer = BookSerializer(book)
        return Response(book_serializer.data)


class BookDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookSearch(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'author__name']


class BookFeatured(generics.ListAPIView):
    queryset = Book.objects.filter(featured=True)
    serializer_class = BookSerializer


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserTrackingList(generics.ListCreateAPIView):
    serializer_class = TrackingSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['status']

    def get_queryset(self):
        user_id = self.request.user.id
        queryset = Tracking.objects.filter(user_id=user_id)
        return queryset


class AuthorList(generics.ListAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class GenreList(generics.ListAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
