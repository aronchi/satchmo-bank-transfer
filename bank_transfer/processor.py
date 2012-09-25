"""
This is a stub and used as the default processor.
It doesn't do anything but it can be used to build out another
interface.

See the authorizenet module for the reference implementation
"""
from django.utils.translation import ugettext as _
from payment.modules.base import BasePaymentProcessor, ProcessorResult

class PaymentProcessor(BasePaymentProcessor):

    def __init__(self, settings):
        self.settings = settings
        super(PaymentProcessor, self).__init__('bank_transfer', settings)


    def prepareData(self, order):
        self.order = order

    def process(self):
        orderpayment = self.record_payment(amount=self.order.balance, reason_code="0")
        return ProcessorResult (self.key, True, _("Success"), orderpayment)

