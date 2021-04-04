from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('download', views.download, name='download'),
    path('search', views.do_search, name='searchdata'),
]