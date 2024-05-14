from django.shortcuts import render

# Create your views here.
def service(request):
    return render(request, 'services.html')

def service_single(request):
    return render(request, 'service-single.html')