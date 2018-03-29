from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Gig, Profile

class GigForm(ModelForm):
    class Meta:
        model = Gig
        # *** BEGIN - Update fields - TCG - 1/28/18 ***
        # fields = ['title', 'category', 'description', 'price', 'photo', 'status']
        fields = ['title', 'category', 'description', 'BrandLogo', 'BrandLink', 'BrandCustomerServicePhone', 'BrandSearch',
                  'BrandWhereToBuy', 'BrandPicture1', 'BrandPicture2', 'BrandPicture3', 'BrandPicture4', 'BrandPicture5', 
                  'BrandPicture6','status']
        
        

class SignUpForm(UserCreationForm):
    avatar = forms.ImageField()
    about = forms.CharField()
    slogan = forms.CharField()
    CompanyName = forms.CharField()
    CompanyCategory = forms.ChoiceField(choices=Profile.COMPANYCATEGORY_CHOICES)
    CompanyType = forms.ChoiceField(choices=Profile.COMPANYTYPE_CHOICES)
    CompanyLogo = forms.FileField()
    CompanyLink = forms.CharField()
    CompanyContactName = forms.CharField()
    CompanyContactPhone = forms.CharField()
    CompanyContactEmail = forms.CharField()

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2', )
