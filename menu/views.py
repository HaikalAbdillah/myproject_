from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from menu.models import Produk
from menu.forms import FormParfum

def produk(request):
    produks = Produk.objects.filter(kategori_id__nama='eau de parfum')[:2]
    context={
        'produks': produks,
    }
    produk = loader.get_template('produk.html')
    return HttpResponse(produk.render(context,request))


def home(request):
    home = loader.get_template('home.html')
    return HttpResponse(home.render())


def t_parfum(request):
    if request.POST:
        form = FormParfum(request.POST)
        if form.is_valid():
            form.save()
            form = FormParfum()
            pesan = "Data berhasil disimpan"

            context={
                'form': form,
                'pesan': pesan,
            }
            return render(request, 't_parfum.html', context)
    else:
        form = FormParfum()
        context={
            'form': form,
        }
    t_parfum = loader.get_template('t_parfum.html')
    return HttpResponse(t_parfum.render(context,request))