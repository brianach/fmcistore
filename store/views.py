from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from django.db.models.functions import Lower

from .models import StoreItem, Category
from .forms import StoreItemForm
# Create your views here.


def all_storeitems(request):
    """ A view to return store page """

    store = StoreItem.objects.all()
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
                store = store.annotate(lower_name=Lower('name'))
            if sortkey == 'category':
                sortkey = 'category__name'

            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            store = store.order_by(sortkey)

        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            store = store.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(
                    request, "You didn't enter any search criteria!")
                return redirect(reverse('store'))

            queries = Q(name__icontains=query) | Q(
                description__icontains=query)
            store = store.filter(queries)

    current_sorting = f'{sort}_{direction}'

    current_category = request.GET.get('category', 'Store')

    context = {
        'store': store,
        'search_term': query,
        'current_categories': categories,
        'current_sorting': current_sorting,
        'current_category': current_category,
    }

    return render(request, 'store/store.html', context)


def storeitem_detail(request, storeitem_id):
    """ A view to show individual store details """

    storeitem = get_object_or_404(StoreItem, pk=storeitem_id)
    context = {
        'storeitem': storeitem,
    }

    return render(request, 'store/storeitem_detail.html', context)


def add_storeitem(request):
    """ Add a storeitem to the store """
    if request.method == 'POST':
        form = StoreItemForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully added storeitem!')
            return redirect(reverse('add_storeitem'))
        else:
            messages.error(request, 'Failed to add storeitem. Please ensure the form is valid.')
    else:
        form = StoreItemForm()
        
    template = 'store/add_storeitem.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


def edit_storeitem(request, storeitem_id):
    """ Edit a storeitem in the store """
    storeitem = get_object_or_404(StoreItem, pk=storeitem_id)
    if request.method == 'POST':
        form = StoreItemForm(request.POST, request.FILES, instance=storeitem)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated storeitem!')
            return redirect(reverse('storeitem_detail', args=[storeitem.id]))
        else:
            messages.error(request, 'Failed to update storeitem. Please ensure the form is valid.')
    else:
        form = StoreItemForm(instance=storeitem)
        messages.info(request, f'You are editing {storeitem.name}')

    template = 'store/edit_storeitem.html'
    context = {
        'form': form,
        'storeitem': storeitem,
    }

    return render(request, template, context)


def delete_storeitem(request, storeitem_id):
    """ Delete a storeitem from the store """
    storeitem = get_object_or_404(StoreItem, pk=storeitem_id)
    storeitem.delete()
    messages.success(request, 'Storeitem deleted!')
    return redirect(reverse('store'))