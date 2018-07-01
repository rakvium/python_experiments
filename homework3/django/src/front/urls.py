"""
Poll's module urls
"""
from django.urls import path
from django.conf.urls import include

from . import views

# pylint: disable=invalid-name
app_name = 'front'

# pylint: disable=invalid-name
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail')
]
