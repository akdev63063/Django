from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def invoice_view(request):
    return HttpResponse("This is the invoice view.")

def invoice_list(request):
    return HttpResponse("This is the invoice list view.")