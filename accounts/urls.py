from django.urls import path
from .views import *


app_name = 'accounts'

urlpatterns = [
    path('', siteHome, name="sitehome")
    path('login/', Login, name= 'login' ),
    path('register/', Signup, name= 'register' ),
    path('logout', Logout, name= 'logout' ),
]