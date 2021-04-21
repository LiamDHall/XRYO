from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from django.db import models
from django.db.models import Q

from PIL import Image
ImageTool = Image

from .models import Category, Product, Variant, Image, Review
from .forms import ProductForm, ReviewForm


def all_products(request):
    """ View to return and render all_products as well allow search,
    sorting and filtering
    """

    products = Product.objects.all()
    categories = None
    query = None
    sort = None
    direction = None

    if request.GET:
        if 'sort' in request.GET:
            sort_key = request.GET['sort']
            sort = sort_key
            if sort_key == 'name':
                sort_key = 'lower_name'
                products = products.annotate(lower_name=Lower('name'))

            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sort_key = f'-{sort_key}'
            products = products.order_by(sort_key)

        if 'category' in request.GET:
            cats = request.GET['category'].split(',')
            products = products.filter(category__name__in=cats)
            categories = Category.objects.filter(name__in=cats)

        if 'search-text' in request.GET:
            query = request.GET['search-text']
            print(query)
            if not query:
                messages.error(request, "Empty Search")
                return redirect(reverse('home'))

            queries = Q(name__icontains=query) | Q(description__icontains=query)
            products = products.filter(queries)

    selected_sorting = f'{sort}_{direction}'

    # No of Products
    no_of_products = 0

    if len(products) > 0:
        for product in products:
            if len(product.variant_set.all()) > 0:
                no_of_products += len(product.variant_set.all())
            else:
                no_of_products += 1

    context = {
        'products': products,
        'search_term': query,
        'no_of_products': no_of_products,
        'selected_catergory': categories,
        'selected_sorting': selected_sorting,
    }

    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """ A view to details of a single product
    """

    product = get_object_or_404(Product, pk=product_id)

    # Handles Reivew submission
    if request.method == 'POST':
        form = ReviewForm(request.POST, request.FILES)

        # Save Review if form is valid
        if form.is_valid():
            Review.objects.create(
                product=product,
                user_name=form.cleaned_data.get('user_name'),
                rating=form.cleaned_data.get('rating'),
                comment=form.cleaned_data.get('comment')
            )
            messages.success(request, 'Review Posted')

        # Send error maessage if form invalid
        else:
            messages.error(
                request,
                'Review failed to post. Please check your form inputs.'
            )
    else:
        form = ReviewForm()

    context = {
        'form': form,
        'product': product,
    }

    return render(request, 'products/product_detail.html', context)


def product_variant(request, product_id, variant_id):
    """ View the details of a single variant
    """

    product = get_object_or_404(Product, pk=product_id)
    variant = get_object_or_404(Variant, pk=variant_id)

    # Handles Review submission
    if request.method == 'POST':
        form = ReviewForm(request.POST, request.FILES)

        # Save Review if form is valid
        if form.is_valid():
            Review.objects.create(
                product=product,
                user_name=form.cleaned_data.get('user_name'),
                rating=form.cleaned_data.get('rating'),
                comment=form.cleaned_data.get('comment')
            )
            messages.success(request, 'Review Posted')

        # Send error maessage if form invalid
        else:
            messages.error(
                request,
                'Review failed to post. Please check your form inputs.'
            )
    else:
        form = ReviewForm()

    context = {
        'variant': variant,
        'product': product,
        'variant_id': variant.id,
        'form': form
    }

    return render(request, 'products/product_variant.html', context)


@login_required
def delete_review(request, review_id):
    """ (SUPER USERS ONLY)
    Edit a product
    """
    current_page = request.POST.get('current_page')

    # Only allows superusers (Site Admins) to view this page.
    if not request.user.is_superuser:
        messages.error(request, 'Access Denied. Site Admins Only')
        return redirect(reverse('home'))

    # Get object
    review = get_object_or_404(Review, pk=review_id)
    review_product = review.product.id

    # Delete object
    review.delete()

    # Give user feedback and redirect
    messages.success(request, 'Review deleted')
    return redirect('product_detail', product_id=review_product)


@login_required
def product_management(request):
    """ Renders product management page where site admin can
    edit add and delete products.
    """

    categories = Category.objects.all()
    products = Product.objects.all()

    context = {
        'categories': categories,
        'products': products,
    }

    return render(request, 'products/product_management.html', context)


@login_required
def add_product(request):
    """ (SUPER USERS ONLY)
    Add new product to site.
    """

    # Only allows superusers (Site Admins) to view this page.
    if not request.user.is_superuser:
        messages.error(request, 'Access Denied. Site Admins Only')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        product_name = form['name'].value()
        print(product_name)
        if form.is_valid():
            try:
                Product.objects.get(name=product_name)
                messages.error(
                    request,
                    f'Product with the name ({product_name}) already exists'
                )

            except Product.DoesNotExist:
                # Save new product
                new_product = form.save()

                # Add Product images
                # Check images are png or jpg / can be opened
                product_images = request.FILES.getlist('product-images')
                for image in product_images:
                    try:
                        # If image can be opened save image
                        open_image = ImageTool.open(image)
                        print(open_image.filename)

                        if open_image.format in {'PNG', 'JPG', 'JPEG'}:
                            Image.objects.create(
                                name=image,
                                album=new_product.album,
                                default=False,
                                image=image
                            )
                        else:
                            messages.error(
                                request,
                                f'Image ({image}) format is not supported'
                            )

                    except IOError:
                        messages.error(
                            request,
                            f'({image}) not upload properly. \
                            Check file is an image.'
                        )

                # Add Variant to database
                variant_count = int(request.POST.get('variant-count'))
                print(variant_count)

                for x in range(0, variant_count):
                    i = x + 1
                    name = request.POST.get(f'variant-name-{i}')
                    sku = request.POST.get(f'variant-sku-{i}')
                    var_images = request.FILES.getlist(f'variant-images-{i}')

                    new_variant = Variant.objects.create(
                        product=new_product,
                        name=name,
                        sku=sku,
                    )

                    # Add Variant Images to database
                    for image in var_images:
                        try:
                            # If image can be opened save image
                            open_image = ImageTool.open(image)
                            print(open_image.filename)

                            if open_image.format in {'PNG', 'JPG', 'JPEG'}:
                                Image.objects.create(
                                    name=image,
                                    album=new_variant.album,
                                    default=False,
                                    image=image
                                )
                            else:
                                messages.error(
                                    request,
                                    f'Image ({image}) format is not supported'
                                )

                        except IOError:
                            messages.error(
                                request,
                                f'({image}) not upload properly. \
                                Check file is an image.'
                            )

                messages.success(request, 'Product Added Successfully')
                return redirect(reverse('product_management'))
        else:
            messages.error(
                request,
                'Adding product failed. Please check your form inputs.'
            )
    else:
        form = ProductForm()

    context = {
        'form': form,
    }

    return render(request, 'products/add_product.html', context)


@login_required
def edit_product(request, product_id):
    """ (SUPER USERS ONLY)
    Edit a product
    """

    # Only allows superusers (Site Admins) to view this page.
    if not request.user.is_superuser:
        messages.error(request, 'Access Denied. Site Admins Only')
        return redirect(reverse('home'))

    # Get Product
    product = get_object_or_404(Product, pk=product_id)

    # Handles Form submission
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)

        # Save Product if form is valid and redurect back to product management
        if form.is_valid():
            form.save()
            messages.success(request, 'Product Updated')
            return redirect(reverse('product_management'))

        # Send error maessage if form invalid
        else:
            messages.error(request, 'Updating product failed. Please check your form inputs.')
    else:
        form = ProductForm(instance=product)
        messages.info(request, f'Warning you are editing {product.name}')

    context = {
        'form': form,
        'product': product,
    }

    return render(request, 'products/edit_product.html', context)


@login_required
def delete_product(request, product_id):
    """ (SUPER USERS ONLY)
    Delete a product from the site
    """

    # Only allows superusers (Site Admins) to view this page.
    if not request.user.is_superuser:
        messages.error(request, 'Access Denied. Site Admins Only')
        return redirect(reverse('home'))

    # Get object
    product = get_object_or_404(Product, pk=product_id)

    # Delete object
    product.delete()

    # Give user feedback and redirect
    messages.success(request, 'Product deleted')
    return redirect(reverse('product_management'))
