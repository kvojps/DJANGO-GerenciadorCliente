from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'contas/dashboard.html')

def products(request):
    return render(request, 'contas/products.html')

def customer(request):
    return render(request, 'contas/customer.html')
