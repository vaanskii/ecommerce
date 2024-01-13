from django.shortcuts import render, redirect, get_object_or_404
from .models import Cart, Item, CartItem
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from item.models import Category

@login_required
def view_cart(request):
    categories = Category.objects.all()
    try:
        cart = Cart.objects.get(user=request.user)
    except Cart.DoesNotExist:
        # Create a new cart for the user
        cart = Cart.objects.create(user=request.user)

    # Calculate the total price
    total_price = sum(cart_item.item.price * cart_item.quantity for cart_item in cart.cartitem_set.all())

    return render(request, 'cart/view_cart.html', {'cart': cart, 'categories': categories, 'total_price': total_price})


@login_required
def add_to_cart(request, item_id):
    item = Item.objects.get(id=item_id)

    # Get or create a cart for the user
    cart, created = Cart.objects.get_or_create(user=request.user)

    # Add the item to the cart
    cart_item, item_created = CartItem.objects.get_or_create(cart=cart, item=item)

    if not item_created:
        # Item already exists in the cart, increment the quantity
        cart_item.quantity += 1
        cart_item.save()
        messages.success(request, f"{item.name} quantity updated in your cart.")
    else:
        messages.success(request, f"{item.name} added to your cart.")

    return redirect('item:detail', item_id, )

@login_required
def update_cart(request, item_id):
    if request.method == 'POST':
        quantity = request.POST.get('quantity', 1)
        
        # Retrieve the user's cart
        try:
            cart = Cart.objects.get(user=request.user)
        except Cart.DoesNotExist:
            messages.error(request, 'Cart not found.')
            return redirect('cart:view_cart')

        # Update the cart item
        cart_item = CartItem.objects.get(cart=cart, item_id=item_id)
        cart_item.quantity = quantity
        cart_item.save()
        messages.success(request, 'Cart updated successfully.')
    
    # Redirect to the view_cart URL without passing categories as an argument
    return redirect('cart:view_cart')

@login_required
def delete_from_cart(request, item_id):
    if request.method == 'POST':
        # Retrieve the user's cart
        try:
            cart = Cart.objects.get(user=request.user)
        except Cart.DoesNotExist:
            messages.error(request, 'Cart not found.')
            return redirect('cart:view_cart')

        cart_item = get_object_or_404(CartItem, cart=cart, item_id=item_id)
        cart_item.delete()
        messages.success(request, 'Item removed from cart.')

    return redirect('cart:view_cart')
