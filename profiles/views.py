from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import Profile
from .forms import ProfileForm

from checkout.models import Order


@login_required
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
        else:
            messages.error(
                request,
                'Update failed. Please check your form inputs.'
            )

    else:
        # Get saved user detailed
        form = ProfileForm(instance=profile)

    # Get all users orders
    orders = profile.orders.all()

    context = {
        'form': form,
        'orders': orders,
    }

    return render(request, 'profiles/profiles.html', context)


@login_required
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
