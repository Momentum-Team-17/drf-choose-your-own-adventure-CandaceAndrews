from rest_framework import serializers
import django_filters
from .models import Book, Author, User, Tracking


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


class TrackingSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tracking
        fields = (
            "status",
            "user",
            "book",
        )
