from django.urls import path
from . import views


urlpatterns = [
    path("orders/", views.OrderViews.as_view()),
    path("orders/<int:pk>/", views.OrderDetailsViews.as_view()),
    path("orders/seller/", views.OrderSellerViews.as_view()),
]
