from django.shortcuts import redirect, render
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import ListView, DetailView, CreateView
from .models import *
from .forms import  EventForm


def createEvent(request):
    context = {}
    if not request.user.is_owner:
        return redirect('index')
    if request.method == 'POST':
        form = EventForm(request.POST,request.FILES)
        if form.is_valid():
            event = Event()
            event.name = form.cleaned_data.get('name')
            event.photo = form.cleaned_data.get('photo')
            event.description = form.cleaned_data.get('description')
            event.short_description = form.cleaned_data.get('short_description')
            event.save()
            return redirect('index')
        else:
            context['form'] = form
    else:
        form = EventForm()
        context['form'] = form
    return render(request, 'events/create_event.html', context)

def index(request):
    return render(request,'index.html')


def restaurantDetailed(request,item_slug):
    context = {}
    item = Restaurant.objects.get(slug__iexact=item_slug)
    schedule = Schedule.objects.filter(place__pk=item.pk)
    context['schedule'] = schedule
    follows = item.followers.count()
    if follows % 10 == 1:
        follows = '{} пользователя'.format(follows)
    else:
        follows = '{} пользователей'.format(follows)
    context['object'] = item
    context['follows'] = follows
    if request.method == 'POST':
        item.followers.add(request.user)
        return redirect(item.get_absolute_url())
    else:
        return render(request, 'events/restaurant_detailed.html', context)


class Restaurants(ListView):
    model = Restaurant
    template_name = 'events/place_list.html'
    extra_context = {
        'last_pk' : Restaurant.objects.last().pk,
        'title' : 'Рестораны'
        }

class NonTypePlaces(ListView):
    model = NontypePlace
    template_name = 'events/place_list.html'
    extra_context = {
        'last_pk' : NontypePlace.objects.last().pk,
        'title' : 'Другие места'
        }

def nonTypePlacesDetailed(request,item_slug):
    context = {}
    item = NontypePlace.objects.get(slug__iexact=item_slug)
    schedule = Schedule.objects.filter(place__pk=item.pk)
    context['schedule'] = schedule
    follows = item.followers.count()
    if follows % 10 == 1:
        follows = '{} пользователя'.format(follows)
    else:
        follows = '{} пользователей'.format(follows)
    context['object'] = item
    context['follows'] = follows
    if request.method == 'POST':
        item.followers.add(request.user)
        return redirect(item.get_absolute_url())
    else:
        return render(request, 'events/nontype_showroom_detailed.html', context)

def concerthallDetailed(request,item_slug):
    context = {}
    item = СoncertHall.objects.get(slug__iexact=item_slug)
    schedule = Schedule.objects.filter(place__pk=item.pk)
    context['schedule'] = schedule
    follows = item.followers.count()
    if follows % 10 == 1:
        follows = '{} пользователя'.format(follows)
    else:
        follows = '{} пользователей'.format(follows)
    context['object'] = item
    context['follows'] = follows
    if request.method == 'POST':
        item.followers.add(request.user)
        return redirect(item.get_absolute_url())
    else:
        return render(request, 'events/concerthall_theatre_detailed.html', context)


class СoncertHalls(ListView):
    model = СoncertHall
    template_name = 'events/place_list.html'
    extra_context = {
        'last_pk' : СoncertHall.objects.last().pk,
        'title' : 'Концертные залы'
        }

def cinemaTheatreDetailed(request,item_slug):
    context = {}
    item = CinemaTheatre.objects.get(slug__iexact=item_slug)
    schedule = Schedule.objects.filter(place__pk=item.pk)
    context['schedule'] = schedule
    follows = item.followers.count()
    if follows % 10 == 1:
        follows = '{} пользователя'.format(follows)
    else:
        follows = '{} пользователей'.format(follows)
    context['object'] = item
    context['follows'] = follows
    if request.method == 'POST':
        item.followers.add(request.user)
        return redirect(item.get_absolute_url())
    else:
        return render(request, 'events/cinema_theatre_detailed.html', context)

class CinemaTheatres(ListView):
    model = CinemaTheatre
    template_name = 'events/place_list.html'
    extra_context = {
        'last_pk' : CinemaTheatre.objects.last().pk,
        'title' : 'Кинотеатры'
        }

def theatreDetailed(request,item_slug):
    context = {}
    item = Theatre.objects.get(slug__iexact=item_slug)
    schedule = Schedule.objects.filter(event__pk=item.pk)
    context['schedule'] = schedule
    follows = item.followers.count()
    if follows % 10 == 1:
        follows = '{} пользователя'.format(follows)
    else:
        follows = '{} пользователей'.format(follows)
    context['object'] = item
    context['follows'] = follows
    if request.method == 'POST':
        item.followers.add(request.user)
        return redirect(item.get_absolute_url())
    else:
        return render(request, 'events/concerthall_theatre_detailed.html', context)


class Theatres(ListView):
    model = Theatre
    template_name = 'events/place_list.html'
    extra_context = {
        'last_pk' : Theatre.objects.last().pk,
        'title' : 'Театры'
        }

def showroomsDetailed(request,item_slug):
    context = {}
    item = Showroom.objects.get(slug__iexact=item_slug)
    schedule = Schedule.objects.filter(place__pk=item.pk)
    context['scheule'] = schedule
    follows = item.followers.count()
    if follows % 10 == 1:
        follows = '{} пользователя'.format(follows)
    else:
        follows = '{} пользователей'.format(follows)
    context['object'] = item
    context['follows'] = follows
    if request.method == 'POST':
        item.followers.add(request.user)
        return redirect(item.get_absolute_url())
    else:
        return render(request, 'events/nontype_showroom_detailed.html', context)

class Showrooms(ListView):
    model = Showroom
    template_name = 'events/place_list.html'
    extra_context = {
        'last_pk' : Showroom.objects.last().pk,
        'title' : 'выставочные галереи'
        }

class Exhibitions(ListView):
    model = ExhibitionEvent
    template_name = 'events/event_list.html'
    extra_context = {
        'last_pk' : ExhibitionEvent.objects.last().pk,
        'title' : 'Выставки'
        }

class TheatreEvents(ListView):
    model = TheatreEvent
    template_name = 'events/event_list.html'
    extra_context = {
        'last_pk' : TheatreEvent.objects.last().pk,
        'title' : 'Театральные выступления'
        }

class SportEvents(ListView):
    model = SportEvent
    template_name = 'events/event_list.html'
    extra_context = {
        'last_pk' : SportEvent.objects.last().pk,
        'title' : 'Спортивные события'
        }

class Concerts(ListView):
    model = СoncertEvent
    template_name = 'events/event_list.html'
    extra_context = {
        'last_pk' : СoncertEvent.objects.last().pk,
        'title' : 'Концерты'
        }
        
class Films(ListView):
    model = FilmEvent
    template_name = 'events/event_list.html'
    extra_context = {
        'last_pk' : FilmEvent.objects.last().pk,
        'title' : 'Фильмы'
        }

class NonTypeEvents(ListView):
    model = NontypeEvent
    template_name = 'events/event_list.html'
    extra_context = {
        'last_pk' : NontypeEvent.objects.last().pk,
        'title' : 'Другие события'
        }

def nonTypeEventsDetailed(request,item_slug):
    context = {}
    item = NontypeEvent.objects.get(slug__iexact=item_slug)
    schedule = Schedule.objects.filter(event__pk=item.pk)
    context['schedule'] = schedule
    follows = item.followers.count()
    if follows % 10 == 1:
        follows = '{} пользователя'.format(follows)
    else:
        follows = '{} пользователей'.format(follows)
    context['object'] = item
    context['follows'] = follows
    if request.method == 'POST':
        item.followers.add(request.user)
        return redirect(item.get_absolute_url())
    else:
        return render(request, 'events/nonTypeEvents_detailed.html', context)

def exhibitionsDetailed(request,item_slug):
    context = {}
    item = ExhibitionEvent.objects.get(slug__iexact=item_slug)
    schedule = Schedule.objects.filter(event__pk=item.pk)
    context['schedule'] = schedule
    follows = item.followers.count()
    if follows % 10 == 1:
        follows = '{} пользователя'.format(follows)
    else:
        follows = '{} пользователей'.format(follows)
    context['object'] = item
    context['follows'] = follows
    if request.method == 'POST':
        item.followers.add(request.user)
        return redirect(item.get_absolute_url())
    else:
        return render(request, 'events/exhibition_Detailed.html', context)

def concerteDetailed(request,item_slug):
    context = {}
    item = СoncertEvent.objects.get(slug__iexact=item_slug)
    schedule = Schedule.objects.filter(event__pk=item.pk)
    context['schedule'] = schedule
    follows = item.followers.count()
    if follows % 10 == 1:
        follows = '{} пользователя'.format(follows)
    else:
        follows = '{} пользователей'.format(follows)
    context['object'] = item
    context['follows'] = follows
    if request.method == 'POST':
        item.followers.add(request.user)
        return redirect(item.get_absolute_url())
    else:
        return render(request, 'events/concert_Detailed.html', context)

def sportDetailed(request,item_slug):
    context = {}
    item = SportEvent.objects.get(slug__iexact=item_slug)
    schedule = Schedule.objects.filter(event__pk=item.pk)
    context['schedule'] = schedule
    follows = item.followers.count()
    if follows % 10 == 1:
        follows = '{} пользователя'.format(follows)
    else:
        follows = '{} пользователей'.format(follows)
    context['object'] = item
    context['follows'] = follows
    if request.method == 'POST':
        item.followers.add(request.user)
        return redirect(item.get_absolute_url())
    else:
        return render(request, 'events/sport_Detailed.html', context)

def theatreEventDetailed(request,item_slug):
    context = {}
    item = TheatreEvent.objects.get(slug__iexact=item_slug)
    schedule = Schedule.objects.filter(event__pk=item.pk)
    context['schedule'] = schedule
    follows = item.followers.count()
    if follows % 10 == 1:
        follows = '{} пользователя'.format(follows)
    else:
        follows = '{} пользователей'.format(follows)
    context['object'] = item
    context['follows'] = follows
    if request.method == 'POST':
        item.followers.add(request.user)
        return redirect(item.get_absolute_url())
    else:
        return render(request, 'events/theatre_event_Detailed.html', context)

def filmDetailed(request,item_slug):
    context = {}
    item = FilmEvent.objects.get(slug__iexact=item_slug)
    schedule = Schedule.objects.filter(event__pk=item.pk)
    context['schedule'] = schedule
    follows = item.followers.count()
    if follows % 10 == 1:
        follows = '{} пользователя'.format(follows)
    else:
        follows = '{} пользователей'.format(follows)
    context['object'] = item
    context['follows'] = follows
    if request.method == 'POST':
        item.followers.add(request.user)
        return redirect(item.get_absolute_url())
    else:
        return render(request, 'events/film_Detailed.html', context)