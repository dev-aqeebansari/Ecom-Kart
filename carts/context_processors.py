from carts.views import _cart_id
from .models import Cart, CartItem


def counter(request):
    cart_count=0
    if 'admin' in request.path:
        return {}
    else:
        try:
            cart=Cart.objects.filter(cart_id =_cart_id(request))
            # print(cart)
            cart_items = CartItem.objects.all().filter(cart=cart[:1])

            for cart_item in cart_items:
                # print(cart_item.product.product_name)
                # print(cart_item.cart)
                cart_count=cart_count + cart_item.quantity
            # print(cart_count)
        except Cart.DoesNotExist:
            cart_count=0
    return dict(cart_count=cart_count)
