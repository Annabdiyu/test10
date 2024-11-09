
from django.urls import path
from . import views
from .views import list_books, LibraryDetailView 
from .views import register, LoginView, LogoutView

urlpatterns = [
    path('books/', views.list_books, name='list_books'),  
    path('library/<int:pk>/', views.LibraryDetailView.as_view(), name='library_detail'), 
    path('register/', views.register, name='register'),  # Registration view
    path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'),  # Login view
    path('logout/', LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),  # Logout view 
]
