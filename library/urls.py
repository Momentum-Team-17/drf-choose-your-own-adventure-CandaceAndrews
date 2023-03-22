from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from library import views


urlpatterns = [
    path("", views.api_root),
    path("books/", views.BookList.as_view(), name="book-list"),
    path("books/<int:pk>/", views.BookDetail.as_view(), name='book-detail'),
    path('books/search/', views.BookSearch.as_view(), name='book-search'),
    path('books/featured/', views.BookFeatured.as_view(), name='book-featured'),
    path('users/', views.UserList.as_view()),
    path('users/<int:pk>/', views.UserDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
