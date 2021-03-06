from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from .models import Product, Category
from .forms import ProductForm
from django.db.models import Avg
from django.db.models import Q
from reviews.models import Reviews
from reviews.forms import ReviewForm
from profiles.models import UserProfile
from wishlist.models import Wishlist


def all_products(request):
    """ A view to show all products, including sorting and search queries """

    products = Product.objects.all()
    query = None
    categories = None
    sort = None
    direction = None

    if request.GET:

        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                products = products.annotate(lower_name=Lower('name'))
            if sortkey == 'category':
                sortkey = 'category__name'

            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            products = products.order_by(sortkey)

        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(
                    request, "You didn't enter any search criteria!")
                return redirect(reverse('products'))

            queries = Q(name__icontains=query) | Q(
                description__icontains=query)
            products = products.filter(queries)

    current_sorting = f'{sort}_{direction}'

    wishlist = None
    if request.user.is_authenticated:
        user = get_object_or_404(UserProfile, user=request.user)
        wishlist = Wishlist.objects.filter(profile_user=user)

    context = {
        'products': products,
        'search_term': query,
        'current_categories': categories,
        'current_sorting': current_sorting,
        'wishlist': wishlist,
    }

    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """ A view to show individual product details """

    product = get_object_or_404(Product, pk=product_id)
    reviews = Reviews.objects.all().filter(product=product)
    avg_rating = reviews.aggregate(Avg('rating'))['rating__avg']
    if avg_rating is not None:
        # round to the nearest 0.5 value
        avg_rating = round(avg_rating * 2) / 2

    if not request.user.is_authenticated:
        template = 'products/product_detail.html'

        context = {
            'product': product,
            'reviews': reviews,
            'avg_rating': avg_rating,
            }
        return render(request, template, context)
    else:
        product = get_object_or_404(Product, pk=product_id)
        profile_user = get_object_or_404(UserProfile, user=request.user)
        # find a match to the product and user
        wishlist = Wishlist.objects.filter(
                   profile_user=profile_user, product=product_id)

        form = ReviewForm()
        reviews = Reviews.objects.all().filter(product=product)
        avg_rating = reviews.aggregate(Avg('rating'))['rating__avg']
        product.rating = avg_rating

        template = 'products/product_detail.html'

        context = {
           'product': product,
           'profile_user': profile_user,
           'wishlist': wishlist,
           'form': form,
           'avg_rating': avg_rating,
        }

        return render(request, template, context)


@login_required
def add_product(request):
    """ Add a product to the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            messages.success(request, 'Successfully added product!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(
                request, 'Add product failed.Please ensure the form is valid.')
    else:
        form = ProductForm()

    template = 'products/add_product.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_product(request, product_id):
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))
    product = get_object_or_404(Product, pk=product_id)
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, "Product successfully updated")
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(
                request, 'Failed to update. Please ensure the form is valid.')
    else:
        form = ProductForm(instance=product)
        messages.info(request, f'You are editing {product.name}')

    template = 'products/edit_product.html'
    context = {
        'form': form,
        'product': product,
    }

    return render(request, template, context)


@login_required
def delete_product(request, product_id):
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    """ Delete a product from the store """
    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    messages.success(request, 'Product deleted!')
    return redirect(reverse('products'))


@login_required
def add_review(request, product_id):
    """
    A view to allow the user to add a review to a product
    """
    user = get_object_or_404(UserProfile, user=request.user)
    product = get_object_or_404(Product, pk=product_id)

    if request.user.is_authenticated:
        if request.method == 'POST':
            form = ReviewForm(request.POST)
            if form.is_valid():
                review = form.save(commit=False)
                review.product = product
                review.profile_user = user
                review.save()
                messages.info(request, 'Your review was successful')
                return redirect(reverse('product_detail', args=[product.id]))
            else:
                messages.error(
                    request, 'Failed to add your review')
    context = {
        'form': form,
    }

    return render(request, context)


@login_required
def edit_review(request, review_id):
    """
    A view to allow the users to edit their own review
    """

    review = get_object_or_404(Reviews, pk=review_id)
    product = review.product

    if request.method == 'POST':
        form = ReviewForm(request.POST, instance=review)
        if form.is_valid():
            form.save()
            messages.success(request, 'Review has been updated')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(
                request, 'Review edit failed, Please try again')

    else:
        form = ReviewForm(instance=review)

    messages.info(request, 'You are editing your review')
    template = 'products/product_detail.html'
    context = {
        'form': form,
        'review': review,
        'product': product,
        'edit': True,
    }
    return render(request, template, context)
