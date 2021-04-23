from django.shortcuts import render

from .models import Post
from .forms import PostForm

# Create your views here.


def view_blog(request):
    """ View blog page
    """
    form = PostForm()

    context = {
        'form': form
    }

    return render(request, 'blog/blog.html', context)
