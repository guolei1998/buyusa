from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.conf import settings

from .models import Gig, Profile, Purchase, Review
from .forms import GigForm, SignUpForm

import os
import braintree

braintree.Configuration.configure(braintree.Environment.Sandbox, merchant_id="7968vwncy9mkmwv6", public_key="5k6r27pfddhdx4wb", private_key="3a6cfa52f4b1d37475125a7a5b5117eb")

# Create your views here.
def home(request):
    gigs = Gig.objects.filter(status=True)
    return render(request, 'home.html', {"gigs": gigs})

def gig_detail(request, id):
    if request.method == 'POST' and \
        not request.user.is_anonymous() and \
        Purchase.objects.filter(gig_id=id, buyer=request.user).count() > 0 and \
        'content' in request.POST and \
        request.POST['content'].strip() != '':
        Review.objects.create(content=request.POST['content'], gig_id=id, user=request.user )
    try:
        gig = Gig.objects.get(id=id)
    except Gig.DoesNotExist:
        return redirect('/')
    
    if request.user.is_anonymous or \
        Purchase.objects.filter(gig=gig, buyer=request.user).count() == 0 or \
        Review.objects.filter(gig=gig, user=request.user).count() > 0:
        show_post_review = False
    else:
        show_post_review = Purchase.objects.filter(gig=gig, buyer=request.user).count() > 0
    reviews = Review.objects.filter(gig=gig)
    client_token = braintree.ClientToken.generate()
    return render(request, 'gig_detail.html', {"show_post_review": show_post_review, "reviews":reviews, "gig": gig, 
                                               "client_token": client_token , "MEDIA_URL" : settings.MEDIA_URL, })

@login_required(login_url="/")
def create_gig(request):
    error = ''
    if request.method == 'POST':
        gig_form = GigForm(request.POST, request.FILES)
        if gig_form.is_valid():
            gig = gig_form.save(commit=False)
            gig.user = request.user
            gig.save()
            return redirect('my_gigs')
        else:
            print(gig_form.errors)
            error = "Data is not valid"

    gig_form = GigForm()
    return render(request, 'create_gig.html', {"error": error, "gig_form":gig_form})

@login_required(login_url="/")
def edit_gig(request, id):
    try:
        gig = Gig.objects.get(id=id, user=request.user)
        error = ''
        if request.method == 'POST':
            gig_form = GigForm(request.POST, request.FILES, instance=gig)
            if gig_form.is_valid():
                gig.save()
                return redirect('my_gigs')
            else:
                error = "Data is not valid"
        gig_form = GigForm(instance=gig)
        return render(request, 'edit_gig.html', {"gig": gig, "error": error, "MEDIA_URL" : settings.MEDIA_URL, "gig_form":gig_form})
    except Gig.DoesNotExist:
        return redirect('/')

def my_gigs(request):
    gigs = Gig.objects.filter(user=request.user)
    return render(request, 'my_gigs.html', {"gigs": gigs})

@login_required(login_url="/")
def profile(request, username):
    if request.method == 'POST' :
        profile = Profile.objects.get(user=request.user)
        profile.about = request.POST['about']
        profile.slogan = request.POST['slogan']
        profile.save()
    else:
        try:
            profile = Profile.objects.get(user__username=username)
        except Profile.DoesNotExist:
            return redirect('/')

    gigs = Gig.objects.filter(user=profile.user, status=True)
    return render(request, 'profile.html', {"profile":profile, "gigs": gigs})


@login_required(login_url="/")
def create_purchase(request):
        if request.method == 'POST':
            try:
                gig = Gig.objects.get(id = request.POST['gig_id'])
            except Gig.DoesNotExist:
                return redirect('/')

            nonce = request. POST["payment_method_nonce"]
            result = braintree.Transaction.sale({
                "amount": gig.price,
                "payment_method_nonce": nonce
            })    

            if result.is_success:
                Purchase.objects.create(gig=gig, buyer=request.user)

        return redirect('/')

@login_required(login_url="/")
def my_sales(request):
    purchases = Purchase.objects.filter(gig__user=request.user)
    return render(request, 'my_sales.html', {"purchases": purchases})

@login_required(login_url="/")
def my_purchases(request):
    purchases = Purchase.objects.filter(buyer=request.user)
    return render(request, 'my_purchases.html', {"purchases": purchases})

def category(request, link):
    categories = {
        "category-1": "C1",
        "category-2": "C2",
        "category-3": "C3",
        "category-4": "C4",
        "category-5": "C5",
    }
    try:
        gigs = Gig.objects.filter(category=categories[link])
        return render(request, 'home.html', {"gigs": gigs})
    except KeyError:
        return redirect('home')


def search(request):
    gigs = Gig.objects.filter(title__contains=request.GET['title'])
    return render(request, 'home.html', {"gigs": gigs})


def file_save_to_media(photo,photoname='avatar'):

    fname =  photo.name
    if not os.path.exists(os.path.join(settings.MEDIA_ROOT,photoname)):
        os.mkdir(os.path.join(settings.MEDIA_ROOT,photoname))                 
    f = open(os.path.join(settings.MEDIA_ROOT,photoname, fname), 'wb+')
    for chunk in photo.chunks():
        f.write(chunk)
    f.close()
    return '%s%s/%s' % (settings.MEDIA_URL, photoname, fname)


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST,request.FILES)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()  # load the profile instance created by the signal
            for field in ['about','slogan','CompanyName','CompanyCategory',
                          'CompanyType','CompanyLogo','CompanyLink','CompanyContactName',
                          'CompanyContactPhone','CompanyContactEmail']:
                setattr(user.profile,field,form.cleaned_data.get(field))
            user.profile.avatar = file_save_to_media(form.cleaned_data.get('avatar'))
            user.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})
