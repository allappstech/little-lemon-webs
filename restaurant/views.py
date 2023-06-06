
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from djoser.views import UserViewSet as DjoserUserViewSet
from django.shortcuts import render, redirect
from .forms import BookingForm
from django.core import serializers
from .models import Category, Menu, MenuItem, Table, Booking, User
#from datetime import datetime
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseRedirect, JsonResponse
from rest_framework import permissions
from rest_framework.authentication import SessionAuthentication, TokenAuthentication

import json
from django.views.decorators.csrf import csrf_exempt
#from rest_framework import generics
from .serializers import (
    CategorySerializer, MenuSerializer, 
    MenuItemSerializer, TableSerializer, 
    BookingSerializer, UserSerializer)








# Create your views here.

# view for home
def home(request):
    return render(request, 'index.html')


# the view for about us
def about(request):
    return render(request, 'about.html')


# the view for Category
class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


# the view for menu
def menu(request):
    menu_data = Menu.objects.all()
    main_data = {"menu": menu_data}
    return render(request, 'menu.html', {"menu": main_data})

class MenuViewSet(viewsets.ModelViewSet):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer




class MenuItemViewSet(viewsets.ModelViewSet):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer


# the view for menuitem
class MenuItemsViewSet(viewsets.ModelViewSet):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
    search_fields = ['category__title']
    ordering_fields = ['price', 'inventory']

    def get_permissions(self):
        permission_classes = []
        if self.request.method != 'GET':
            permission_classes = [IsAuthenticated]

        return [permission() for permission in permission_classes]



# the for reservations
def reservations(request):
    bookings = Booking.objects.all()
    booking_json = serializers.serialize('json', bookings)
    data = [{'first_name': booking.first_name,
             'reservation_date': booking.reservation_date,
             'reservation_slot': booking.reservation_slot}
            for booking in bookings]
    return render(request, 'bookings.html', {'bookings': bookings, 'booking_json': booking_json, 'data': data})
    
    
    
# the view for book    
def book(request):
    form = BookingForm()
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            booking_data = {
                'first_name': form.cleaned_data['first_name'],
                'reservation_date': form.cleaned_data['reservation_date'].strftime('%Y-%m-%d'),
                'reservation_slot': form.cleaned_data['reservation_slot'],
            }
            response_data = {
                'success': True,
                'message': 'Booking submitted successfully.',
                'booking_data': booking_data,
            }
            return HttpResponse(json.dumps(response_data), content_type='application/json')
        else:
            form = BookingForm()
    context = {'form': form}
    return render(request, 'book.html', context)  



# the view for display 
def display_menu_item(request, pk=None): 
    if pk: 
        menu_item = Menu.objects.get(pk=pk) 
    else: 
        menu_item = "" 
    return render(request, 'menu_item.html', {"menu_item": menu_item}) 





@csrf_exempt
def bookings(request):
    def is_reservation_available(reservation_date, reservation_slot):
        existing_reservations = Booking.objects.filter(reservation_date=reservation_date, reservation_slot=reservation_slot)
        return not existing_reservations.exists()

    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            reservation_date = form.cleaned_data['reservation_date']
            reservation_slot = form.cleaned_data['reservation_slot']

            # Check if the reservation date and time are available
            if not is_reservation_available(reservation_date, reservation_slot):
                return HttpResponseBadRequest('Reservation is not available.')

            # Create a new reservation
            reservation = Booking(
                first_name=first_name,
                reservation_date=reservation_date,
                reservation_slot=reservation_slot,
            )
            reservation.save()

            # Redirect to the reservations page or a success page
            return HttpResponseRedirect('/reservations/')
    else:
        form = BookingForm()
    
    return render(request, 'book.html', {'form': form, 'bookings': bookings})
    #return render(request, 'bookings.html', {'bookings': bookings, 'booking_json': booking_json, 'data': data})
    



class TableViewSet(viewsets.ModelViewSet):
    queryset = Table.objects.all()
    serializer_class = TableSerializer



class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes_by_action = {
        'create': [permissions.AllowAny],  # Allow unauthenticated users to create (POST)
        'list': [permissions.AllowAny],    # Allow unauthenticated users to list (GET)
        'retrieve': [permissions.AllowAny], # Allow unauthenticated users to retrieve (GET)
        'update': [permissions.IsAuthenticated],  # Restrict update (PUT) to authenticated users
        'partial_update':[permissions.IsAuthenticated],  # Restrict partial update (PATCH) to authenticated users
        'destroy': [permissions.IsAuthenticated],  # Restrict destroy (DELETE) to authenticated users
    }
    
    def get_permissions(self):
        # Use different permission classes based on the action
        return [permission() for permission in self.permission_classes_by_action.get(self.action, self.permission_classes)]
        





class UserViewSet(DjoserUserViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


