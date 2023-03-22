from django.contrib import admin
from .models import User, Book, Author

admin.site.register(User)
admin.site.register(Book)
admin.site.register(Author)
