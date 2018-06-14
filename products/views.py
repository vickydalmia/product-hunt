from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Product
from django.utils import timezone
# Create your views here.


def products(request):
    return render(request, 'home.html')


@login_required
def create(request):
    if request.method == 'POST':
        if request.POST['title'] and request.POST['body'] and request.POST['url'] and request.FILES['icon'] and request.FILES['image']:
            product_data = Product(
                title = request.POST['title'], 
                body = request.POST['body'], 
                url = request.POST['url'], 
                image = request.FILES['image'], 
                icon = request.FILES['icon'], 
                pub_date = timezone.datetime.now(), 
                hunter = request.user)
            product_data.save()
            return redirect('/products/'+ str(product_data.id))
        else:
            return render(request, 'products/createproduct.html', {'error': 'All Fields Are Required'})
    else:
        return render(request, 'products/createproduct.html')


def detail(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    return render(request, 'products/productdetail.html', {'product':product})


@login_required
def upvote(request, product_id):
    if request.method == 'POST':
        product = get_object_or_404(Product, pk=product_id)
        product.votes_total += 1
        product.save()
        return render(request, 'products/productdetail.html', {'product':product})


