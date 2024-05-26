from django.shortcuts import render
from .models import Service

# Create your views here.
def service(request):
    categories = Service.objects.all()
    context = {
        'categories': categories
    }
    return render(request, 'services.html', context)

def service_single(request):
    return render(request, 'service-single.html')