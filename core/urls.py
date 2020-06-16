from django.contrib.auth.views import logout_then_login
from django.urls import path, include

from core.views import CustomLoginView, register, ProfileView, PartnersListView
from products.views import list_donors

urlpatterns = [
    path('', CustomLoginView.as_view(), name='login'),
    path('logout', logout_then_login, name='logout'),
    path('register', register, name='register'),
    path('profile', ProfileView.as_view(), name='profile'),
    path('company/donors', list_donors, name='donors_list'),
    path('partners/', PartnersListView.as_view(), name='donors_list'),
]
