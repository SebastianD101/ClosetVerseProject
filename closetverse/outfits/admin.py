from django.contrib import admin
from .models import Shirt, Pants, Shoes, Jacket, Accessories

# Register your models here
admin.site.register(Shirt)
admin.site.register(Pants)
admin.site.register(Shoes)
admin.site.register(Jacket)
admin.site.register(Accessories)
