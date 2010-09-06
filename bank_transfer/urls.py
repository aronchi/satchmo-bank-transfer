from django.conf.urls.defaults import *
from livesettings import config_get_group
from django.conf import settings

config = config_get_group('PAYMENT_BANK_TRANSFER')

urlpatterns = patterns('',
     (r'^$', 'bank_transfer.views.pay_ship_info', {'SSL':config.SSL.value}, 'BANK_TRANSFER_satchmo_checkout-step2'),
     (r'^confirm/$', 'bank_transfer.views.confirm_info', {'SSL':config.SSL.value}, 'BANK_TRANSFER_satchmo_checkout-step3'),
     (r'^success/$', 'payment.views.checkout.success', {'SSL':config.SSL.value}, 'BANK_TRANSFER_satchmo_checkout-success'),
)
