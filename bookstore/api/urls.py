# your_app/urls.py
from django.urls import path
from .views import add_book, get_all_books, get_book_by_isbn, update_book, delete_book
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView


urlpatterns = [
    # Endpoint for adding a new book
    path('add_book/', add_book, name='add_book'),

    # Endpoint for retrieving all books
    path('get_all_books/', get_all_books, name='get_all_books'),

    # Endpoint for retrieving a specific book by ISBN
    path('get_book_by_isbn/<str:isbn>/', get_book_by_isbn, name='get_book_by_isbn'),

    # Endpoint for updating book details by ISBN
    path('update_book/<str:isbn>/', update_book, name='update_book'),

    # Endpoint for deleting a book by ISBN
    path('delete_book/<str:isbn>/', delete_book, name='delete_book'),
]
