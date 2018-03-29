from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone
from ckeditor.fields import RichTextField

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
    about = models.CharField(max_length=1000, default='')
    slogan = models.CharField(max_length=500, default='')
    # *** BEGIN - Fields added for BuyUSA - TCG - 1/19/18 ***
    CompanyName = models.CharField(max_length=50, default='')
    CompanyCategory = models.CharField(max_length=3, choices=COMPANYCATEGORY_CHOICES, default='b2c')
    CompanyType = models.CharField(max_length=12, choices=COMPANYTYPE_CHOICES, default='manufacturer')
    CompanyLogo = models.FileField(upload_to='profile', default='')
    CompanyLink = models.CharField(max_length=50, default='')
    BBB = models.BooleanField(default=True)
    CompanyContactName = models.CharField(max_length=50, default='')
    CompanyContactPhone = models.CharField(max_length=50, default='')
    CompanyContactEmail = models.CharField(max_length=50, default='')
    CompanyJoined = models.DateTimeField(default=timezone.now)
    # *** END - Fields added for BuyUSA - TCG - 1/19/18 ***

    def __str__(self):
        return self.user.username
    
    
@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()


class Gig(models.Model):
    CATEGORY_CHOICES = {
        ("C1", "Category 1"),
        ("C2", "Category 2"),
        ("C3", "Category 3"),
        ("C4", "Category 4"),
        ("C5", "Category 5")
    }

    title = models.CharField(max_length=500)
    category = models.CharField(max_length=2, choices=CATEGORY_CHOICES, default='')
    description = RichTextField(max_length=1000, default='')
    BrandLogo = models.FileField(upload_to='gigs', default='')
    BrandLink = models.CharField(max_length=50, default='')
    BrandCustomerServicePhone = models.CharField(max_length=50, default='')
    BrandSearch = models.CharField(max_length=500, default='')
    BrandWhereToBuy = models.CharField(max_length=200, default='')
    # price = models.IntegerField(default=6)
    # photo = models.FileField(upload_to='gigs', default='')
    BrandPicture1 =  models.FileField(upload_to='gigs', default='')
    BrandPicture2 =  models.FileField(upload_to='gigs', default='')
    BrandPicture3 =  models.FileField(upload_to='gigs', default='')
    BrandPicture4 =  models.FileField(upload_to='gigs', default='')
    BrandPicture5 =  models.FileField(upload_to='gigs', default='')
    BrandPicture6 =  models.FileField(upload_to='gigs', default='') #　added by guolei 02/23/2017
    status = models.BooleanField(default=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    create_time = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

class Purchase(models.Model):
    gig = models.ForeignKey(Gig,on_delete=models.CASCADE)
    buyer = models.ForeignKey(User,on_delete=models.CASCADE)
    time = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.gig.title

class Review(models.Model):
    gig = models.ForeignKey(Gig,on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    content = models.CharField(max_length=500)

    def __str__(self):
        return self.content

