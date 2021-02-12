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
from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from django.conf.urls.static import static
from django.conf import settings
from account import views as account_views
from events import views as events_views

urlpatterns = [
    path('api-auth/', include('rest_framework.urls')),
    path('admin/', admin.site.urls),
    path('events/', include('events.urls')),
    path('news/', include('news.urls')),
    path('help/', account_views.help, name='help'),
    path('contacts/', account_views.contacts, name='contacts'),
    path('', account_views.index, name='index'),
    path('sign-up/',account_views.userRegister,name='registration'),
    path('sign-in/',account_views.userLogin,name='login'),
    path('logout/',account_views.logout_view,name='logout'),
    path('city/<str:city_slug>/',account_views.city_view,name='city'),
    path('account/<int:user_id>/edit',account_views.edit_account,name='edit_account'),
    path('account/<int:user_id>/',account_views.AccountViews.as_view(),name='account'),
    path('application/owner',account_views.ownerApplicationView,name='owner'),
    path('application/org',account_views.orgApplicationView,name='org'),
    path('application/success',account_views.applicationSuccess,name='application_success'),
    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
