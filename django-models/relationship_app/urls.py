'''from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('books/', views.list_books, name='list_books'),  
    path('library/<int:pk>/', views.LibraryDetailView.as_view(), name='library_detail'), 
    path('register/', views.register, name='register'),
    path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'), 
    path('logout/', LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),
    path('admin_view/', views.admin_view, name='admin_view'),
    path('librarian/', views.librarian_view, name='librarian_view'),# Single path only
    path('member_view/', views.member_view, name='member_view'),
    path('accounts/login/', auth_views.LoginView.as_view(), name='login'),
]'''
from django.urls import path
from .views import list_books, LibraryDetailView
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('books/', list_books, name='list_books'),  # Function-based view
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),  # Class-based view for library details
    path('login/', auth_views.LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),
    path('register/', views.register, name='register'),
    path('admin/', views.admin_view, name='admin_view'),
    path('librarian/', views.librarian_view, name='librarian_view'),
    path('member/', views.member_view, name='member_view'),

    path('add_book/', views.add_book, name='add_book'),  # URL for adding a book
    path('edit_book/<int:pk>/', views.edit_book, name='edit_book'),  # URL for editing a specific book
    path('delete_book/<int:pk>/', views.delete_book, name='delete_book'),
]


