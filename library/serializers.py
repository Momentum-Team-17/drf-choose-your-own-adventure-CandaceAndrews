from rest_framework import serializers
import django_filters
from .models import Book, Author, User, Tracking, Genre


class GenreSerializer(serializers.ModelSerializer):

    class Meta:
        model = Genre
        fields = '__all__'


class AuthorSerializer(serializers.ModelSerializer):
    name = serializers.StringRelatedField(many=False)

    class Meta:
        model = Author
        fields = (
            '__all__'
        )


class BookSerializer(serializers.ModelSerializer):
    author = AuthorSerializer()
    genre = GenreSerializer(many=True)

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
