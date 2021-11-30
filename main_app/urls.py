from django.urls import path
from .views import Home, SignUp

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('accounts/signup/', SignUp.as_view(), name='signup'),
]