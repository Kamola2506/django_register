from django.urls import path
from .views import home, mening_ismim ,mening_familyam, yoshim, university, postlar


urlpatterns = [
    path('home/', home, name='home'),
    path('mening_ismim/', mening_ismim, name='mening_ismim'),
    path('mening_familyam/', mening_familyam, name='mening_familyam'),
    path('yoshim/', yoshim, name='yoshim'),
    path('university/', university, name='university'),
    path('postlar/', postlar, name='postlar'),
]