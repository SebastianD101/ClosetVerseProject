from django.shortcuts import render, redirect, get_object_or_404
from .forms import ShirtForm, JacketForm, PantsForm, ShoesForm, AccessoriesForm, OutfitForm
from .models import Shirt, Jacket, Pants, Shoes, Accessories, Outfit
from django.db.models import Q, Value
from django.db.models.functions import Concat


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
            form.save()
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
    shirt = get_object_or_404(Shirt, pk=pk)
    if request.method == 'POST':
        shirt.delete()
        return redirect('list_shirts')
    return render(request, 'delete_shirt.html', {'item': shirt, 'type': 'shirt'})

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
            form.save()
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
    jacket = get_object_or_404(Jacket, pk=pk)
    if request.method == 'POST':
        jacket.delete()
        return redirect('list_jackets')
    return render(request, 'delete_jacket.html', {'item': jacket, 'type': 'jacket'})

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
            form.save()
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
    pants = get_object_or_404(Pants, pk=pk)
    if request.method == 'POST':
        pants.delete()
        return redirect('list_pants')
    return render(request, 'delete_pants.html', {'item': pants, 'type': 'pants'})

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
            form.save()
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
    shoe = get_object_or_404(Shoes, pk=pk)
    if request.method == 'POST':
        shoe.delete()
        return redirect('list_shoes')
    return render(request, 'delete_shoes.html', {'item': shoe, 'type': 'shoes'})

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
            form.save()
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
    accessory = get_object_or_404(Accessories, pk=pk)
    if request.method == 'POST':
        accessory.delete()
        return redirect('list_accessories')
    return render(request, 'delete_accessories.html', {'item': accessory, 'type': 'accessories'})

# -------------------
# Outfit Views
# -------------------
def list_outfits(request):
    color_query = request.GET.get('color', '')

    # Query for outfits based on the selected color
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

    # Collect unique colors from all item models
    colors = list(set(Shirt.objects.values_list('color', flat=True)) |
                  set(Jacket.objects.values_list('color', flat=True)) |
                  set(Pants.objects.values_list('color', flat=True)) |
                  set(Shoes.objects.values_list('color', flat=True)) |
                  set(Accessories.objects.values_list('color', flat=True)))
    colors = [color for color in colors if color]  # Remove empty values
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
