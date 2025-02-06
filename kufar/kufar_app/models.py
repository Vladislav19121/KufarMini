from django.db import models
from django.contrib.auth.models import User
from pathlib import Path
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType

BASE_DIR = Path(__file__).resolve().parent.parent

class Phone(models.Model):
    STATUS_CHOICES = [
        ('new', 'Новый'),
        ('used', 'Б/У'),
    ]
     
    name = models.CharField(max_length = 20)
    model = models.CharField(max_length = 100)
    status = models.CharField(max_length=4, choices=STATUS_CHOICES)
    description = models.TextField()
    price = models.FloatField()

    def __str__(self):
        return f"{self.name} {self.model} ({self.get_status_display()})"

class PhoneImage(models.Model):
    phone = models.ForeignKey(Phone, related_name='images', on_delete=models.CASCADE)
    images = models.ImageField(upload_to=f'{BASE_DIR}/media/phones/', null=True)

    def __str__(self):
        return f'Image for {self.phone.id} {self.phone.name} '

class Car(models.Model):
    STATUS_CHOICES = [
        ('new', 'Новый'),
        ('used', 'Б/У'),
    ]
     
    name = models.CharField(max_length = 20)
    model = models.CharField(max_length = 100)
    status = models.CharField(max_length=4, choices=STATUS_CHOICES)
    description = models.TextField()
    price = models.FloatField()

    def __str__(self):
        return f"{self.name} {self.model} ({self.get_status_display()})"

class CarImage(models.Model):
    car = models.ForeignKey(Car, related_name='images', on_delete=models.CASCADE)
    images = models.ImageField(upload_to=f'{BASE_DIR}/media/cars/', null=True)

    def __str__(self):
        return f'Image for {self.car.id} {self.car.name} '

class Tablet(models.Model):
    STATUS_CHOICES = [
        ('new', 'Новый'),
        ('used', 'Б/У'),
    ]
     
    name = models.CharField(max_length = 20)
    model = models.CharField(max_length = 100)
    status = models.CharField(max_length=4, choices=STATUS_CHOICES)
    description = models.TextField()
    price = models.FloatField()

    def __str__(self):
        return f"{self.name} {self.model} ({self.get_status_display()})"

class TabletImage(models.Model):
    tablet = models.ForeignKey(Tablet, related_name='images', on_delete=models.CASCADE)
    images = models.ImageField(upload_to=f'{BASE_DIR}/media/tablets/', null=True)

    def __str__(self):
        return f'Image for {self.tablet.id} {self.tablet.name} '
    
class Computer(models.Model):
    STATUS_CHOICES = [
        ('new', 'Новый'),
        ('used', 'Б/У'),
    ]
     
    name = models.CharField(max_length = 20)
    model = models.CharField(max_length = 100)
    status = models.CharField(max_length=4, choices=STATUS_CHOICES)
    description = models.TextField()
    price = models.FloatField()

    def __str__(self):
        return f"{self.name} {self.model} ({self.get_status_display()})"

class ComputerImage(models.Model):
    computer = models.ForeignKey(Computer, related_name='images', on_delete=models.CASCADE)
    images = models.ImageField(upload_to=f'{BASE_DIR}/media/computers/', null=True)

    def __str__(self):
        return f'Image for {self.computer.id} {self.computer.name} '
    
class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='carts')
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f'Cart for {self.user.username}'

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, related_name='items', on_delete=models.CASCADE)
    phone = models.ForeignKey(Phone, on_delete=models.CASCADE, null=True, blank=True, related_name='cart_items')
    tablet = models.ForeignKey(Tablet, on_delete=models.CASCADE, null=True, blank=True, related_name='cart_items')
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        if self.phone:
            return f'{self.quantity} of {self.phone.name} in cart'
        elif self.tablet:
            return f'{self.quantity} of {self.tablet.name} in cart'
        else:
            return f'{self.quantity} of unknown item in cart'
