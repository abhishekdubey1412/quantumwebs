from django.urls import  path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about-us/', views.about, name='about'),
    path('contact-us/', views.contact, name='contact'),
    path('privacy-policy/', views.privacy_policy, name='privacy-policy'),
    path('terms-and-condition/', views.terms_and_condition, name='terms-and-condition'),
    path('faqs/', views.faqs, name='faqs'),
    path('career/', views.career, name='career'),
    path('career-single/', views.career_single, name='career-single'),
    path('subscribe/', views.subscribe, name="subscribe")
]

handler404 = 'core.views.custom_404_view'