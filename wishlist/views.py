from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render

from profiles.models import UserProfile
from products.models import Product
from wishlist.models import Wishlist
# Create your views here.

@login_required
def wishlist(request):
    """ A view to return the wishlist page """

    user = get_object_or_404(UserProfile, user=request.user)
    wishlist= Wishlist.objects.filter(profile_user =user)

    template = 'wishlist/wishlist.html'

    context = {
        'wishlist': wishlist,
    }
    
    return render(request,template,context)

@login_required
def add_to_wishlist(request, product_id):
    user = get_object_or_404(UserProfile, user=request.user)
    product = get_object_or_404(Product, pk=product_id)

    Wishlist.objects.create(
        profile_user=user,
        product=product
    )
    messages.info(
        request, f'{product.name} has been added to your Wishlist!')

    return redirect(reverse('product_detail', args=[product.id]))



