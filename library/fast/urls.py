from django.urls import path
from django.contrib.auth.views import LoginView
from django.conf.urls import url
from django.contrib import admin
from django.urls import path,include
from . import views
from . import QRcodeReader
from django.conf.urls import include, url
#from django_file_download import views as file_views
#from .views import login_view, logout_view

urlpatterns = [
    path('', views.index, name="home"),
    path('login/', views.login_view, name="login"),
    #url(r'^login/$', LoginView.as_view(), name='login'),
    path('search/', views.search, name="search"),
    path('admin/', admin.site.urls),
    path('details/', views.view_details, name="details"),
    #path('registration/login/', views.login_view,name="login"),
    path('logout/', views.logout_view,name="logout"),
    path('bookinfo/',QRcodeReader.readbarcode,name="barcode"),
    #url(r'^download$', file_views.file_download, name='file_download'),
    #path('advancesearch/', views.advancesearch,name="advancesearch"),
]
