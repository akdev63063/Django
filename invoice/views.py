from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def invoice_view(request):
    return HttpResponse("This is the invoice view.")

def invoice_list(request):
    return HttpResponse("This is the invoice list view.")

def home(request):
    return render(request, 'home.html')

def about(request):
    return HttpResponse("This is the about page.")

def contact(request):
    return HttpResponse("This is the contact page.")    

