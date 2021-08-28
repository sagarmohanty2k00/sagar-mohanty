from django.urls import path
from . import views
urlpatterns = [
    path('message/', views.send),
]