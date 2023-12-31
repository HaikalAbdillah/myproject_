# Generated by Django 5.0 on 2023-12-31 04:48

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0002_produk_perml'),
    ]

    operations = [
        migrations.CreateModel(
            name='Kategori',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=200)),
                ('keterangan', models.TextField()),
            ],
        ),
        migrations.AddField(
            model_name='produk',
            name='kategori_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='menu.kategori'),
        ),
    ]
