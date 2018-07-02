from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'), #index url
    path('test/', views.test,name='test') #refer to the view method that returns the page.
]