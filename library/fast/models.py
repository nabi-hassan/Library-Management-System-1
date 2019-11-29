from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
#from filetransfers.api import serve_file

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=20, default='Ali')
    password = models.CharField(max_length=20, default='Ali')
    email = models.EmailField()
    NoOfBookIssued = models.IntegerField(default=123)
    def __str__(self):
        return self.name

class Book(models.Model):
    ISBN = models.IntegerField(default=1234, primary_key=True)
    DatePurchased = models.DateField(default=None, blank=True, null=True)
    Name = models.CharField(max_length=50, default='Ali')
    Edition = models.IntegerField(default=1234)
    Price = models.IntegerField(default=1234)
    Copies = models.IntegerField(default=1234)
    Publisher = models.CharField(max_length=20, default='Ali')
    AuthorFullName=models.CharField(max_length=30,default='Ali')
    image = models.ImageField(default=None, blank=True, null=True)
    category = models.CharField(max_length=20, default='Ali')
    Barcode = models.BigIntegerField(default=None, blank=True, null=True)
    #file = models.FileField(upload_to='')
    views = models.IntegerField(default=0)
    def __str__(self):
        return self.Name

class Borrower(models.Model):
    noOfBookIssued = models.IntegerField(default=123)
    userID = models.ForeignKey(Profile, on_delete=models.CASCADE)

class IssuedBooks(models.Model):
    noofRenews = models.IntegerField(default=123)
    issueDate = models.DateField(default=123)
    userID = models.ForeignKey(Profile, on_delete=models.CASCADE)
    ISBN = models.ForeignKey(Book, on_delete=models.CASCADE)
    DueFine = models.IntegerField(default=0)
    returnDate = models.DateField(default=123, blank=True, null=True)
