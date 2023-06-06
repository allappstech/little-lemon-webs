
from django.urls import path, include
#from djoser import views as djoser_views
from djoser.views import UserViewSet
from rest_framework.authtoken import views as authtoken_views
from rest_framework_simplejwt.views import TokenRefreshView
from . import views
from .views import UserViewSet
from rest_framework import routers
#from.views import Booking




router = routers.DefaultRouter()
router.register(r'categories', views.CategoryViewSet)
router.register(r'menuitems', views.MenuItemsViewSet)
router.register(r'menus', views.MenuViewSet)
router.register(r'tables', views.TableViewSet)
router.register(r'bookings', views.BookingViewSet)
router.register(r'users', views.UserViewSet)



urlpatterns = [
    
    path('', views.home, name="home"),
    path('bout/', views.about, name="about"),
    path('api/book/', views.book, name="book"),
    path('api/reservations/', views.reservations, name="reservations"),
    path('api/menu/', views.menu, name="menu"),
    path('menu_item/<int:pk>/', views.display_menu_item, name="menu_item"),  
    path('api/bookings/', views.bookings, name='bookings'), 
    
    #path('bookings/', bookings, name='bookings'),
    
    path('api/', include(router.urls)),
    
    # User Registration
    #path('api/auth/users/', UserViewSet.as_view({'post': 'create'}), name='user-create'),
    path('api/auth/registration/', UserViewSet.as_view({'post': 'create'}), name='user-create'),
    
    
    # API authentication and other URLs
    path('api/auth/', include('rest_framework.urls', namespace='rest_framework')),
    
    # Provides endpoints to obtain authentication token, refresh expired token, and verify the token's validity.
    path('api/auth/', include('djoser.urls.authtoken')),
    
    # Provides endpoints to obtain JWT token, refresh expired token, and verify the token's validity.
    path('api/auth/', include('djoser.urls.jwt')),
    
    # Used to obtain an authentication token, expects 'POST' request with valid user credentials (username and password) and returns an authentication token.
    path('api/auth/token/', authtoken_views.obtain_auth_token, name='token-obtain'),
    
    # Used to refresh an expired authentication token, expects 'POST' request with a valid refresh token and returns a new authentication token. 
    path('api/auth/token/refresh/', TokenRefreshView.as_view(), name='token-refresh'),
]