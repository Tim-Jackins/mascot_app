from django.urls import path
from . import views

urlpatterns = [
    path('', views.MascotListCreate.as_view()),
]
