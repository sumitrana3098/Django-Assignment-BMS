from django.urls import path
from inventory.views import book_list, add_book, update_book

urlpatterns = [
    path('', book_list, name='book_list'),
    path('add/', add_book, name='add_book'),
    path('update/<int:book_id>/', update_book, name='update_book'),
]
