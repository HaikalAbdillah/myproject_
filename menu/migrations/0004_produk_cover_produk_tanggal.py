# Generated by Django 5.0 on 2024-01-02 09:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0003_kategori_produk_kategori_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='produk',
            name='cover',
            field=models.ImageField(null=True, upload_to='cover/'),
        ),
        migrations.AddField(
            model_name='produk',
            name='tanggal',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
