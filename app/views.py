from django.shortcuts import render
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from app.models import Restaurant
from app.forms import RestaurantForm, RestaurantFormEdit
from django.urls import reverse

# Create your views here.

def index(req):
    return render(req, "index.html")

def restaurant(req):
    restaurant = Restaurant.objects.all()
    return render(req, "restaurants.html", {"restaurant" : restaurant})

def restaurant_details(req, restaurant_id):
    restourant = Restaurant.objects.get(id = restaurant_id)
    return HttpResponse(f"Restaurant details for restourant with id = {restaurant_id} <br> {restourant.name}")

def restaurant_add(req):
    if req.method == "POST":
        restaurant = RestaurantForm(req.POST)
        if (restaurant.is_valid()):
            restaurant.save()
            return HttpResponseRedirect(reverse("restaurants"))
    else:
        restaurant = RestaurantForm()

    return render(req, "restaurantFrom.html", {"form": restaurant})

def restaurant_delete(req, restaurant_id):
    restaurant = Restaurant.objects.get(id = restaurant_id)

    if (restaurant != None):
        restaurant.delete()

    return HttpResponseRedirect(reverse("restaurants"))

def restaurant_edit(request, restaurant_id):
    restaurant = Restaurant.objects.get(id=restaurant_id)
    if request.method == "POST":
        form = RestaurantFormEdit(request.POST, instance=restaurant)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('restaurants'))
    else:
        form = RestaurantFormEdit(instance=restaurant)

    return render(request, "restaurantFormEdit.html", {"form": form, "id": restaurant_id})