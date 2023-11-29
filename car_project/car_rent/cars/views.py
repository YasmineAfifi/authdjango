from django.shortcuts import render
from .forms import CarForm
from .models import Car
from django.http import HttpResponse
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required

# Create your views here.

# display home page html 
def get_home_page(request):
     all_cars= Car.objects.all()
     return render(request ,'cars/home.html',{'cars':all_cars})

# add car function  
def add_car(request):
    if request.method == 'POST':
        car_data = CarForm(request.POST, request.FILES)
        # print(car_data.errors)
        if car_data.is_valid():
            car_data.save()
    else:
        car_data = CarForm()
        
    return render(request,'cars/addcar.html',{'carForm':car_data})

def get_details(request,car_id):
    try:

        car = Car.objects.get(id=car_id)
        return render(request,'cars/carDetails.html',{"details":car})
    
    except Car.DoesNotExist:

        return HttpResponse('Car does not exist')
    
    

# delete specific object
def delete_car(request,car_id):

    car = Car.objects.get(id=car_id)
    car.delete()
    return redirect('/home')

# update the form 
def update_car(request,car_id):

    car = Car.objects.get(id=car_id)

    if request.method =="POST":
        car_form = CarForm(request.POST,instance=car)
        if car_form.is_valid():
            car_form.save()
            return HttpResponse('updated')
    else:
        return render(request,"cars/updateCar.html",{'car':car})