from .models import Order

from django.urls import reverse


def get_or_create_order(cart, request):
    
    order = cart.order

    if order is None and request.user.is_authenticated:
        order = Order.objects.create(cart=cart, user=request.user)

    if order:
        request.session['order_id'] = order.order_id

    return order
    

def breadcrumb(product=True, address=False, payment=False, confirmation=False):
    return [
        {'tittle': 'Produtos', 'active':product, 'url': reverse('orders:order')},
        {'tittle': 'direccion', 'active':address, 'url': reverse('orders:address')},
        {'tittle': 'pago', 'active':payment, 'url': reverse('orders:order')},
        {'tittle': 'confirmacion', 'active':confirmation, 'url': reverse('orders:order')},
    ]