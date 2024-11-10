
from django.shortcuts import render
from django.views.generic.detail import DetailView
from .models import Library  
from .models import Book

from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test

from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render, redirect
from .models import UserProfile
from django.core.exceptions import PermissionDenied

from django.http import HttpResponseForbidden



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

@login_required
@user_passes_test(is_librarian)
def librarian_view(request):
    # Check if the user is authenticated and has a UserProfile
    if request.user.is_authenticated:
        try:
            user_profile = UserProfile.objects.get(user=request.user)
            # Allow access only if the role is 'Librarian'
            if user_profile.role == 'Librarian':
                # Your view logic here
                return render(request, 'relationship_app/librarian_view.html')
            else:
                return HttpResponseForbidden("You do not have permission to access this page.")
        except UserProfile.DoesNotExist:
            return HttpResponseForbidden("User profile not found.")
    else:
        return HttpResponseForbidden("You need to be logged in to access this page.")


@user_passes_test(is_member)
def member_view(request):
    return render(request, 'relationship_app/member_view.html')
def home(request):
    return render(request, 'relationship_app/home.html')