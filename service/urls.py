from django.urls import  path
from . import views
urlpatterns = [
    path('services/', views.service, name='services'),
    path('service-single/', views.service_single, name='service-single'),
]