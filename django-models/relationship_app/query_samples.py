'''from relationship_app.models import Author, Book, Library, Librarian


def books_by_author(author_name):
    author = Author.objects.get(name=author_name)
    books = Book.objects.filter(author=author)
    return books


def books_in_library(library_name):
    library = Library.objects.get(name=library_name)
    books = library.books.all()
    return books


def librarian_for_library(library_name):
    library = Library.objects.get(name=library_name)
    librarian = Librarian.objects.get(library=library)
    return librarian'''

from relationship_app.models import Author, Book, Library, Librarian

# Query 1: All books by a specific author
def get_books_by_author(author_name):
    author = Author.objects.get(name=author_name)
    books = Book.objects.filter(author=author)
    for book in books:
        print(book.title)

# Query 2: List all books in a library
def get_books_in_library(library_name):
    library = Library.objects.get(name=library_name)
    books = library.books.all()
    for book in books:
        print(book.title)

# Query 3: Retrieve the librarian for a library
def get_librarian_for_library(library_name):
    library = Library.objects.get(name=library_name)
    librarian = Librarian.objects.get(library=library)
    print(f"The librarian for {library.name} is {librarian.name}")