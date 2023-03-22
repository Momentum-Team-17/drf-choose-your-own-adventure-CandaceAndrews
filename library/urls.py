from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from library import views


urlpatterns = [
    path("", views.api_root),
    path("books/", views.BookList.as_view(), name="book-list"),
    path("books/<int:pk>/", views.BookDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
