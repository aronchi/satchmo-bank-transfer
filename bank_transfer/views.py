"""Simple wrapper for standard checkout as implemented in satchmo.payment.views"""

from livesettings import config_get_group
from payment.views import confirm, payship
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.utils.translation import ugettext as _
from satchmo_utils.views import bad_or_missing
from satchmo_store.shop.models import Order

payment_module = config_get_group('PAYMENT_BANK_TRANSFER')    
#bank_transfer = config_get_group('PAYMENT_BANK_TRANSFER')

def simple_pay_ship_info(request, template):
    """A pay_ship view which doesn't require a credit card."""
    return payship.base_pay_ship_info(request, payment_module, payship.simple_pay_ship_process_form, template)
    
def pay_ship_info(request):
    return payship.base_pay_ship_info(request, payment_module, payship.simple_pay_ship_process_form,'checkout/bank_transfer/pay_ship.html')
    

def confirm_info(request):
    return confirm.credit_confirm_info(request, payment_module, template='checkout/bank_transfer/confirm.html')

def success(request):
    """
    The order has been succesfully processed.  This can be used to generate a receipt or some other confirmation
    """
    try:
        order = Order.objects.from_request(request)
    except Order.DoesNotExist:
        return bad_or_missing(request, _('Your order has already been processed.'))
    
    # Added to track total sold for each product
    for item in order.orderitem_set.all():
        product = item.product
        product.total_sold += item.quantity
        product.items_in_stock -= item.quantity
        product.save()
        
    del request.session['orderID']
    
    context = RequestContext(request, {'order': order})
    return render_to_response('checkout/bank_transfer/success.html', context)
