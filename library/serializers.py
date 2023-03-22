from rest_framework import serializers
from .models import Book, Author, User


class BookSerializer(serializers.ModelSerializer):

    class Meta:
        model = Book
        fields = (
            "id",
            "title",
            "author",
            "year_published",
            "genre",
            "featured",
        )


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = (
            "id",
            "username",
        )
