from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.urls import reverse
from dailyEvents.utils import slugify
from django.contrib.auth.decorators import login_required, user_passes_test


class MyAccountManager(BaseUserManager):
	def create_user(self, email, username,  password=None):
		#sex=None, vk_url=None, about=None, send_mail=None,
		if not email:
			raise ValueError('Users must have an email address')
		if not username:
			raise ValueError('Users must have a username')

		user = self.model(
			email=self.normalize_email(email),
			username=username,
		)

		user.set_password(password)
		user.save(using=self._db)
		return user

	def create_superuser(self, email, username, password):
		#sex, vk_url, about, send_mail
		user = self.create_user(
			email=self.normalize_email(email),
			password=password,
			username=username,
		)
		user.is_admin = True
		user.is_superuser = True
		user.is_staff = True
		is_organizer = True
		is_owner = True
		user.save()
		return user


class Account(AbstractBaseUser):
	email = models.EmailField(verbose_name='email', max_length=60, unique=True)
	username = models.CharField(verbose_name='логин', max_length=40, unique=True)
	date_joined	= models.DateTimeField(verbose_name='дата регистрации', auto_now_add=True)
	last_login = models.DateTimeField(verbose_name='был в сети', auto_now=True)
	is_active = models.BooleanField(default=True)
	is_superuser = models.BooleanField(default=False)
	is_admin = models.BooleanField(default=False)
	is_staff = models.BooleanField(default=False)

	is_organizer = models.BooleanField(default=False)
	is_owner = models.BooleanField(default=False)
	choices = (
		('М',"мужской"),
		('Ж',"женский"),
	)
	sex = models.CharField(verbose_name='пол', max_length=10) 
	photo = models.ImageField(upload_to='photos/%Y/%m/%d', verbose_name='фото', blank=True, default='default/profile_pic.jpg')
	vk_url = models.URLField(blank=True)
	about = models.TextField(blank=True)
	send_mail = models.BooleanField(default=True)
	#events
	
	USERNAME_FIELD = 'email'
	REQUIRED_FIELDS = ['username',]

	objects = MyAccountManager()

	class Meta:
		verbose_name = 'пользователь'
		verbose_name_plural = 'пользователи'

	def check_if_owner(self):
		return self.is_owner

	rec_login_required = user_passes_test(lambda u: True if u.check_if_owner else False, login_url='/')
	
	def owner_login_required(self,view_func):
		decorated_view_func = login_required(rec_login_required(view_func), login_url='sign-in')
		return decorated_view_func

	def __str__(self):
		return self.email

	def has_perm(self, perm, obj=None):
		return self.is_admin

	def has_module_perms(self, perm, obj=None):
		return 1
	
	def has_perm_to_add_event(self, perm, obj=None):
		return self.is_organizer

	def has_perm_to_add_place(self, perm, obj=None):
		return self.is_owner

	def get_absolute_url(self):
		return reverse('account', kwargs={'user_id':self.pk})


class City(models.Model):
	name = models.CharField(max_length=100,verbose_name='название', unique=True)
	slug = models.SlugField(max_length=100, blank=True)

	class Meta:
		verbose_name = 'город'
		verbose_name_plural = 'города'
		ordering = ['name']

	def __str__(self):
		return self.name

	def save(self, *args, **kwargs):
		self.slug = slugify(self.name)
		super().save(*args,**kwargs)

	def get_absolute_url(self):
		return reverse('city', kwargs={'city_slug':self.slug})

class OwnerApplication(models.Model):
	place_name = models.CharField(max_length=100)
	description = models.TextField()
	owner = models.ForeignKey(Account,on_delete=models.CASCADE)

class OrgApplication(models.Model):
	event_name = models.CharField(max_length=100)
	description = models.TextField()
	owner = models.ForeignKey(Account,on_delete=models.CASCADE)












