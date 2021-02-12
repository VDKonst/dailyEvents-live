from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Account, City, OwnerApplication
from django.contrib.auth import authenticate
from django.core.files.uploadedfile import SimpleUploadedFile
from django.contrib.auth.password_validation import validate_password
from django.shortcuts import get_object_or_404
from django.http import HttpResponseNotFound


class RegistrationForm(forms.Form):
    email = forms.EmailField(max_length=60, label='введите email *',widget=forms.EmailInput(
        attrs={
            'class':'input-xlarge',
            'placeholder':"email",
            }))
    username = forms.CharField(label='введите логин *', max_length=40, widget=forms.TextInput(
        attrs={
            'class':'input-xlarge',
            'placeholder':"логин",
            }))
    password1 = forms.CharField(label="введите Пароль *", widget=forms.PasswordInput(
        attrs={
            'class':'input-xlarge',
            'placeholder':"пароль",
            }))
    password2 = forms.CharField(label= "подтверждение пароля *", widget=forms.PasswordInput(
        attrs={
            'class':'input-xlarge',
            'placeholder':"пароль",
            }),
        help_text= "введенные пароли должны совпадать")
    sex = forms.ChoiceField(label='выберите ваш пол *',
        choices = (('мужчина',"мужчина"),('женщина',"женщина"),), 
        widget=forms.RadioSelect(
            attrs={
                'class':'form-check-input',
            }
    ) ) 
    photo = forms.ImageField( label='фото', required=False)
    vk_url = forms.URLField(label='ваша страница в социальных сетях', required=False,widget=forms.URLInput(
        attrs={
            'class':'input-xlarge',
        }
    ))
    about = forms.CharField(required=False, label='дополнительная информация', widget=forms.Textarea(
        attrs={
            'class':'input-xlarge',
            'placeholder':"дополнительная информация",
            'rows':'4',
            }))
    send_mail = forms.BooleanField(required=False, label='отправлять уведомления на почту',widget=forms.CheckboxInput())

    class Meta:
        model = Account
        fields = ('email', 'username','password1','password2')

    def clean_email(self, *args, **kwargs):
        email = self.cleaned_data['email']
        try:
            Account.objects.get(email=email)
            raise forms.ValidationError('пользователь с таким email существует')
        except Account.DoesNotExist:
            return email


    def clean_username(self, *args, **kwargs):
        username = self.cleaned_data['username']
        try:
            Account.objects.get(username=username)
            raise forms.ValidationError('пользователь с таким логином существует')
        except Account.DoesNotExist:
            return username

    def clean_password1(self, *args, **kwargs):
        pswd = self.cleaned_data.get('password1')
        if not validate_password(pswd):
            return pswd
    
    def clean_password2(self, *args, **kwargs):
        pswd = self.cleaned_data.get('password1')
        pswd1 = self.cleaned_data.get('password2')
        if pswd != pswd1:
            raise forms.ValidationError(
                "введенные пароли не совпадают"
            )
        else:
            return pswd1


class AuthForm(forms.ModelForm):
    email = forms.EmailField(max_length=60, label='введите email',widget=forms.EmailInput(
        attrs={
            'class':'input-xlarge',
            'placeholder':"email",
            }))
    password = forms.CharField(label="введите Пароль", widget=forms.PasswordInput(
        attrs={
            'class':'input-xlarge',
            'placeholder':"пароль",
            }))

    class Meta: 
        model = Account
        fields = ('email', 'password')

    def clean(self):
        if self.is_valid():
            print(self.cleaned_data)
            email = self.cleaned_data['email']
            pswd = self.cleaned_data['password']
            if not authenticate(email=email,password=pswd):
                raise forms.ValidationError('данные введены неверно')
        

class UploadImageForm(forms.Form):
    photo = forms.ImageField( label='фото', required=False)

class EditAccForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        vk_url = kwargs.pop('vk_url', None)
        about = kwargs.pop('about', None)
        super(EditAccForm,self).__init__(*args, **kwargs)
        self.fields["vk_url"].initial = vk_url
        self.fields["about"].initial = about

    photo = forms.ImageField( label='фото', required=False)
    vk_url = forms.URLField(label='ваша страница в социальных сетях', required=False,widget=forms.URLInput(
        attrs={
            'class':'input-xlarge',
        }
    ))
    about = forms.CharField(required=False, label='дополнительная информация', widget=forms.Textarea(
        attrs={
            'class':'input-xlarge',
            'placeholder':"дополнительная информация",
            'rows':'4',
            }))
    send_mail = forms.BooleanField(required=False, label='отправлять уведомления на почту',widget=forms.CheckboxInput())

    class Meta:
        model=Account
        fields= ['sex','vk_url','about',"send_mail"]

class CityForm(forms.Form):
    city_name= forms.CharField(widget=forms.TextInput(
        attrs={
            'class':'search-query span2',
            'placeholder':"выберите город",
             "list":"cities" ,
            }))
            

class OwnerApplicationForm(forms.ModelForm):
    class Meta:
        model = OwnerApplication
        fields = ['place_name','description',]
        widgets = {
            'place_name': forms.TextInput(attrs={'class':'input-xlarge',}),
            'description':forms.Textarea(attrs={'class':'input-xlarge','rows':"5",}),
            
        }
