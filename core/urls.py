from django.urls import  path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about-us/', views.about, name='about'),
    path('contact-us/', views.contact, name='contact'),
    path('privacy-policy/', views.privacy_policy, name='privacy-policy'),
    path('terms-and-condition/', views.terms_and_condition, name='terms-and-condition'),
    path('faq/', views.faq, name='faq'),
    path('career/', views.career, name='career'),
    path('career-single/', views.career_single, name='career-single'),
]

handler404 = 'core.views.custom_404_view'