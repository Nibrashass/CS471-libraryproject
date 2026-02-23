from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='books.index'),
    path('aboutus/', views.aboutus, name='books.aboutus'),
    path('list_books/', views.list_books, name='books.list_books'),
    path('one_book/', views.one_book, name='books.one_book'),
]