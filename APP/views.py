from django.shortcuts import render

from .models import Dress, Kids


# Create your views here.
def home(req):
    return render(req, 'home.html')


def about(req):
    return render(req, 'about.html')


def product(req):
    women = Dress.objects.all()
    return render(req, 'product.html', {'women': women})


def kids(req):
    kiddress = Kids.objects.all()
    return render(req, 'kids.html', {'kiddress': kiddress})


def location(req):
    return render(req, 'location.html')
