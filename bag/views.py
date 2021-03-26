from django.shortcuts import render

# Create your views here.


def view_bag(request):
    """ View to display content of a users bag
    """
    return render(request, 'bag/bag.html')
