
from math import ceil
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django import forms
from .models import Book
from .models import User
from django.contrib.auth import (
    authenticate,
    get_user_model,
    login,
    logout
)

from .forms import UserLoginForm
class LoginForm(forms.Form):
    UserId = forms.CharField(label='UserId', max_length=20, required=True)
    password = forms.CharField(max_length=32, widget=forms.PasswordInput, required=True)

    def clean_name(self):
        UserId = self.cleaned_data.get("UserId")
        if len(UserId) < 5:
            raise forms.ValidationError("Not a valid UserId")
        return UserId

def index(request):
    allBooks = []
    catBooks = Book.objects.values('category')
    cats = {item['category'] for item in catBooks}
    for cat in cats:
        books = Book.objects.filter(category=cat)
        n = len(books)
        nslides = ceil(n/4)
        allBooks.append([books, range(1, nslides), nslides])
    params = {'allBooks':allBooks}
    return render(request, 'index.html', params)
"""
def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/fast/')
        if form.errors:
            print(form.errors)
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form':form})
"""

def valid(request):
    validid = request.POST.get('id', 'default')
    validpwd = request.POST.get('pwd', 'default')
    print(validid, validpwd)
    return HttpResponse("Welcome "+validid+" to our libray website")
"""
def search(request):
    queryBooks = request.GET.get('book')
    queryEdition = request.GET.get('edition')
    queryAuthor = request.GET.get('Author')
    catBooks = request.GET.get('category')
    

    allBooks=[]
    if catBooks!="":
        cats = []
        cats.append(catBooks)
        if queryBooks!="" and queryEdition!="" and queryAuthor!="":
            for cat in cats:
                books = Book.objects.filter(Name__icontains=queryBooks, Edition=queryEdition, AuthorFullName__icontains=queryAuthor,category__icontains=cat)
                n = len(books)
                nslides = ceil(n/4)
                if len(books)>0:
                    allBooks.append([books, range(1, nslides), nslides])
        elif queryBooks!="" and queryEdition!="":
            for cat in cats:
                books = Book.objects.filter(Name__icontains=queryBooks, Edition=queryEdition,category__icontains=cat)
                n = len(books)
                nslides = ceil(n/4)
                if len(books)>0:
                    allBooks.append([books, range(1, nslides), nslides])
        elif queryBooks!="" and queryAuthor!="":
            for cat in cats:
                books = Book.objects.filter(Name__icontains=queryBooks, AuthorFullName__icontains=queryAuthor,category__icontains=cat)
                n = len(books)
                nslides = ceil(n/4)
                if len(books)>0:
                    allBooks.append([books, range(1, nslides), nslides])
        elif queryEdition!="" and queryAuthor!="":
            for cat in cats:
                books = Book.objects.filter(Edition__icontains=queryEdition, AuthorFullName__icontains=queryAuthor,category__icontains=cat)
                n = len(books)
                nslides = ceil(n/4)
                if len(books)>0:
                    allBooks.append([books, range(1, nslides), nslides])
        elif queryEdition!="":
            for cat in cats:
                books = Book.objects.filter(Edition=queryEdition,category__icontains=cat)
                n = len(books)
                nslides = ceil(n/4)
                if len(books)>0:
                    allBooks.append([books, range(1, nslides), nslides])
        elif queryAuthor!="":
            for cat in cats:
                books = Book.objects.filter(AuthorFullName__icontains=queryAuthor,category__icontains=cat)
                n = len(books)
                nslides = ceil(n/4)
                if len(books)>0:
                    allBooks.append([books, range(1, nslides), nslides])
        elif queryBooks!="":
            for cat in cats:
                books = Book.objects.filter(Name__icontains=queryBooks,category__icontains=cat)
                n = len(books)
                nslides = ceil(n/4)
                if len(books)>0:
                    allBooks.append([books, range(1, nslides), nslides])
        else:
            for cat in cats:
                books = []
                n = len(books)
                nslides = ceil(n/4)
                if len(books)>0:
                    allBooks.append([books, range(1, nslides), nslides])
    else:
        catBooks = Book.objects.values('category')
        cats = {item['category'] for item in catBooks}
        if queryBooks!="" and queryEdition!="" and queryAuthor!="":
            for cat in cats:
                books = Book.objects.filter(Name__icontains=queryBooks, Edition=queryEdition, AuthorFullName=queryAuthor,category=cat)
                n = len(books)
                nslides = ceil(n/4)
                if len(books)>0:
                    allBooks.append([books, range(1, nslides), nslides])
        elif queryBooks!="" and queryEdition!="":
            for cat in cats:
                books = Book.objects.filter(Name=queryBooks, Edition=queryEdition,category=cat)
                n = len(books)
                nslides = ceil(n/4)
                if len(books)>0:
                    allBooks.append([books, range(1, nslides), nslides])
        elif queryBooks!="" and queryAuthor!="":
            for cat in cats:
                books = Book.objects.filter(Name=queryBooks, AuthorFullName=queryAuthor,category=cat)
                n = len(books)
                nslides = ceil(n/4)
                if len(books)>0:
                    allBooks.append([books, range(1, nslides), nslides])
        elif queryEdition!="" and queryAuthor!="":
            for cat in cats:
                books = Book.objects.filter(Edition=queryEdition, AuthorFullName=queryAuthor,category=cat)
                n = len(books)
                nslides = ceil(n/4)
                if len(books)>0:
                    allBooks.append([books, range(1, nslides), nslides])
        elif queryEdition!="":
            for cat in cats:
                books = Book.objects.filter(Edition=queryEdition,category=cat)
                n = len(books)
                nslides = ceil(n/4)
                if len(books)>0:
                    allBooks.append([books, range(1, nslides), nslides])
        elif queryAuthor!="":
            for cat in cats:
                books = Book.objects.filter(AuthorFullName=queryAuthor,category=cat)
                n = len(books)
                nslides = ceil(n/4)
                if len(books)>0:
                    allBooks.append([books, range(1, nslides), nslides])
        elif queryBooks!="":
            for cat in cats:
                books = Book.objects.filter(Name=queryBooks,category=cat)
                n = len(books)
                nslides = ceil(n/4)
                if len(books)>0:
                    allBooks.append([books, range(1, nslides), nslides])
        else:
            for cat in cats:
                books = []
                n = len(books)
                nslides = ceil(n/4)
                if len(books)>0:
                    allBooks.append([books, range(1, nslides), nslides])
    params = {'allBooks':allBooks}
    return render(request, 'search.html', params)
"""
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'librarymanagement17k@gmail.com'
EMAIL_HOST_PASSWORD = 'impakistani007'
EMAIL_PORT = 587
subject = "Thankyou for loging in Fast library"
message = "Welcome to Fast library"
from_email = settings.EMAIL_HOST_USER


def login_view(request):
    title = "Login"
    form = UserLoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        login(request, user)
        if next:
            context = {'form': form,'email':user.email,'title':title}        
            to_list = [user.email,settings.EMAIL_HOST_USER]
            send_mail(subject,message,from_email,to_list,fail_silently=True)
            return render(request,'details.html',context)
        return redirect('')
    context = {'form': form}
    return render(request, "login.html", context)

def logout_view(request):
    logout(request)
    return redirect('/fast')

@login_required
def view_details(request):
    context={}
    context['user'] = request.user
    print(request.user)
    #user = User.objects.filter(UserID=context['user'])
    
    return render(request,"details.html",context)
"""
def search(request):
    queryBooks = request.GET.get('book')
    queryEdition = request.GET.get('edition')
    queryAuthor = request.GET.get('Author')
    catBooks = Book.objects.values('category')
    cats = {item['category'] for item in catBooks}

    allBooks=[]
    if queryBooks!="" and queryEdition!="" and queryAuthor!="":
        for cat in cats:
            books = Book.objects.filter(Name__icontains=queryBooks, Edition=queryEdition, AuthorFullName__icontains=queryAuthor,category__icontains=cat)
            n = len(books)
            nslides = ceil(n/4)
            if len(books)>0:
                allBooks.append([books, range(1, nslides), nslides])
    elif queryBooks!="" and queryEdition!="":
        for cat in cats:
            books = Book.objects.filter(Name__icontains=queryBooks, Edition=queryEdition,category__icontains=cat)
            n = len(books)
            nslides = ceil(n/4)
            if len(books)>0:
                allBooks.append([books, range(1, nslides), nslides])
    elif queryBooks!="" and queryAuthor!="":
        for cat in cats:
            books = Book.objects.filter(Name__icontains=queryBooks, AuthorFullName__icontains=queryAuthor,category__icontains=cat)
            n = len(books)
            nslides = ceil(n/4)
            if len(books)>0:
                allBooks.append([books, range(1, nslides), nslides])
    elif queryEdition!="" and queryAuthor!="":
        for cat in cats:
            books = Book.objects.filter(Edition=queryEdition, AuthorFullName__icontains=queryAuthor,category__icontains=cat)
            n = len(books)
            nslides = ceil(n/4)
            if len(books)>0:
                allBooks.append([books, range(1, nslides), nslides])
    elif queryEdition!="":
        for cat in cats:
            books = Book.objects.filter(Edition=queryEdition,category__icontains=cat)
            n = len(books)
            nslides = ceil(n/4)
            if len(books)>0:
                allBooks.append([books, range(1, nslides), nslides])
    elif queryAuthor!="":
        for cat in cats:
            books = Book.objects.filter(AuthorFullName__icontains=queryAuthor,category__icontains=cat)
            n = len(books)
            nslides = ceil(n/4)
            if len(books)>0:
                allBooks.append([books, range(1, nslides), nslides])
    elif queryBooks!="":
        for cat in cats:
            books = Book.objects.filter(Name__icontains=queryBooks,category__icontains=cat)
            n = len(books)
            nslides = ceil(n/4)
            if len(books)>0:
                allBooks.append([books, range(1, nslides), nslides])
    else:
        for cat in cats:
            books = Book.objects.filter(category__icontains=cat)
            n = len(books)
            nslides = ceil(n/4)
            if len(books)>0:
                allBooks.append([books, range(1, nslides), nslides])
    params = {'allBooks':allBooks}
    return render(request, 'search.html', params)
    """

def search(request):
    queryBooks = request.GET.get('book')
    queryEdition = request.GET.get('edition')
    queryAuthor = request.GET.get('Author')
    catBooks = Book.objects.values('category')
    cats = {item['category'] for item in catBooks}

    allBooks=[]
    if queryBooks!="" and queryEdition!="" and queryAuthor!="":
        for cat in cats:
            books = Book.objects.filter(Name=queryBooks, Edition=queryEdition, AuthorFullName=queryAuthor,category=cat)
            n = len(books)
            nslides = ceil(n/4)
            if len(books)>0:
                allBooks.append([books, range(1, nslides), nslides])
    elif queryBooks!="" and queryEdition!="":
        for cat in cats:
            books = Book.objects.filter(Name__icontains=queryBooks, Edition=queryEdition,category=cat)
            n = len(books)
            nslides = ceil(n/4)
            if len(books)>0:
                allBooks.append([books, range(1, nslides), nslides])
    elif queryBooks!="" and queryAuthor!="":
        for cat in cats:
            books = Book.objects.filter(Name__icontains=queryBooks, AuthorFullName__icontains=queryAuthor,category=cat)
            n = len(books)
            nslides = ceil(n/4)
            if len(books)>0:
                allBooks.append([books, range(1, nslides), nslides])
    elif queryEdition!="" and queryAuthor!="":
        for cat in cats:
            books = Book.objects.filter(Edition=queryEdition, AuthorFullName__icontains=queryAuthor,category=cat)
            n = len(books)
            nslides = ceil(n/4)
            if len(books)>0:
                allBooks.append([books, range(1, nslides), nslides])
    elif queryEdition!="":
        for cat in cats:
            books = Book.objects.filter(Edition=queryEdition,category=cat)
            n = len(books)
            nslides = ceil(n/4)
            if len(books)>0:
                allBooks.append([books, range(1, nslides), nslides])
    elif queryAuthor!="":
        for cat in cats:
            books = Book.objects.filter(AuthorFullName__icontains=queryAuthor,category=cat)
            n = len(books)
            nslides = ceil(n/4)
            if len(books)>0:
                allBooks.append([books, range(1, nslides), nslides])
    elif queryBooks!="":
        for cat in cats:
            books = Book.objects.filter(Name__icontains=queryBooks,category=cat)
            n = len(books)
            nslides = ceil(n/4)
            if len(books)>0:
                allBooks.append([books, range(1, nslides), nslides])
    else:
        for cat in cats:
            books = []
            n = len(books)
            nslides = ceil(n/4)
            if len(books)>0:
                allBooks.append([books, range(1, nslides), nslides])
    params = {'allBooks':allBooks}
    return render(request, 'search.html', params)