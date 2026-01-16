from django.urls import path
from . import views 

# Define URL patterns for the asiatouragency app
urlpatterns = [
    path('', views.index, name='index'), 
]