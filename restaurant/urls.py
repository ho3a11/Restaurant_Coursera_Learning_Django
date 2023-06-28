
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('book/', views.book, name='book'),
    path('menu/', views.menu, name='menu'),
    path('menu_item/<int:pk>/', views.menu_detail, name='menu_item'),
    path('api/bookings/', views.BookingList.as_view(), name='booking-list'),
    path('api/registration/', views.Registration.as_view(), name='registration'),






]
