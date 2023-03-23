from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from library import views


urlpatterns = [
    path("", views.api_root),
    path("books/", views.BookList.as_view(), name="book-list"),
    path("books/<int:pk>/", views.BookDetail.as_view(), name='book-detail'),
    path('books/search/', views.BookSearch.as_view(), name='book-search'),
    path('books/featured/', views.BookFeatured.as_view(), name='book-featured'),
    path('users/', views.UserList.as_view(), name="users"),
    path('users/<int:pk>/', views.UserDetail.as_view(), name="user-detail"),
    path('users/tracking/', views.UserTrackingList.as_view(), name="user-tracking"),
    path('authors/', views.AuthorList.as_view(), name="author-list"),
    path('genre/', views.GenreList.as_view(), name='genre-list'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
