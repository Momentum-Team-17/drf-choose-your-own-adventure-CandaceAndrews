from django.shortcuts import render
from django.db.models import Q
from django_filters import rest_framework as filters
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAdminUser
from rest_framework import generics, filters, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from django_filters.rest_framework import DjangoFilterBackend
from django.forms.models import model_to_dict

from .models import Book, User, Tracking, Author, Genre, Notes
from .serializers import BookSerializer, UserSerializer, TrackingSerializer, AuthorSerializer, GenreSerializer, NoteSerializer


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
            "Notes": reverse('notes-list', request=request, format=format)
        }
    )


class BookList(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def create(self, request):
        author_id = request.data.get("author").get("id")
        author = Author.objects.get(id=author_id)
        title = request.data.get("title")
        book = Book.objects.create(
            author=author, title=title)
        # genres = request.data.get("genre", [])
        # for genre_name in genres:
        #     genre = Genre.objects.get_or_create(genre_name=genre_name)
        #     book.genre.add(genre)

        book_serializer = BookSerializer(book)
        return Response(book_serializer.data)


class BookDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    @permission_classes([IsAdminUser])
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    @permission_classes([IsAdminUser])
    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

    @permission_classes([IsAdminUser])
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


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


class NoteList(generics.ListAPIView):
    serializer_class = NoteSerializer

    def get_queryset(self):
        user = self.request.user
        if user.is_authenticated:
            return Notes.objects.filter(Q(user=user) | Q(is_public=True))
        else:
            return Notes.objects.filter(is_public=True)


# -----------------------------------------------------------------
# class NoteList(generics.ListAPIView):
#     serializer_class = NoteSerializer
#     filter_backends = [DjangoFilterBackend]
#     # filterset_fields = ['is_public']

#     def get_queryset(self):
#         user_id = self.request.user.id
#         queryset = Notes.objects.filter(user_id=user_id)
#         return queryset


# @api_view(["GET"])
# def book_notes(request):
#     # Get the notes for the specified book ID
#     notes = Notes.objects.order_by("-created_at")

#     # Filter out private notes that were not created by the current user
#     if not request.user.is_authenticated:
#         notes = notes.filter(is_public=True)
#     else:
#         notes = notes.filter(Q(is_public=True) | Q(user=request.user))

#     # Serialize the notes and return them in the response
#     serializer = NoteSerializer(notes, many=True)
#     return Response(serializer.data)


# @api_view(["POST"])
# def create_note(request):
#     # Get the book and user IDs from the request data
#     book_id = request.data.get("book_id")
#     user_id = request.data.get("user_id")

#     # Create a new Note object
#     note = Note(
#         book_id=book_id,
#         user_id=user_id,
#         note_body=request.data.get("note_body"),
#         is_public=request.data.get("is_public"),
#         page_number=request.data.get("page_number")
#     )
#     # Save the note to the database
#     note.save()

#     # Serialize the note and return it in the response
#     serializer = NoteSerializer(note)
#     return Response(serializer.data, status=status.HTTP_201_CREATED)
