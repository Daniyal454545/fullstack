from django.urls import path
from sportcrud import views
urlpatterns = [
    path('sport', views.sportcrud, name='sport-list')
]