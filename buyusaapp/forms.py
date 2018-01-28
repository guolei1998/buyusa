from django.forms import ModelForm
from .models import Gig

class GigForm(ModelForm):
    class Meta:
        model = Gig
        # *** BEGIN - Update fields - TCG - 1/28/18 ***
        # fields = ['title', 'category', 'description', 'price', 'photo', 'status']
        fields = ['title', 'category', 'description', 'BrandLogo', 'BrandLink', 'BrandCustomerServicePhone', 'BrandSearch', 'BrandWhereToBuy', 'price', 'photo', 'BrandPicture2', 'BrandPicture3', 'BrandPicture4', 'BrandPicture5', 'status']