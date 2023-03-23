from rest_framework import serializers
import django_filters
from .models import Book, Author, User, Tracking


class BookSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(many=False)
    genre = serializers.StringRelatedField(many=True)

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


class TrackingSerializer(serializers.ModelSerializer):
    book = serializers.StringRelatedField(many=False)
    user = serializers.StringRelatedField(many=False)

    class Meta:

        model = Tracking
        fields = (
            "user",
            "book",
            "status",
        )


class UserSerializer(serializers.ModelSerializer):
    tracking_instances = TrackingSerializer(
        many=True, read_only=True)

    class Meta:
        model = User
        fields = (
            "id",
            "username",
            "tracking_instances",
        )


class AuthorSerializer(serializers.ModelSerializer):
    name = serializers.StringRelatedField(many=False)

    class Meta:
        model = Book
        fields = (
            "name",
        )
