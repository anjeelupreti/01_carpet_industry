from django.shortcuts import render

# Create your views here.
def homepage(request):
    return render(request, 'pages/homepage.html')

def contact_us(request):
    return render(request, 'pages/contact.html')

def about_us(request):
    return render(request, 'pages/about.html')

def products(request):
    return render(request, 'pages/products.html')

def product_detail(request):
    return render(request, 'pages/product_detail.html')

def gallery(request):
    return render(request, 'pages/gallery.html')

def manufacturing(request):
    return render(request, 'pages/manufacturing.html')

def history(request):
    return render(request, 'pages/history.html')