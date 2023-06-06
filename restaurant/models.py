from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission


# Create your models here.


# the model for Category
class Category(models.Model):
    slug = models.SlugField()
    title = models.CharField(max_length=255, db_index=True)
    
    def __str__(self): 
        return self.title
    



# the model for Booking 
class Booking(models.Model):
    first_name = models.CharField(max_length=200)
    reservation_date = models.DateField()
    reservation_slot = models.SmallIntegerField(null=True, blank=True, default=10)
    
    def __str__(self): 
        return self.first_name

#  another version of the model for Booking 
''' class Booking(models.Model):
    table = models.ForeignKey('Table', on_delete=models.CASCADE)
    customer_name = models.CharField(max_length=100)
    customer_email = models.EmailField()
    booking_date = models.DateField()
    booking_time = models.TimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Booking #{self.id} - {self.customer_name}"  '''



# the model for Menu
class Menu(models.Model):
   name = models.CharField(max_length=200) 
   price = models.IntegerField(null=False) 
   menu_item_description = models.TextField(max_length=1000, default='') 

   def __str__(self):
      return self.name
  

#the model for MenuItem (idividual dish on the menu)
class MenuItem(models.Model):
    name = models.CharField(max_length=255, db_index=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2, db_index=True)
    image = models.ImageField(upload_to='menu_images/', blank=False, null=True)
    featured = models.BooleanField(db_index=True)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name
    
    



#the model for Table
class Table(models.Model):
    number = models.IntegerField(unique=True)
    #number = models.ImageField(unique=True)
    capacity = models.IntegerField()
    is_available = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"Table {self.number}"
    
          

class User(AbstractUser):
    groups = models.ManyToManyField(Group, related_name='auth_users')
    user_permissions = models.ManyToManyField(Permission, related_name='auth_users')

    # Add any additional fields you need for user authentication or profile information
    # For example:
    # age = models.IntegerField()
    # address = models.CharField(max_length=255)
    password = models.CharField(max_length=128)
    email = models.EmailField(blank=True, max_length=254)
    username = models.CharField(max_length=128, error_messages={'unique': 'A user with that username already exists.'})
    is_superuser = models.BooleanField(default=False)
    # If you don't need any additional fields, you can leave this model empty
    def __str__(self):
        return f"Username: {self.username}\nEmail: {self.email}"

  