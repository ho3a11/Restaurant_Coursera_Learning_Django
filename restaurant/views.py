from django.shortcuts import render,redirect
from . models import Booking,Menu
from . forms import BookingForm

# Create your views here.

def home(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def book(request):
    form = BookingForm()
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {'form':form}
    return render(request, 'book.html', context=context)

def menu(request):
    menu = Menu.objects.all().order_by('name')
    context = {'menu':menu}
    return render(request , 'menu.html' , context=context)
    

def menu_detail(request,pk=None):
    menu_item = Menu.objects.get(id=pk)
    context = {'menu_item':menu_item}
    return render(request, 'menu_item.html', context=context)


