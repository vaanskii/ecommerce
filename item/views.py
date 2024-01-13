from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.db.models import Q

from .models import Item, Category
from .forms import NewItemForm, EditItemForm


def category_items(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    items = Item.objects.filter(category=category)
    categories = Category.objects.all()

    return render(request, 'item/category_items.html', {'category': category, 'items': items, 'categories': categories})

def items(request):

    query = request.GET.get('query', '')
    category_id = request.GET.get('category', 0)
    categories = Category.objects.all()
    items = Item.objects.filter(is_sold=False)

    if category_id:
        items = items.filter(category_id=category_id )

    if query:
        items = items.filter(Q(name__icontains=query) | Q(description__icontains=query))

    result_count = items.count()

    return render(request, 'item/items.html', {
        'items':items,
        'query':query,
        'categories':categories,
        'category_id': int(category_id),
        'result_count': result_count
    })

def detail(request, pk):
    item = get_object_or_404(Item, pk=pk)
    related_items = Item.objects.filter(category=item.category, is_sold=False).exclude(pk=pk)[:10]
    categories = Category.objects.all()

    return render(request, 'item/detail.html', {
        'item': item,
        'related_items': related_items,
        'categories' : categories,
    })


@login_required
def new(request):
    categories = Category.objects.all()
    if request.method == "POST":
        form = NewItemForm(request.POST, request.FILES)

        if form.is_valid():
            item = form.save(commit=False)
            item.created_by = request.user
            item.save()

            return redirect('item:detail', pk=item.id)
    else:
        form = NewItemForm()

    return render(request, 'item/form.html', {
        'form': form,
        'title': 'New Item | ',
        'categories' : categories,
    })


@login_required
def edit(request, pk):
    categories = Category.objects.all()
    item = get_object_or_404(Item, pk=pk, created_by=request.user)

    if request.method == "POST":
        form = EditItemForm(request.POST, request.FILES, instance=item)

        if form.is_valid():
            form.save()

            return redirect('item:detail', pk=item.id)
    else:
        form = EditItemForm(instance=item)

    return render(request, 'item/update-item.html', {
        'form': form,
        'title': 'Edit Item',
        'categories' : categories,
    })

@login_required
def delete(request, pk):
    item = get_object_or_404(Item, pk=pk, created_by=request.user)
    item.delete()

    return redirect('core:index')

@login_required
def user_items(request):
    categories = Category.objects.all()
    user_uploaded_items = Item.objects.filter(created_by=request.user)
    print("user_uploaded_items:", user_uploaded_items)

    if user_uploaded_items.exists():
        return render(request, 'item/user_items.html', {'user_uploaded_items': user_uploaded_items,'categories' : categories,})
    else:
        return render(request, 'item/user_items.html', {'categories' : categories,})