from django.urls import path
from . import views

urlpatterns = [
   	path('', views.UserSearch, name='usersearch'),
    ]