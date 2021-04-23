from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import Post
from .forms import PostForm

# Create your views here.


def view_blog(request):
    """ View blog page and handles posting blog posts.
    """

    # Handles Post submission
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)

        # Save Post if form is valid
        if form.is_valid():
            form.save()
            messages.success(request, 'Blog Post Posted')

        # Send error maessage if form invalid
        else:
            messages.error(
                request,
                'Post failed to post. Please check your form inputs.'
            )
    else:
        form = PostForm()
    
    posts = Post.objects.all()

    context = {
        'form': form,
        'posts': posts,
    }

    return render(request, 'blog/blog.html', context)

@login_required
def delete_post(request, post_id):
    """ (SUPER USERS ONLY)
    Delete a Blog from the site
    """

    # Only allows superusers (Site Admins) to view this page.
    if not request.user.is_superuser:
        messages.error(request, 'Access Denied. Site Admins Only')
        return redirect(reverse('home'))

    # Get object
    post = get_object_or_404(Post, pk=post_id)

    # Delete object
    post.delete()

    current_page = request.POST.get('current_page')

    # Give user feedback and redirect
    messages.success(request, 'Post deleted')
    return redirect(current_page)
