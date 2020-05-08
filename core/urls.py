from django.contrib.auth.views import logout_then_login
from django.urls import path, include

from core.views import CustomLoginView, register, ProfileView

urlpatterns = [
    path('', CustomLoginView.as_view(), name='login'),
    path('logout', logout_then_login, name='logout'),
    path('register', register, name='register'),
    path('profile', ProfileView.as_view(), name='profile'),
]
