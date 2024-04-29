from django.conf import settings
from django.shortcuts import render, redirect, get_object_or_404
from .forms import ShirtForm, JacketForm, PantsForm, ShoesForm, AccessoriesForm, OutfitForm
from .models import Shirt, Jacket, Pants, Shoes, Accessories, Outfit
from django.db.models import Q, Value
from django.db.models.functions import Concat
from django.db import connection
import os
from django.http import Http404, HttpResponseRedirect
from django.urls import reverse


# Home page view
def index(request):
    return render(request, 'index.html')

# -------------------
# Shirt Views
# -------------------
def list_shirts(request):
    color = request.GET.get('color', '')
    if color:
        shirts = Shirt.objects.filter(color__iexact=color)
    else:
        shirts = Shirt.objects.all()

    colors = Shirt.objects.values_list('color', flat=True).distinct()
    return render(request, 'list_shirts.html', {'shirts': shirts, 'colors': colors})


def add_shirt(request):
    if request.method == 'POST':
        form = ShirtForm(request.POST, request.FILES)
        if form.is_valid():
            brand = form.cleaned_data['brand']
            name = form.cleaned_data['name']
            sku = form.cleaned_data.get('sku', '')
            size = form.cleaned_data.get('size', '')
            color = form.cleaned_data.get('color', '')
            picture = request.FILES.get('picture')
            
            picture_path = ''
            if picture:
                picture_path = os.path.join('shirts', picture.name)
                save_path = os.path.join(settings.MEDIA_ROOT, picture_path)
                
                os.makedirs(os.path.dirname(save_path), exist_ok=True)
                
                with open(save_path, 'wb+') as destination:
                    for chunk in picture.chunks():
                        destination.write(chunk)
            
            # Prepared SQL statement
            sql = """
            INSERT INTO outfits_shirt (brand, name, sku, size, color, picture)
            VALUES (%s, %s, %s, %s, %s, %s)
            """
            with connection.cursor() as cursor:
                cursor.execute(sql, [brand, name, sku, size, color, picture_path])
            
            return redirect('list_shirts')
    else:
        form = ShirtForm()

    return render(request, 'add_edit_shirt.html', {'form': form})

def edit_shirt(request, pk):
    shirt = get_object_or_404(Shirt, pk=pk)
    if request.method == 'POST':
        form = ShirtForm(request.POST, request.FILES, instance=shirt)
        if form.is_valid():
            form.save()
            return redirect('list_shirts')
    else:
        form = ShirtForm(instance=shirt)
    return render(request, 'add_edit_shirt.html', {'form': form, 'edit_mode': True, 'item_id': pk})

def delete_shirt(request, pk):
    sql_check = "SELECT id FROM outfits_shirt WHERE id = %s"
    with connection.cursor() as cursor:
        cursor.execute(sql_check, [pk])
        shirt = cursor.fetchone()
    
    if not shirt:
        raise Http404("Shirt not found.")

    if request.method == 'POST':
        # Prepared SQL statement
        sql_delete = "DELETE FROM outfits_shirt WHERE id = %s"
        with connection.cursor() as cursor:
            cursor.execute(sql_delete, [pk])
        return redirect('list_shirts')
    
    return render(request, 'delete_shirt.html', {'item': {'id': pk}, 'type': 'shirt'})

# -------------------
# Jacket Views
# -------------------
def list_jackets(request):
    color = request.GET.get('color', '')
    if color:
        jackets = Jacket.objects.filter(color__iexact=color)
    else:
        jackets = Jacket.objects.all()

    colors = Jacket.objects.values_list('color', flat=True).distinct()
    return render(request, 'list_jacket.html', {'jackets': jackets, 'colors': colors})

def add_jacket(request):
    if request.method == 'POST':
        form = JacketForm(request.POST, request.FILES)
        if form.is_valid():
            brand = form.cleaned_data['brand']
            name = form.cleaned_data['name']
            sku = form.cleaned_data.get('sku', None)
            size = form.cleaned_data.get('size', None)
            color = form.cleaned_data.get('color', None)
            picture = request.FILES.get('picture')
            
            picture_path = None
            if picture:
                picture_path = os.path.join('jackets', picture.name)
                save_path = os.path.join(settings.MEDIA_ROOT, picture_path)

                os.makedirs(os.path.dirname(save_path), exist_ok=True)
                
                with open(save_path, 'wb+') as destination:
                    for chunk in picture.chunks():
                        destination.write(chunk)
            
            # Prepared SQL statement
            sql = """
            INSERT INTO outfits_jacket (brand, name, sku, size, color, picture)
            VALUES (%s, %s, %s, %s, %s, %s)
            """
            with connection.cursor() as cursor:
                cursor.execute(sql, [brand, name, sku, size, color, picture_path])
            
            return redirect('list_jackets')
    else:
        form = JacketForm()

    return render(request, 'add_edit_jacket.html', {'form': form})

def edit_jacket(request, pk):
    jacket = get_object_or_404(Jacket, pk=pk)
    if request.method == 'POST':
        form = JacketForm(request.POST, request.FILES, instance=jacket)
        if form.is_valid():
            form.save()
            return redirect('list_jackets')
    else:
        form = JacketForm(instance=jacket)
    return render(request, 'add_edit_jacket.html', {'form': form, 'edit_mode': True, 'item_id': pk})

def delete_jacket(request, pk):
    sql_check = "SELECT id FROM outfits_jacket WHERE id = %s"
    with connection.cursor() as cursor:
        cursor.execute(sql_check, [pk])
        jacket = cursor.fetchone()
    
    if not jacket:
        raise Http404("Jacket not found.")

    if request.method == 'POST':
        # Prepared SQL statement
        sql_delete = "DELETE FROM outfits_jacket WHERE id = %s"
        with connection.cursor() as cursor:
            cursor.execute(sql_delete, [pk])
        return redirect('list_jackets')
    
    return render(request, 'delete_jacket.html', {'item': {'id': pk}, 'type': 'jacket'})

# -------------------
# Pants Views
# -------------------
def list_pants(request):
    color = request.GET.get('color', '')
    if color:
        pants = Pants.objects.filter(color__iexact=color)
    else:
        pants = Pants.objects.all()

    colors = Pants.objects.values_list('color', flat=True).distinct()
    return render(request, 'list_pants.html', {'pants': pants, 'colors': colors})

def add_pants(request):
    if request.method == 'POST':
        form = PantsForm(request.POST, request.FILES)
        if form.is_valid():
            brand = form.cleaned_data['brand']
            name = form.cleaned_data['name']
            sku = form.cleaned_data.get('sku', None)
            size = form.cleaned_data.get('size', None)
            color = form.cleaned_data.get('color', None)
            picture = request.FILES.get('picture')
            
            picture_path = None
            if picture:
                picture_path = os.path.join('pants', picture.name)
                save_path = os.path.join(settings.MEDIA_ROOT, picture_path)

                os.makedirs(os.path.dirname(save_path), exist_ok=True)

                with open(save_path, 'wb+') as destination:
                    for chunk in picture.chunks():
                        destination.write(chunk)
                
                picture_path = picture_path
            
            # Prepared SQL statement
            sql = """
            INSERT INTO outfits_pants (brand, name, sku, size, color, picture)
            VALUES (%s, %s, %s, %s, %s, %s)
            """
            with connection.cursor() as cursor:
                cursor.execute(sql, [brand, name, sku, size, color, picture_path])
            
            return redirect('list_pants')
    else:
        form = PantsForm()
    return render(request, 'add_edit_pants.html', {'form': form})

def edit_pants(request, pk):
    pants = get_object_or_404(Pants, pk=pk)
    if request.method == 'POST':
        form = PantsForm(request.POST, request.FILES, instance=pants)
        if form.is_valid():
            form.save()
            return redirect('list_pants')
    else:
        form = PantsForm(instance=pants)
    return render(request, 'add_edit_pants.html', {'form': form, 'edit_mode': True, 'item_id': pk})

def delete_pants(request, pk):
    sql_check = "SELECT id FROM outfits_pants WHERE id = %s"
    with connection.cursor() as cursor:
        cursor.execute(sql_check, [pk])
        pants = cursor.fetchone()
    
    if not pants:
        raise Http404("Pants not found.")

    if request.method == 'POST':
        # Use a prepared SQL statement to delete the pants
        sql_delete = "DELETE FROM outfits_pants WHERE id = %s"
        with connection.cursor() as cursor:
            cursor.execute(sql_delete, [pk])
        return redirect('list_pants')
    
    return render(request, 'delete_pants.html', {'item': {'id': pk}, 'type': 'pants'})

# -------------------
# Shoes Views
# -------------------
def list_shoes(request):
    color = request.GET.get('color', '')
    if color:
        shoes = Shoes.objects.filter(color__iexact=color)
    else:
        shoes = Shoes.objects.all()

    colors = Shoes.objects.values_list('color', flat=True).distinct()
    return render(request, 'list_shoes.html', {'shoes': shoes, 'colors': colors})

def add_shoes(request):
    if request.method == 'POST':
        form = ShoesForm(request.POST, request.FILES)
        if form.is_valid():
            brand = form.cleaned_data['brand']
            name = form.cleaned_data['name']
            sku = form.cleaned_data.get('sku', None)
            size = form.cleaned_data.get('size', None)
            color = form.cleaned_data.get('color', None)
            picture = request.FILES.get('picture')
            
            picture_path = None
            if picture:
                picture_path = os.path.join('shoes', picture.name)
                save_path = os.path.join(settings.MEDIA_ROOT, picture_path)
                
                os.makedirs(os.path.dirname(save_path), exist_ok=True)

                with open(save_path, 'wb+') as destination:
                    for chunk in picture.chunks():
                        destination.write(chunk)
                
                picture_path = picture_path
            
            # Prepared SQL statement
            sql = """
            INSERT INTO outfits_shoes (brand, name, sku, size, color, picture)
            VALUES (%s, %s, %s, %s, %s, %s)
            """
            with connection.cursor() as cursor:
                cursor.execute(sql, [brand, name, sku, size, color, picture_path])
            
            return redirect('list_shoes')
    else:
        form = ShoesForm()

    return render(request, 'add_edit_shoes.html', {'form': form})

def edit_shoes(request, pk):
    shoe = get_object_or_404(Shoes, pk=pk)
    if request.method == 'POST':
        form = ShoesForm(request.POST, request.FILES, instance=shoe)
        if form.is_valid():
            form.save()
            return redirect('list_shoes')
    else:
        form = ShoesForm(instance=shoe)
    return render(request, 'add_edit_shoes.html', {'form': form, 'edit_mode': True, 'item_id': pk})

def delete_shoes(request, pk):
    sql_check = "SELECT id FROM outfits_shoes WHERE id = %s"
    with connection.cursor() as cursor:
        cursor.execute(sql_check, [pk])
        shoe = cursor.fetchone()
    
    if not shoe:
        raise Http404("Shoes not found.")

    if request.method == 'POST':
        # Execute a prepared SQL statement to delete the shoes
        sql_delete = "DELETE FROM outfits_shoes WHERE id = %s"
        with connection.cursor() as cursor:
            cursor.execute(sql_delete, [pk])
        return redirect('list_shoes')

    return render(request, 'delete_shoes.html', {'item': {'id': pk}, 'type': 'shoes'})

# -------------------
# Accessories Views
# -------------------
def list_accessories(request):
    color = request.GET.get('color', '')
    if color:
        accessories = Accessories.objects.filter(color__iexact=color)
    else:
        accessories = Accessories.objects.all()

    colors = Accessories.objects.values_list('color', flat=True).distinct()
    return render(request, 'list_accessories.html', {'accessories': accessories, 'colors': colors})

def add_accessories(request):
    if request.method == 'POST':
        form = AccessoriesForm(request.POST, request.FILES)
        if form.is_valid():
            # Extract form data
            brand = form.cleaned_data['brand']
            name = form.cleaned_data['name']
            sku = form.cleaned_data.get('sku', None)
            size = form.cleaned_data.get('size', None)
            color = form.cleaned_data.get('color', None)
            picture = request.FILES.get('picture')
            
            picture_path = None
            if picture:
                picture_path = os.path.join('accessories', picture.name)
                save_path = os.path.join(settings.MEDIA_ROOT, picture_path)
                
                os.makedirs(os.path.dirname(save_path), exist_ok=True)
                
                with open(save_path, 'wb+') as destination:
                    for chunk in picture.chunks():
                        destination.write(chunk)
                
                picture_path = picture_path
            
            # Prepared SQL statement
            sql = """
            INSERT INTO outfits_accessories (brand, name, sku, size, color, picture)
            VALUES (%s, %s, %s, %s, %s, %s)
            """
            with connection.cursor() as cursor:
                cursor.execute(sql, [brand, name, sku, size, color, picture_path])
            
            return redirect('list_accessories')
    else:
        form = AccessoriesForm()

    return render(request, 'add_edit_accessories.html', {'form': form})

def edit_accessories(request, pk):
    accessory = get_object_or_404(Accessories, pk=pk)
    if request.method == 'POST':
        form = AccessoriesForm(request.POST, request.FILES, instance=accessory)
        if form.is_valid():
            form.save()
            return redirect('list_accessories')
    else:
        form = AccessoriesForm(instance=accessory)
    return render(request, 'add_edit_accessories.html', {'form': form, 'edit_mode': True, 'item_id': pk})

def delete_accessories(request, pk):
    sql_check = "SELECT id FROM outfits_accessories WHERE id = %s"
    with connection.cursor() as cursor:
        cursor.execute(sql_check, [pk])
        accessory = cursor.fetchone()
    
    if not accessory:
        raise Http404("Accessory not found.")

    if request.method == 'POST':
        # Execute a prepared SQL statement to delete the accessory
        sql_delete = "DELETE FROM outfits_accessories WHERE id = %s"
        with connection.cursor() as cursor:
            cursor.execute(sql_delete, [pk])
        return redirect('list_accessories')

    return render(request, 'delete_accessories.html', {'item': {'id': pk}, 'type': 'accessories'})

# -------------------
# Outfit Views
# -------------------
def list_outfits(request):
    color_query = request.GET.get('color', '')

    if color_query:
        outfits = Outfit.objects.filter(
            Q(shirt__color__iexact=color_query) |
            Q(jacket__color__iexact=color_query) |
            Q(pants__color__iexact=color_query) |
            Q(shoes__color__iexact=color_query) |
            Q(accessories__color__iexact=color_query)
        ).distinct()
    else:
        outfits = Outfit.objects.all()

    colors = list(set(Shirt.objects.values_list('color', flat=True)) |
                  set(Jacket.objects.values_list('color', flat=True)) |
                  set(Pants.objects.values_list('color', flat=True)) |
                  set(Shoes.objects.values_list('color', flat=True)) |
                  set(Accessories.objects.values_list('color', flat=True)))
    colors = [color for color in colors if color]
    colors.sort()

    return render(request, 'list_outfits.html', {'outfits': outfits, 'colors': colors, 'color_query': color_query})

def add_outfit(request):
    if request.method == 'POST':
        form = OutfitForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('list_outfits')
    else:
        form = OutfitForm()
    return render(request, 'add_edit_outfit.html', {'form': form})

def edit_outfit(request, pk):
    outfit = get_object_or_404(Outfit, pk=pk)
    if request.method == 'POST':
        form = OutfitForm(request.POST, request.FILES, instance=outfit)
        if form.is_valid():
            form.save()
            return redirect('list_outfits')
    else:
        form = OutfitForm(instance=outfit)
    return render(request, 'add_edit_outfit.html', {'form': form, 'edit_mode': True, 'item_id': pk})

def delete_outfit(request, pk):
    outfit = get_object_or_404(Outfit, pk=pk)
    if request.method == 'POST':
        outfit.delete()
        return redirect('list_outfits')
    return render(request, 'delete_outfit.html', {'item': outfit, 'type': 'outfit'})
