from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from menu.models import Produk
from menu.forms import FormParfum
from django.contrib import messages

def hapus_p(request, id_produk):
    parfum = Produk.objects.filter(id=id_produk)
    parfum.delete()

    return redirect('produk')

def ubp(request, id_produk):
    parfum = Produk.objects.get(id=id_produk)
    template = 'ubp.html'
    if request.POST:
        form = FormParfum(request.POST, instance=parfum)
        if form.is_valid():
            form.save()
            messages.success(request, "Data berhasil disimpan")
            return redirect('ubp', id_produk=id_produk)
    else:
        form = FormParfum(instance=parfum)
        context={
            'form': form,
            'parfum': parfum,
        }
    return render(request, template, context)

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