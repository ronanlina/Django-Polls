from django.urls import path
from . import views

app_name = 'polls' # namespacing to differentiate which app to use

urlpatterns = [
    # /[app name]/id/url
    path('', views.IndexView.as_view(), name='index'), #index url
    path('test/', views.test,name='test'), #refer to the view method that returns the page.
    path('<int:pk>/',views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/',views.ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
]