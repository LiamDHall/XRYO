from django.shortcuts import render, get_object_or_404
from django.contrib import messages

from .models import Profile
from .forms import ProfileForm
from products.models import Category, Product

from checkout.models import Order


def profile(request):
    """ View to display a users profile.
    """

    # Get user profile
    profile = get_object_or_404(Profile, user=request.user)

    # POST / Save Form
    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile details saved')

    # Get saved user detailed
    form = ProfileForm(instance=profile)

    # Get all users orders
    orders = profile.orders.all()

    categories = Category.objects.all()
    products = Product.objects.all()

    context = {
        'form': form,
        'orders': orders,
        'categories': categories,
        'products': products,
    }

    return render(request, 'profiles/profiles.html', context)


def view_order_details(request, order_number):
    """ Takes user to checkout success page or the selected order they
    click in the their order history.
    """

    order = get_object_or_404(Order, order_number=order_number)

    messages.info(request, (
        f'Past confirmation for your order {order_number}. '
        'A confirmation email was sent on the order date.'
    ))

    context = {
        'order': order,
        'from_profile': True,
    }

    return render(request, 'checkout/checkout_success.html', context)
