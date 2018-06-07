from django.urls import path
from . import views


app_name = 'karma'

urlpatterns = [
    path('', views.index, name='index'),
    path('new', views.NewGameView.as_view(), name='new_game'),
]
