from django.urls import path
from . import views

urlpatterns = [
    path('', views.snewss, name="snewss"),

]

