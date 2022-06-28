from django.shortcuts import render, redirect, reverse, HttpResponse
from django.contrib import messages

from products.models import Product

# Create your views here.

def view_bag(request):
    """ A view that renders the bag contents page """

    return render(request, 'bag/bag.html')
    

def add_to_bag(request, item_id):
    """ Add a quantity of the specified product to the shopping bag """

    product = Product.objects.get(pk=item_id)
    quantity = int(request.POST.get('quantity'))
    
    redirect_url = request.POST.get('redirect_url')
    

    spicy = None
    if 'product_spicy' in request.POST:
        spicy = request.POST['product_spicy']
    bag = request.session.get('bag', {})

    if spicy:
        if item_id in list(bag.keys()):
            if spicy in bag[item_id]['spicy_level'].keys():
                bag[item_id]['spicy_level'][spicy] += quantity
                messages.success(request, f'Updated spicy level {spicy.upper()} {product.name} quantity to {bag[item_id]["spicy_level"][spicy]}')
            else:
                bag[item_id]['spicy_level'][spicy] = quantity
                messages.success(request, f'Added spicy {spicy.upper()} {product.name} to your bag')
        else:
            bag[item_id] = {'spicy_level': {spicy: quantity}}
            messages.success(request, f'Added spice {spicy.upper()} {product.name} to your bag')
    else:
        if item_id in list(bag.keys()):
            bag[item_id] += quantity
            messages.success(request, f'Updated {product.name} quantity to {bag[item_id]}')
        else:
            bag[item_id] = quantity
            messages.success(request, f'Added {product.name} to your bag')

    request.session['bag'] = bag

    return redirect(reverse('view_bag'))
    


def adjust_bag(request, item_id):
    """Adjust the quantity of the specified product to the specified amount"""

    quantity = int(request.POST.get('quantity'))
    spicy = None
    if 'product_spicy' in request.POST:
        spicy = request.POST['product_spicy']
    bag = request.session.get('bag', {})

    if spicy:
        if quantity > 0:
            bag[item_id]['spicy_level'][spicy] = quantity
        else:
            del bag[item_id]['spicy_level'][spicy]
            if not bag[item_id]['spicy_level']:
                bag.pop(item_id)
    else:
        if quantity > 0:
            bag[item_id] = quantity
        else:
            bag.pop(item_id)

    request.session['bag'] = bag
    return redirect(reverse('view_bag'))


def remove_from_bag(request, item_id):
    """Remove the item from the shopping bag"""

    try:
        spicy = None
        if 'product_spicy' in request.POST:
            spicy = request.POST['product_spicy']
        bag = request.session.get('bag', {})

        if spicy:
            del bag[item_id]['spicy_level'][spicy]
            if not bag[item_id]['spicy_level']:
                bag.pop(item_id)
        else:
            bag.pop(item_id)

        request.session['bag'] = bag
        return HttpResponse(status=200)

    except Exception as e:
        return HttpResponse(status=500)