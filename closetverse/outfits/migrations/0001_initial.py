# Generated by Django 5.0.1 on 2024-01-16 05:16

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Accessories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=100)),
                ('sku', models.CharField(blank=True, max_length=100, null=True)),
                ('size', models.CharField(blank=True, max_length=10, null=True)),
                ('color', models.CharField(blank=True, max_length=30, null=True)),
                ('picture', models.ImageField(blank=True, null=True, upload_to='images/')),
            ],
        ),
        migrations.CreateModel(
            name='Jacket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=100)),
                ('sku', models.CharField(blank=True, max_length=100, null=True)),
                ('size', models.CharField(blank=True, max_length=10, null=True)),
                ('color', models.CharField(blank=True, max_length=30, null=True)),
                ('picture', models.ImageField(blank=True, null=True, upload_to='images/')),
            ],
        ),
        migrations.CreateModel(
            name='Pants',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=100)),
                ('sku', models.CharField(blank=True, max_length=100, null=True)),
                ('size', models.CharField(blank=True, max_length=10, null=True)),
                ('color', models.CharField(blank=True, max_length=30, null=True)),
                ('picture', models.ImageField(blank=True, null=True, upload_to='images/')),
            ],
        ),
        migrations.CreateModel(
            name='Shirt',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=100)),
                ('sku', models.CharField(blank=True, max_length=100, null=True)),
                ('size', models.CharField(blank=True, max_length=10, null=True)),
                ('color', models.CharField(blank=True, max_length=30, null=True)),
                ('picture', models.ImageField(blank=True, null=True, upload_to='images/')),
            ],
        ),
        migrations.CreateModel(
            name='Shoes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=100)),
                ('sku', models.CharField(blank=True, max_length=100, null=True)),
                ('size', models.CharField(blank=True, max_length=10, null=True)),
                ('color', models.CharField(blank=True, max_length=30, null=True)),
                ('picture', models.ImageField(blank=True, null=True, upload_to='images/')),
            ],
        ),
        migrations.CreateModel(
            name='Outfit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('accessories', models.ManyToManyField(blank=True, to='outfits.accessories')),
                ('jacket', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='outfits.jacket')),
                ('pants', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='outfits.pants')),
                ('shirt', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='outfits.shirt')),
                ('shoes', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='outfits.shoes')),
            ],
        ),
    ]