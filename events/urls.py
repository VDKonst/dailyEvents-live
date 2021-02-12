"""dailyEvents URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from django.conf.urls import url, include
from . import views


urlpatterns = [
    path('exhibitions/',views.Exhibitions.as_view(),name='exhibitions'),
    path('various-events/',views.NonTypeEvents.as_view(),name='various-events'),
    path('films/',views.Films.as_view(),name='films'),
    path('concerts/',views.Concerts.as_view(),name='concerts'),
    path('theatre-events/',views.TheatreEvents.as_view(),name='theatre-events'),
    path('sport/',views.SportEvents.as_view(),name='sport'),
    path('restaurants/',views.Restaurants.as_view(),name='restaurants'),
    path('various-places/',views.NonTypePlaces.as_view(),name='various-places'),
    path('concerthalls/',views.СoncertHalls.as_view(),name='concerthalls'),
    path('theatres/',views.Theatres.as_view(),name='theatres'),
    path('cinema-theatres/',views.CinemaTheatres.as_view(),name='cinema-theatres'),
    path('showrooms/',views.Showrooms.as_view(),name='showrooms'),
    path('restaurants/<str:item_slug>/',views.restaurantDetailed,name='restaurant'),
    path('various-places/<str:item_slug>/',views.nonTypePlacesDetailed,name='various-place'),
    path('concerthalls/<str:item_slug>/',views.concerthallDetailed,name='concert_hall'),
    path('cinema-theatres/<str:item_slug>/',views.cinemaTheatreDetailed,name='cinema'),
    path('theatres/<str:item_slug>/',views.theatreDetailed,name='theatre'),
    path('showrooms/<str:item_slug>/',views.showroomsDetailed,name='showroom'),
    path('various-events/<str:item_slug>/',views.nonTypeEventsDetailed,name='various-event'),
    path('exhibitions/<str:item_slug>/',views.exhibitionsDetailed,name='exhibition'),
    path('concerts/<str:item_slug>/',views.concerteDetailed,name='concert_event'),
    path('sport/<str:item_slug>/',views.sportDetailed, name='sport_event'),
    path('theatre-events/<str:item_slug>/',views.theatreEventDetailed, name='theatre_event'),
    path('films/<str:item_slug>/',views.filmDetailed, name='film_event'),
    path('create-event/',views.createEvent, name='create_event'),
    
    

]
