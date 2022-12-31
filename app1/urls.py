from django.urls import path
from app1.views import *

app_name='lokesh'

urlpatterns = [
    path('manish/',manish,name='mainsh'),
]
