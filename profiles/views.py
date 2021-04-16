from django.shortcuts import render


def profile(request):
    """ View to display a users profile.
    """

    context = {

    }

    return render(request, 'profiles/profiles.html', context)
