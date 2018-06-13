from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

from . import views

app_name = 'forum'

urlpatterns = [
    path('', views.index, name='index'),
    path('tag/<slug:tag_id>', views.index, name='tag'),
    path('topic/<slug:topic_id>', views.topis, name='topic'),
    path('topic/add/', views.add_topic, name='add-topic'),
    path('topic/add-tag/', views.add_tag, name='add-tag'),
]
