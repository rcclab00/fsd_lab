from django.urls import path
from . import views
urlpatterns = [
    path('', views.home),
    path('filter/', views.filter_year),
]

