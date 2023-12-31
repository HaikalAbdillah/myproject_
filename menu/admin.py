from django.contrib import admin
from menu.models import Produk, Kategori

# Register your models here.
class Parfum(admin.ModelAdmin):
    list_display = ('namaProduk', 'harga', 'kategori_id', 'perML')
    search_fields = ('namaProduk', 'harga', 'alco')
    list_filter = ('kategori_id',)
    list_per_page = 3

admin.site.register(Produk, Parfum)
admin.site.register(Kategori)
