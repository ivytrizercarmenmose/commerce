from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .models import Clients







def index(request):
    data = Clients.objects.all()
    context = {"data": data}
    return render(request, "index.html", context)


def edit(request):
    return render(request, "about.html")


def login(request):
    return render(request, "contact.html")


def signup(request):
    return render(request, "staff.html")


def Bookings(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        age = request.POST.get('age')
        gender = request.POST.get('gender')
        query = Clients(name=name, email=email, age=age, gender=gender,  city=city)
        query.save()
        return redirect("/")

        return render(request, "index.html")


def deleteData(request, id):
    d = Clients.objects.get(id=id)
    d.delete()
    return redirect("/")
    return render(request="index.html")


def updateData(request, id):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        age = request.POST.get('age')
        gender = request.POST.get('gender')
        country = request.POST.get('country')
        city = request.POST.get('city')

        update_Info = Clients.objects.get(id=id)
        update_Info.name = name
        update_Info.email = email
        update_Info.age = age
        update_Info.gender = gender
        update_Info.country = country
        update_Info.city = city

        update_Info.save()
        return redirect("/")
    d = Clients.objects.get(id=id)
    context = {"d": d}
    return render(request, "edit.html",context)
