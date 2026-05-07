from django.urls import path
from . import views
urlpatterns = [
    path('', views.home),
    path('cse_prof/', views.cse_professors),
]
