from django.contrib import admin
from .models import Book
from .models import Profile
from .models import Borrower
from .models import IssuedBooks
# Register your models here.

admin.site.register(Profile)
admin.site.register(Book)
admin.site.register(Borrower)
admin.site.register(IssuedBooks)
