from django.contrib import admin
from .models import User, Book, Author, Genre, Tracking, Notes

admin.site.register(User)
admin.site.register(Book)
admin.site.register(Author)
admin.site.register(Genre)
admin.site.register(Tracking)
admin.site.register(Notes)
