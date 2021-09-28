from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('delete', views.delete, name="delete"),
    path('put', views.put, name='put'),
    path('tags', views.get_tags, name='tags'),
    path('tag', views.get_postit_tags, name='tag')
]