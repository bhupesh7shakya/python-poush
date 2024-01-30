from .views import *
from django.urls import path
urlpatterns = [
    path('', home, name="home"),
    path('delete/<id>', delete, name="delete"),
    path('change/<id>', change, name="change"),
    path('insert', insert, name="insert"),
    path('edit/<id>', edit, name="edit"),
]
