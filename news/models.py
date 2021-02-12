from django.db import models
from account.models import Account
from django.urls import reverse
from dailyEvents.utils import slugify


class News(models.Model):
    author = models.ForeignKey(Account, related_name='news', on_delete=models.CASCADE,null=True)
    headline = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, blank=True)
    text = models.TextField()
    likes = models.IntegerField(null=True,default=0)
    dislikes = models.IntegerField(null=True,default=0)
    photo = models.ImageField(upload_to='photos/news/%Y/%m/%d', verbose_name='фото', blank=True, default='default/event_pic.jpg')
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    categories = (
        ('фильмы', 'фильмы'),
        ('театр', 'театр'),
        ('концерты', 'концерты'),
    )
    category = models.CharField(max_length=100,choices=categories)

    class Meta:
	    verbose_name = 'новость'
	    verbose_name_plural = 'новости'

    def __str__(self):
	    return self.headline

    def save(self, *args, **kwargs):
	    self.slug = slugify(self.headline)
	    super().save(*args,**kwargs)

    def get_absolute_url(self):
	    return reverse('view_news', kwargs={'item_slug':self.slug})
