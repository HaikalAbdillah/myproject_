from django.db import models

class Kategori(models.Model):
   nama = models.CharField(max_length=200)
   keterangan = models.TextField()

   def __str__(self):
       return f"{self.nama}"
   

class Produk(models.Model):
  namaProduk = models.CharField(max_length=255)
  harga = models.CharField(max_length=255)
  alco = models.CharField(max_length=200)
  perML = models.IntegerField(null=True)
  kategori_id = models.ForeignKey(Kategori, on_delete=models.CASCADE, null=True)

  def __str__(self):
      return f"{self.namaProduk} {self.harga} {self.alco} {self.perML}"
  
  