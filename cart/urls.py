from django.urls import path
from . import views
from rest_framework_simplejwt import views as jwt_views

urlpatterns = [
    # token
    path("cart/", views.CartModifierView.as_view()),
]
