from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from menu.models import Produk

def produk(request):
    produks = Produk.objects.all()
    context={
        'produks': produks,
    }
    produk = loader.get_template('produk.html')
    return HttpResponse(produk.render(context,request))


def home(request):
    home = loader.get_template('home.html')
    return HttpResponse(home.render())
