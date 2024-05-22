from service.models import Service
from django.contrib import messages
from .models import Faq, Contact, Subscribe, Review
from django.shortcuts import render, redirect
from django.core.validators import validate_email
from django.core.exceptions import ValidationError

def home(request):
    try:
        services = Service.objects.all()
        reviews = Review.objects.all()
    except Service.DoesNotExist:
        services = None
        reviews = None

    context = {
        'services': services,
        'reviews': reviews
    }
    
    return render(request, 'index.html', context)

def about(request):
    return render(request,'about.html')

def contact(request):
    if request.method == "POST":
        customer_name = request.POST.get('customer_name', '')
        email = request.POST.get('email', '')
        contact = request.POST.get('contact', '')
        company_name = request.POST.get('company_name', '')
        message = request.POST.get('message', '')

        # Create a new Contact object and save it to the database
        contact = Contact.objects.create(
            name=customer_name,
            email=email,
            phone=contact,
            company=company_name,
            message=message
        )

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

def subscribe(request):
    if request.method == "POST":
        email = request.POST.get('email')
        
        # Validate the email address
        try:
            validate_email(email)
        except ValidationError:
            messages.error(request, "Invalid email address.")
            return redirect('home')

        # Create a new subscription
        try:
            Subscribe.objects.create(email=email)
            messages.success(request, "Subscription successful.")
        except Exception as e:
            messages.error(request, f"An error occurred: {str(e)}")
            return redirect('home')
    
    return redirect('home')