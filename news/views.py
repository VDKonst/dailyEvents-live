from django.urls import reverse_lazy
from .forms import *
from django.views.generic import CreateView, DetailView
from django.db.models import F
from django.shortcuts import redirect
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status, permissions
from .serializers import NewsSerializer
from rest_framework.decorators import api_view

class CreateNews(CreateView):
    form_class = NewsForm
    template_name = 'news/add_news.html'
    #success_url = reverse_lazy('index')

class ViewNews(DetailView):
    model = News
    slug_url_kwarg = 'item_slug'
    template_name = 'news/view_news.html'
    context_object_name = 'news'

def addLike(request,item_slug):
    news = News.objects.get(slug__exact=item_slug)
    if request.method == "POST":
        news.likes = F('likes') + 1
        news.save()
    return redirect('view_news',item_slug=item_slug)

def addDislike(request,item_slug):
    news = News.objects.get(slug__exact=item_slug)
    if request.method == "POST":
        news.dislikes= F('dislikes') + 1
        news.save()
    return redirect('view_news',item_slug=item_slug)

@api_view(['GET', 'POST', 'DELETE'])
def api_news_list(request):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    if request.method == 'GET':
        news = News.objects.all()
        headline = request.GET.get('headline', None)
        if headline is not None:
            news = news.filter(headline__icontains=headline)
        
        news_serializer = NewsSerializer(news, many=True)
        return JsonResponse(news_serializer.data, safe=False)
    elif request.method == 'POST':
        news_data = JSONParser().parse(request)
        news_serializer = NewsSerializer(data=news_data)
        if news_serializer.is_valid():
            news_serializer.save()
            return JsonResponse(news_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(news_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        _ = News.objects.all().delete()
        return JsonResponse({'message': '{} новостей было удалено'.format(_[0])}, status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'PUT', 'DELETE'])
def api_news_detail(request, pk):
    try: 
        news = News.objects.get(pk=pk) 
    except News.DoesNotExist: 
        return JsonResponse({'message': 'Такой новости не существует'}, status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET': 
        news_serializer = NewsSerializer(news) 
        return JsonResponse(news_serializer.data)
    elif request.method == 'PUT': 
        news_data = JSONParser().parse(request) 
        news_serializer = NewsSerializer(news, data=news_data) 
        if news_serializer.is_valid(): 
            news_serializer.save() 
            return JsonResponse(news_serializer.data) 
        return JsonResponse(news_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE': 
        news.delete() 
        return JsonResponse({'message': 'новость успешно удалена'}, status=status.HTTP_204_NO_CONTENT)
 

