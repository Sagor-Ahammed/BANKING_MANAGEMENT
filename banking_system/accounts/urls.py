from django.urls import path
from .views import UserRegistrationView,UserloginView,LogoutView

app_name = 'accounts'
urlpatterns = [
 path('login/',UserloginView.as_view(),name='user_login'),
    path('logout/',LogoutView.as_view(),name='user_logout'),
    path('register/',UserRegistrationView.as_view(),name='user_registration'), 
]
