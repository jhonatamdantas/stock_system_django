from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpRequest, HttpResponse
from .forms import ProductForm
from .models import HardwareProduct

# Create your views here.
def home(request:HttpRequest):
    return render(request, 'home.html')

def register_product(request: HttpRequest):
    form = ProductForm()
    if request.method == "POST":
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    return render(request, 'register.html', {'form': form})


def update(request: HttpRequest, pk: int):
    product = get_object_or_404(HardwareProduct, id=pk)
    form = ProductForm(instance=product)

    if request.method == "POST":
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('edit')
    return render(request, 'update.html', {'form': form})


def edit(request: HttpRequest):
    products = HardwareProduct.objects.all()
    return render(request, 'edit.html', {'products': products})


def delete(request: HttpRequest, pk:int):
    product = get_object_or_404(HardwareProduct, id=pk)
    if request.method == "POST":
        product.delete()
        return redirect('edit')
    return render(request, 'edit.html', {'product': product})