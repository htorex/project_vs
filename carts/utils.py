from .models import Carts

def get_or_create_cart(request):
    user = request.user if request.user.is_authenticated else None
    cart_id = request.session.get("cart_id")
    cart = Carts.objects.filter(cart_id=cart_id).first()

    if cart is None:
        cart = Carts.objects.create(user=user)

    if user and cart.user is None:
        cart.user = user
        cart.save()

    request.session['cart_id'] = cart.cart_id
        
    return cart