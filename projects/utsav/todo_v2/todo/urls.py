from .views import *
from django.urls import path
urlpatterns = [
    path('', home),
    path('delete/<id>', delete),
    path('change/<id>', change),
    path('insert', insert),
    path('edit/<id>', edit),
]
