from django.db import models

# Create your models here.
class Author(models.Model):
    name=models.CharField(max_length=100)
    
    
class Book(models.Model):
    title=models.CharField(max_length=100)
    author=models.ForeignKey(Author,on_delete=models.CASCADE,related_name='Books')
    
    
class Library(models.Model):
    name=models.CharField(max_length=100)
    books=models.ManyToManyField(Book)
    
    
class Librarian(models.Model):
    name=models.CharField(max_length=100)
    library=models.OneToOneField(Library,on_delete=models.CASCADE,related_name='librarians')
