
from django.urls import path
from . import views
from .views import list_books, LibraryDetailView 
from .views import register, login_view, logout_view

urlpatterns = [
    path('books/', views.list_books, name='list_books'),  
    path('library/<int:pk>/', views.LibraryDetailView.as_view(), name='library_detail'), 
    path('register/', register, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'), 
]
