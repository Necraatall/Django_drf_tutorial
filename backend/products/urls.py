from django.urls import path

from . import views

# / means /api/products/
urlpatterns = [
    path('', views.product_alt_view),
    path('<int:pk>/', views.product_alt_view)
]
