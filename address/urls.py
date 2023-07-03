from django.urls import path
from . import views
from rest_framework_simplejwt import views as jwt_views

urlpatterns = [
    path("address/:user_id", views.AddressView.as_view()),
]
