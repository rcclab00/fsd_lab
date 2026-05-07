from django.urls import path
from . import views
urlpatterns = [
    path('', views.home),
    path('amazon/', views.amazon_students),
]
