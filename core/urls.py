from django.urls import path, include
from core.views import CustomLoginView, RegisterView

urlpatterns = [
    path('', CustomLoginView.as_view()),
    path('register', RegisterView.as_view()),
]
