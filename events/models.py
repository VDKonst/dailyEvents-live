from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.urls import reverse
from dailyEvents.utils import slugify
from account.models import Account, City


class Schedule(models.Model):
    date = models.DateTimeField()
    event = models.ForeignKey('Event', related_name='start_at', on_delete=models.CASCADE)
    place = models.ForeignKey('Place', on_delete=models.CASCADE)

    class Meta:
	    verbose_name = 'расписание'
	    verbose_name_plural = 'расписания'
	    ordering = ['date']


class Event(models.Model):
    name = models.CharField(max_length=100,verbose_name='название', unique=True)
    slug = models.SlugField(max_length=100, blank=True)
    followers = models.ManyToManyField(Account, related_name='followed_events',blank=True)
    photo = models.ImageField(upload_to='photos/events/%Y/%m/%d', verbose_name='фото', blank=True, default='default/event_pic.jpg')
    short_description = models.CharField(max_length=70)
    description = models.TextField()
    default_user = Account.objects.filter(is_admin=True).order_by('date_joined').first().pk
    organizer = models.ForeignKey(Account,blank=True, related_name='events', on_delete=models.CASCADE, default=default_user)
    rating = models.CharField(max_length=3, default='0+')
    schedule = models.ManyToManyField('Place',through=Schedule)
    comments = models.ManyToManyField(Account,through="EventComments")


    class Meta:
	    verbose_name = 'событие-родитель'
	    verbose_name_plural = 'события-родители'

    def __str__(self):
	    return self.name

    def save(self, *args, **kwargs):
	    self.slug = slugify(self.name)
	    super().save(*args,**kwargs)

class TheatreEvent(Event):
    author = models.CharField(max_length=50)
    artists = models.TextField()
    director = models.CharField(max_length=50)
    time = models.CharField(max_length=15)

    class Meta:
	    verbose_name = 'театральный спектакль'
	    verbose_name_plural = 'театральные спектакли'

    def __str__(self):
	    return self.name

    def get_absolute_url(self):
	    return reverse('theatre_event', kwargs={'item_slug':self.slug})

class SportEvent(Event):
    category = models.CharField(max_length =30)

    class Meta:
	    verbose_name = 'спортивное событие'
	    verbose_name_plural = 'спортивные события'

    def __str__(self):
	    return self.name

    def get_absolute_url(self):
	    return reverse('sport_event', kwargs={'item_slug':self.slug})

class СoncertEvent(Event):
    artist = models.CharField(max_length=50)
    time = models.CharField(max_length=15)

    class Meta:
	    verbose_name = 'концерт'
	    verbose_name_plural = 'концерты'

    def __str__(self):
	    return self.name

    def get_absolute_url(self):
	    return reverse('concert_event', kwargs={'item_slug':self.slug})

class ExhibitionEvent(Event):
    artists = models.TextField()
    category = models.CharField(max_length=30)

    class Meta:
	    verbose_name = 'выставка'
	    verbose_name_plural = 'выставки'

    def __str__(self):
	    return self.name

    def get_absolute_url(self):
	    return reverse('exhibition', kwargs={'item_slug':self.slug})

class FilmEvent(Event):
    author = models.CharField(max_length=50)
    artists = models.TextField()
    director = models.CharField(max_length=50)
    time = models.CharField(max_length=15)
    premier_date = models.DateField()
    country = models.CharField(max_length=50)

    class Meta:
	    verbose_name = 'фильм'
	    verbose_name_plural = 'фильмы'

    def __str__(self):
	    return self.name

    def get_absolute_url(self):
	    return reverse('film_event', kwargs={'item_slug':self.slug})

class NontypeEvent(Event):
    
    class Meta:
	    verbose_name = 'событие'
	    verbose_name_plural = 'события'

    def __str__(self):
	    return self.name

    def get_absolute_url(self):
	    return reverse('various-event', kwargs={'item_slug':self.slug})

class Place(models.Model):
    name = models.CharField(max_length=100,verbose_name='название', unique=True)
    slug = models.SlugField(max_length=100, blank=True)
    city = models.ForeignKey(City, related_name='places', on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='photos/place/%Y/%m/%d', verbose_name='фото', blank=True, default='default/place_pic.jpg')
    short_description = models.CharField(max_length=70,blank=True)
    description = models.TextField()
    default_user = Account.objects.filter(is_admin=True).order_by('date_joined').first().pk
    owner = models.ForeignKey(Account, related_name='places', on_delete=models.CASCADE, default=default_user)
    followers = models.ManyToManyField(Account,blank=True, related_name='liked_places')
    address = models.CharField(max_length=100)
    comments = models.ManyToManyField(Account,through="PlaceComments")

    class Meta:
	    verbose_name = 'место-родитель'
	    verbose_name_plural = 'места-родители'

    def __str__(self):
	    return self.name

    def save(self, *args, **kwargs):
	    self.slug = slugify(self.name)
	    super().save(*args,**kwargs)

class CinemaTheatre(Place):
    work_time = models.CharField(max_length=30)
    room_count = models.IntegerField()

    class Meta:
	    verbose_name = 'кинотеатр'
	    verbose_name_plural = 'кинотеатры'

    def __str__(self):
	    return self.name

    def get_absolute_url(self):
	    return reverse('cinema', kwargs={'item_slug':self.slug})

class Theatre(Place):
    work_time = models.CharField(max_length=30)
    seat_count = models.IntegerField()

    class Meta:
	    verbose_name = 'театр'
	    verbose_name_plural = 'театры'

    def __str__(self):
	    return self.name

    def get_absolute_url(self):
	    return reverse('theatre', kwargs={'item_slug':self.slug})

class Showroom(Place):
    work_time = models.CharField(max_length=30)
    
    class Meta:
	    verbose_name = 'выставочный зал'
	    verbose_name_plural = 'выставочные залы'

    def __str__(self):
	    return self.name

    def get_absolute_url(self):
	    return reverse('showroom', kwargs={'item_slug':self.slug})

class СoncertHall(Place):
    work_time = models.CharField(max_length=30)
    seat_count = models.IntegerField()

    class Meta:
	    verbose_name = 'концертный зал'
	    verbose_name_plural = 'концертные залы'

    def __str__(self):
	    return self.name

    def get_absolute_url(self):
	    return reverse('concert_hall', kwargs={'item_slug':self.slug})

class Restaurant(Place):
    work_time = models.CharField(max_length=30)
    table_count = models.IntegerField()
    cousine =  models.CharField(max_length=30)
    average_bill = models.IntegerField()
    category = models.CharField(max_length=40)

    class Meta:
	    verbose_name = 'ресторан'
	    verbose_name_plural = 'рестораны'

    def __str__(self):
	    return self.name

    def get_absolute_url(self):
	    return reverse('restaurant', kwargs={'item_slug':self.slug})

class NontypePlace(Place): 
    work_time = models.CharField(max_length=30, default='не предоставлено')

    class Meta:
	    verbose_name = 'место'
	    verbose_name_plural = 'места'

    def __str__(self):
	    return self.name

    def get_absolute_url(self):
	    return reverse('various-place', kwargs={'item_slug':self.slug})

class EventComments(models.Model):
    comment = models.TextField()
    date = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(Account, on_delete=models.CASCADE) 
    event = models.ForeignKey(Event, on_delete=models.CASCADE)

class PlaceComments(models.Model):
    comment = models.TextField()
    date = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(Account, on_delete=models.CASCADE) 
    place = models.ForeignKey(Place, on_delete=models.CASCADE)