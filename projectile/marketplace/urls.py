from django.urls import path
from .views import *

urlpatterns = [
    path('', AddFileDetatils.as_view())
]