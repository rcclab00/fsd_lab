from django.urls import path
from . import views
urlpatterns = [
    path('', views.home),
    path('high/', views.high_salary),
]
