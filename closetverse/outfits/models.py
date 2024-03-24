from django.db import models

class Shirt(models.Model):
    brand = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    sku = models.CharField(max_length=100, blank=True, null=True)  # optional
    size = models.CharField(max_length=10, blank=True, null=True)  # optional
    color = models.CharField(max_length=30, blank=True, null=True) # optional
    picture = models.ImageField(upload_to='images/', blank=True, null=True) # optional

    def __str__(self):
        return f"{self.brand} {self.name} {self.color}"

class Jacket(models.Model):
    brand = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    sku = models.CharField(max_length=100, blank=True, null=True)  # optional
    size = models.CharField(max_length=10, blank=True, null=True)  # optional
    color = models.CharField(max_length=30, blank=True, null=True) # optional
    picture = models.ImageField(upload_to='images/', blank=True, null=True) # optional

    def __str__(self):
        return f"{self.brand} {self.name} {self.color}"

class Pants(models.Model):
    brand = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    sku = models.CharField(max_length=100, blank=True, null=True)  # optional
    size = models.CharField(max_length=10, blank=True, null=True)  # optional
    color = models.CharField(max_length=30, blank=True, null=True) # optional
    picture = models.ImageField(upload_to='images/', blank=True, null=True) # optional

    def __str__(self):
        return f"{self.brand} {self.name} {self.color}"

class Shoes(models.Model):
    brand = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    sku = models.CharField(max_length=100, blank=True, null=True)  # optional
    size = models.CharField(max_length=10, blank=True, null=True)  # optional
    color = models.CharField(max_length=30, blank=True, null=True) # optional
    picture = models.ImageField(upload_to='images/', blank=True, null=True) # optional
    
    def __str__(self):
        return f"{self.brand} {self.name} {self.color}"
    

class Accessories(models.Model):
    brand = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    sku = models.CharField(max_length=100, blank=True, null=True)  # optional
    size = models.CharField(max_length=10, blank=True, null=True)  # optional
    color = models.CharField(max_length=30, blank=True, null=True) # optional
    picture = models.ImageField(upload_to='images/', blank=True, null=True) # optional

    def __str__(self):
        return f"{self.brand} {self.name} {self.color}"

# Model for Outfit
class Outfit(models.Model):
    shirt = models.ForeignKey(Shirt, on_delete=models.CASCADE)
    jacket = models.ForeignKey(Jacket, on_delete=models.CASCADE, blank=True, null=True)  # Jacket is optional
    pants = models.ForeignKey(Pants, on_delete=models.CASCADE)
    shoes = models.ForeignKey(Shoes, on_delete=models.CASCADE)
    accessories = models.ManyToManyField(Accessories, blank=True)  # Accessories are optional

    def __str__(self):
        return f"Outfit with {self.shirt}, {self.jacket}, {self.pants}, {self.shoes}, Accessories count: {self.accessories.count()}"