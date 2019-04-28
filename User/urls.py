
from django.urls import path,include
from .views import *
app_name = 'User'
urlpatterns = [
    path('', loginView.as_view(), name='loginView'),
]