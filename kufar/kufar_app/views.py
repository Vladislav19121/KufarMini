from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm
from rest_framework import viewsets
from .serializers import *
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from django.contrib.auth.decorators import login_required
from .forms import *
from django.http import HttpResponseBadRequest

class PhonesViewSet(viewsets.ModelViewSet):
    queryset = Phone.objects.all()
    serializer_class = PhonesSerializer
    permission_classes = [IsAuthenticated]
    
class PhoneImageViewSet(viewsets.ModelViewSet):
    queryset = PhoneImage.objects.all()
    serializer_class = PhoneImageSerializer
    permission_classes = [IsAuthenticated]




@csrf_exempt
def registration(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            if user:
                login(request, user)
                return redirect('home')
    else:
        form = UserCreationForm()
        
    
    return render(request, 'register.html', {'form': form})

@csrf_exempt
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user_log = authenticate(request, username=username, password=password)
        
        if user_log is not None:
            login(request, user_log)  
            return redirect('home')  
        else:
            error_message = "Неверное имя пользователя или пароль."
            return render(request, 'login.html', {'error': error_message})

    return render(request, 'login.html')   
 
@csrf_exempt            
def logout_view(request):
    logout(request)
    return redirect('home')

def home(request):
    return render(request, 'home.html')

def phones_page(request):
    phones = Phone.objects.all()
    images = PhoneImage.objects.all()
    
    return render(request, 'phone_page.html', {'phones': phones, 'images': images})

def tablets_page(request):
    tablets = Tablet.objects.all()
    images = TabletImage.objects.all()
    
    return render(request, 'tablet_page.html', {'tablets': tablets, 'images': images})

def computers_page(request):
    phones = Phone.objects.all()
    images = PhoneImage.objects.all()
    
    return render(request, 'phone_page.html', {'phones': phones, 'images': images})

def cars_page(request):
    cars = Car.objects.all()
    images = CarImage.objects.all()
    
    return render(request, 'car_page.html', {'cars': cars, 'images': images})

def user_page(request, id):
    user = get_object_or_404(User, id=id)
    return render(request, 'user_page.html')

@login_required
def add_phone_in_cart(request, id):
    phone = get_object_or_404(Phone, id=id)
    if request.method =='POST':
        cart, created = Cart.objects.get_or_create(user=request.user)
        cart_item, created = CartItem.objects.get_or_create(cart=cart, phone=phone)
        if not created:
            cart_item.quantity += 1
            cart_item.save()
            return redirect('cart_view')
        else:
            return redirect('cart_view')
    else:
        return HttpResponseBadRequest("Неверный метод запроса")

@login_required
def add_tablet_in_cart(request, id):
    tablet = get_object_or_404(Tablet, id=id)
    if request.method =='POST':
        cart, created = Cart.objects.get_or_create(user=request.user)
        cart_item, created = CartItem.objects.get_or_create(cart=cart, tablet=tablet)
        if not created:
            cart_item.quantity += 1
            cart_item.save()
            return redirect('cart_view')
        else:
            return redirect('cart_view')
    else:
        return HttpResponseBadRequest("Неверный метод запроса")
    
@login_required
def add_car_in_cart(request, id):
    car = get_object_or_404(Car, id=id)
    if request.method =='POST':
        cart, created = Cart.objects.get_or_create(user=request.user)
        cart_item, created = CartItem.objects.get_or_create(cart=cart, car=car)
        if not created:
            cart_item.quantity += 1
            cart_item.save()
            return redirect('cart_view')
        else:
            return redirect('cart_view')
    else:
        return HttpResponseBadRequest("Неверный метод запроса")

@login_required
def cart_view(request):
    try:
        cart = Cart.objects.get(user=request.user)
        cart_items = CartItem.objects.filter(cart=cart)
        total_price = 0  # Инициализируем total_price

        for item in cart_items:
            if item.phone:
                first_phone_image = PhoneImage.objects.filter(phone=item.phone).first()
                if first_phone_image:
                    item.first_image = first_phone_image.images.url
                else:
                    item.first_image = None
                total_price += item.phone.price * item.quantity # Обновляем total_price
            elif item.tablet:
                first_tablet_image = TabletImage.objects.filter(tablet=item.tablet).first()
                if first_tablet_image:
                    item.first_image = first_tablet_image.images.url
                else:
                    item.first_image = None
                total_price += item.tablet.price * item.quantity # Обновляем total_price
            else:
                item.first_image = None # Устанавливаем в None, если нет ни телефона, ни планшета

    except Cart.DoesNotExist:
        cart_items = []
        total_price = 0

    context = {
        'cart_items': cart_items,
        'total_price': total_price,
    }
    return render(request, 'cart_view.html', context)

def delete_item_cart(request, item_id):
    if request.method == 'POST':
        item = get_object_or_404(CartItem, id = item_id)
        if item:
            try:
                item.delete()
                return redirect('cart_view') 
            except CartItem.DoesNotExist:
                return f'Ошибка'

    


def add_phone_announcement(request, id):
    user = get_object_or_404(User, id=id)
    if request.method == 'POST':
        form = PhoneForm(request.POST, request.FILES)
        form_img = PhoneImageForm(request.POST, request.FILES)

        if form.is_valid() and form_img.is_valid():
            # Сохраняем данные из PhoneForm
            phone = form.save()

            # Получаем изображение из PhoneImageForm
            phone_image = form_img.save(commit=False)  # Не сохраняем сразу в БД
            phone_image.phone = phone  # Устанавливаем связь с телефоном
            phone_image.save()  # Теперь сохраняем изображение

            return redirect('phones')  # Или любой другой URL

    else:
        form = PhoneForm()
        form_img = PhoneImageForm()  # Создаем экземпляр класса, а не класс

    return render(request, 'add_phone_announcement.html', {'form': form, 'form_img': form_img})

def add_tablet_announcement(request, id):
    user = get_object_or_404(User, id=id)
    if request.method == 'POST':
        form = TabletForm(request.POST, request.FILES)
        form_img = TabletImageForm(request.POST, request.FILES)

        if form.is_valid() and form_img.is_valid():
            # Сохраняем данные из PhoneForm
            tablet = form.save()

            # Получаем изображение из PhoneImageForm
            tablet_image = form_img.save(commit=False)  # Не сохраняем сразу в БД
            tablet_image.tablet = tablet  # Устанавливаем связь с телефоном
            tablet_image.save()  # Теперь сохраняем изображение

            return redirect('tablets')  # Или любой другой URL

    else:
        form = TabletForm()
        form_img = TabletImageForm()  # Создаем экземпляр класса, а не класс

    return render(request, 'add_tablet_announcement.html', {'form': form, 'form_img': form_img})

def add_car_announcement(request, id):
    user = get_object_or_404(User, id=id)
    if request.method == 'POST':
        form = CarForm(request.POST, request.FILES)
        form_img = CarImageForm(request.POST, request.FILES)
        if form.is_valid() and form_img.is_valid():
            car = form.save()
            car_img = form_img.save(commit=False)
            car_img.car = car
            car_img.save()
            return redirect('cars')
    else:
        form = CarForm()
        form_img = CarImageForm()  # Создаем экземпляр класса, а не класс

    return render(request, 'add_car_announcement.html', {'form': form, 'form_img': form_img})



        