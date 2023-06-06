
from rest_framework import serializers
#from django.contrib.auth.models import User
from .models import Category, Booking, Menu, MenuItem, Table, User




# serializers for the "Category" model
class CategorySerializer (serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['title', 'slug']




# serializers for the "Booking" model
class BookingSerializer (serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'




# serializers for the "Menu" model
class MenuSerializer (serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = '__all__'




# serializers for the "MenuItem" model

class MenuItemSerializer (serializers.ModelSerializer):
    class Meta:
        model = MenuItem
        fields = ['name', 'description', 'price', 'featured', 'category']



# serializers for the "Table" model

class TableSerializer (serializers.ModelSerializer):
    class Meta:
        model = Table
        fields = ['number', 'capacity', 'is_available']



# serializer for the User model
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['first_name', 'username', 'email']






'''
# Define serializers for the imported models
class TableSerializer(serializers.ModelSerializer):
    class Meta:
        model = Table
        fields = '__all__'  # Or specify the fields you want to include in the serialization

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'  # Or specify the fields you want to include in the serialization   '''