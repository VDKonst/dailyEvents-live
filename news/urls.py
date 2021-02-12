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
    path('add_news/',views.CreateNews.as_view(), name='add_news'),
    path('<str:item_slug>/',views.ViewNews.as_view(), name='view_news'),
    path('<str:item_slug>/add-like',views.addLike, name='add_like'),
    path('<str:item_slug>/add-dislike',views.addDislike, name='add_dislike'),
    url(r'^api/news$', views.api_news_list),
    url(r'^api/news/(?P<pk>[0-9]+)$', views.api_news_detail),
    
    ]