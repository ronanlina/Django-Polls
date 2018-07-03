from django.urls import path
from . import views

urlpatterns = [
    # /[app name]/id/url
    path('', views.index, name='index'), #index url
    path('test/', views.test,name='test'), #refer to the view method that returns the page.
    path('<int:question_id>/',views.detail, name='detail'),
    path('<int:question_id>/results/',views.results, name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
]