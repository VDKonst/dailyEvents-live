from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
from django.contrib.auth import login, authenticate,logout
from .forms import AuthForm, RegistrationForm, CityForm, EditAccForm, UploadImageForm, OwnerApplicationForm
from .models import Account, City, OwnerApplication
from django.contrib.auth.decorators import login_required
from django.views.generic import DetailView
from django.utils.decorators import method_decorator
from events.models import Place, Event, Schedule
from django.db.models import F
from news.models import News


def contacts(request):
    context = {}
    return render(request,"account/contacts.html",context)

def help(request):
    context = {}
    return render(request,"account/help.html",context)

def applicationSuccess(request):
    context = {}
    return render(request,"account/application_success.html",context)

def ownerApplicationView(request):
    context = {}
    if request.user.is_authenticated:
        user = request.user
    else:
        return redirect('index')
    form = OwnerApplicationForm
    if request.method == "POST":
        form = OwnerApplicationForm(request)
        if form.is_valid():
            place_name = request.cleaned_data['place_name']
            description = request.cleaned_data['description']
            application = OwnerApplication()
            application.place_name = place_name
            application.description = description
            application.user = user
            application.save()
        return redirect('application_success')
    else:
        form = OwnerApplicationForm()
        context['form']=form
        return render(request,"account/set_application.html",context)

def orgApplicationView(request):
    context = {}
    if request.user.is_authenticated:
        user = request.user
    else:
        return redirect('index')
    form = OwnerApplicationForm
    if request.method == "POST":
        form = OwnerApplicationForm(request)
        if form.is_valid():
            event_name = request.cleaned_data['place_name']
            description = request.cleaned_data['description']
            application = OwnerApplicationForm()
            application.place_name = event_name
            application.description = description
            application.user = user
            application.save()
        return redirect('application_success')
    else:
        form = OwnerApplicationForm()
        context['form']=form
        return render(request,"account/set_application.html",context)

def index(request):
    form = CityForm
    cities = City.objects.all()
    events = Event.objects.all()
    news = News.objects.order_by("-created_at")
    first_news = news[0]
    news = News.objects.order_by("-created_at")[1:4]
    context = {
        "cities":cities,
        "news":news,
        "first_news":first_news,
    }
    if request.method == 'GET':
        form = CityForm()
        context['form'] = form
        return render(request,'index.html',context)
    else:
        form = CityForm(request.POST)
        if form.is_valid():
            city_name = form.cleaned_data.get('city_name')
            city = City.objects.get(name__exact=city_name)
            return redirect(city.get_absolute_url())


@login_required(login_url='sign-in')
def logout_view(request):
    logout(request)
    return redirect('index')


def userRegister(request):
    if request.user.is_authenticated:
        return redirect('index')
    context = {}
    if request.method == 'POST':
        form = RegistrationForm(request.POST,request.FILES)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            username = form.cleaned_data.get('username')
            pswd = form.cleaned_data.get('password1')
            account = Account.objects.create_user(email = email,username = username,password=pswd)
            account.save()
            account = authenticate(email=email,password=pswd)
            login(request, account)
            account.sex = form.cleaned_data['sex']
            account.vk_url = form.cleaned_data['vk_url']
            account.about = form.cleaned_data['about']
            account.send_mail = form.cleaned_data['send_mail']
            if form.cleaned_data['photo'] != None:
                account.photo = form.cleaned_data['photo']
            account.save()
            return redirect('index')
        else:
            context['form'] = form
    else:
        form = RegistrationForm
        context['form'] = form
    return render(request, 'account/registration.html', context)

def userLogin(request):
    if request.user.is_authenticated:
        return redirect('index')
    context = {}
    if request.method == 'POST':
        form = AuthForm(request.POST)
        if form.is_valid():
            email = request.POST['email']
            pswd = request.POST['password']
            account = authenticate(email=email,password=pswd)
            if account:
                login(request, account)
                return redirect('index')    
        else:
            context['form'] = form
    else:
        form = AuthForm()
        context['form'] = form
    return render(request, 'account/login.html', context)


@method_decorator(login_required, name='dispatch')
class AccountViews(DetailView):
    model = Account
    pk_url_kwarg = 'user_id'
    template_name = 'account/account_page.html'

    def get_context_data(self, **kwargs):
        self.object = self.get_object()
        context = super().get_context_data(**kwargs)
        context['places'] = self.object.liked_places.all()
        context['events'] = self.object.followed_events.all()
        return context


@login_required(login_url='sign-in')
def edit_account(request,user_id):
    context = {}
    user = Account.objects.get(pk__iexact=int(user_id))
    if request.method == 'POST':
        form = EditAccForm(request.POST,request.FILES)
        if form.is_valid():
            user.vk_url = form.cleaned_data['vk_url']
            user.about = form.cleaned_data['about']
            user.send_mail = form.cleaned_data['send_mail']
            if form.cleaned_data['photo'] != '':
                user.photo = form.cleaned_data['photo']
            user.save()
            return redirect(user.get_absolute_url())
        else:
            context['form'] = form
    else:
        form = EditAccForm(vk_url=user.vk_url,about=user.about)
        context['form'] = form
    return render(request, 'account/edit_account_page.html', context)


def city_view(request,city_slug):
    city = City.objects.get(slug__iexact=city_slug)
    places = Place.objects.filter(city__name=city.name)
    place_names = places.values('name')
    schedule = Schedule.objects.filter(place__name__in=place_names)
    if schedule.count() == 0:
        title ='Для данного города информация не предоставлена.'
    else:
        title = 'Мероприятия и места города {}'.format(city.name)
    context = {
        'city':city,
        'schedule':schedule,
        'places':places,
        'title':title
    }
    return render(request, 'account/city.html', context)