from django.shortcuts import render, get_object_or_404
from django.contrib import messages

from .models import Profile
from .forms import ProfileForm


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

    context = {
        'form': form,
        'orders': orders,
    }

    return render(request, 'profiles/profiles.html', context)
