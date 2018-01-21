from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
class Profile(models.Model):
    # *** BEGIN - Choices added for BuyUSA - TCG - 1/19/18***
    COMPANYCATEGORY_CHOICES = {
        ("b2b", "Business-to-Business"),
        ("b2c", "Business-to-Consumer")
    }

    COMPANYTYPE_CHOICES = {
        ("manufacturer", "Manufacturer"),
        ("wholesale", "Wholesale"),
        ("retail", "Retail"),
        ("service", "Service"),
        ("independent", "Independent")
    }
    # *** END - Choices added for BuyUSA - TCG - 1/19/18 ***

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.CharField(max_length=500)
    about = models.CharField(max_length=1000)
    slogan = models.CharField(max_length=500)
    # *** BEGIN - Fields added for BuyUSA - TCG - 1/19/18 ***
    CompanyName = models.CharField(max_length=50)
    CompanyCategory = models.CharField(max_length=3, choices=COMPANYCATEGORY_CHOICES)
    CompanyType = models.CharField(max_length=12, choices=COMPANYTYPE_CHOICES)
    CompanyLogo = models.FileField(upload_to='profile')
    CompanyLink = models.CharField(max_length=50)
    BBB = models.BooleanField(default=True)
    CompanyContactName = models.CharField(max_length=50)
    CompanyContactPhone = models.CharField(max_length=50)
    CompanyContactEmail = models.CharField(max_length=50)
    CompanyJoined = models.DateTimeField(default=timezone.now)
    # *** END - Fields added for BuyUSA - TCG - 1/19/18 ***

    def __str__(self):
        return self.user.username

class Gig(models.Model):
    CATEGORY_CHOICES = {
        ("C1", "Category 1"),
        ("C2", "Category 2"),
        ("C3", "Category 3"),
        ("C4", "Category 4"),
        ("C5", "Category 5")
    }

    title = models.CharField(max_length=500)
    category = models.CharField(max_length=2, choices=CATEGORY_CHOICES)
    description = models.CharField(max_length=1000)
    BrandLogo = models.FileField(upload_to='gig')
    BrandLink = models.CharField(max_length=50)
    BrandSearch = models.CharField(max_length=500)
    BrandWhereToBuy = models.CharField(max_length=200)
    price = models.IntegerField(default=6)
    photo = models.FileField(upload_to='gigs')
    BrandPicture2 =  models.FileField(upload_to='gigs')
    BrandPicture3 =  models.FileField(upload_to='gigs')
    BrandPicture4 =  models.FileField(upload_to='gigs')
    BrandPicture5 =  models.FileField(upload_to='gigs')
    status = models.BooleanField(default=True)
    user = models.ForeignKey(User)
    create_time = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

class Purchase(models.Model):
    gig = models.ForeignKey(Gig)
    buyer = models.ForeignKey(User)
    time = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.gig.title

class Review(models.Model):
    gig = models.ForeignKey(Gig)
    user = models.ForeignKey(User)
    content = models.CharField(max_length=500)

    def __str__(self):
        return self.content

