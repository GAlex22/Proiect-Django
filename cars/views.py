from django.shortcuts import render,get_object_or_404
from .models import Car


# Create your views here.
def index(request):
    new_cars = Car.objects.filter(category = 'New')[:9]
    used_cars = Car.objects.filter(category = 'Used')[:9]

    context ={
        'new_cars':new_cars,
        'used_cars':used_cars
    }
    return render(request, 'index.html', context)

def about(request):
    return render(request, 'about.html')

def car_detail(request,car_id):
    cars = get_object_or_404(Car, id=car_id)

    context = {
    'cars':cars
}
    return render(request,'car_detail.html',context)

def inventory(request):
    inventory_cars = Car.objects.all()

    context = {
        'inventory_cars':inventory_cars
    }
    return render(request,'inventory.html',context)

def contact(request):
    return render(request,'contact.html') 

