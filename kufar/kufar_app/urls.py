from django.urls import path, include
from . import views
from django.conf.urls.static import static
from django.conf import settings
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register(r'phones', PhonesViewSet, basename='phones')
router.register(r'phone_images', PhoneImageViewSet, basename='phone_images')


urlpatterns = [
    path('api/', include(router.urls)),
    path('registration', views.registration, name = 'register'),
    path('login/', views.login_view, name = 'login'),
    path('logout/', views.logout_view, name = 'logout'),
    path('', views.home, name = 'home'),
    path('phones/', views.phones_page, name = 'phones'),
    path('tablets/', views.tablets_page, name = 'tablets'),
    path('cars/', views.cars_page, name = 'cars'),
    path('computers/', views.computers_page, name = 'computers'),
    path('user_page/<int:id>/', views.user_page, name = 'user_page'),
    path('add_phone_in_cart/<int:id>/', views.add_phone_in_cart, name='add_phone_in_cart'),
    path('add_tablet_in_cart/<int:id>/', views.add_tablet_in_cart, name='add_tablet_in_cart'),
    path('add_car_in_cart/<int:id>/', views.add_car_in_cart, name='add_car_in_cart'),
    path('add_computer_in_cart/<int:id>/', views.add_computer_in_cart, name='add_computer_in_cart'),
    path('delete_item_cart/<int:item_id>/', views.delete_item_cart, name='delete_item_cart'),
    path('cart/', views.cart_view, name = 'cart_view'),
    path('add_phone_announcement/<int:id>/', views.add_phone_announcement, name = 'add_phone_announcement'),
    path('add_tablet_announcement/<int:id>/', views.add_tablet_announcement, name = 'add_tablet_announcement'),
    path('add_car_announcement/<int:id>/', views.add_car_announcement, name = 'add_car_announcement'),
    path('add_computer_announcement/<int:id>/', views.add_computer_announcement, name = 'add_computer_announcement'),
    path('search/', views.search_results, name='search_results'),
]
    

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)