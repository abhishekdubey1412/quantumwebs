from django.shortcuts import render
from .models import Faq

def home(request):
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')

def privacy_policy(request):
    return render(request,'privacy-policy.html')

def terms_and_condition(request):
    return render(request,'terms-and-condition.html')

def faqs(request):
    faqs_list = Faq.objects.all()
    return render(request, 'faqs.html', {'faqs': faqs_list})

def career(request):
    return render(request, 'career.html')

def career_single(request):
    return render(request, 'career-single.html')

def custom_404_view(request, exception):
    return render(request, '404.html', status=404)