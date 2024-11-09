
from django.shortcuts import render
from django.views.generic.detail import DetailView
from .models import Library  
from .models import Book

from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test

from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render, redirect
from .models import UserProfile
from django.core.exceptions import PermissionDenied


def list_books(request):
    books = Book.objects.all()  
    return render(request, 'relationship_app/list_books.html', {'books': books})


class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'




def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  
            return redirect('home')  
    else:
        form = UserCreationForm()
    return render(request, 'relationship_app/register.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'relationship_app/login.html', {'form': form})


@login_required
def logout_view(request):
    logout(request)
    return render(request, 'relationship_app/logout.html')




def is_admin(user):
    return user.userprofile.role == 'Admin'


def is_librarian(user):
    return user.is_authenticated and user.userprofile.role == 'Librarian'


def is_member(user):
    return user.userprofile.role == 'Member'

@user_passes_test(is_admin)
def admin_view(request):
    return render(request, 'relationship_app/admin_view.html')


def librarian_view(request):
    # If the user is not a Librarian, raise PermissionDenied
    if not is_librarian(request.user):
        raise PermissionDenied
    
    # If the user is a Librarian, render the view
    return render(request, 'relationship_app/librarian_view.html')


@user_passes_test(is_member)
def member_view(request):
    return render(request, 'relationship_app/member_view.html')