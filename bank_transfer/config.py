from livesettings import *
from django.utils.translation import ugettext_lazy as _

# this is so that the translation utility will pick up the string
gettext = lambda s: s

PAYMENT_GROUP = ConfigurationGroup('PAYMENT_BANK_TRANSFER',
    _('Bank Transfer Module Settings'),
    ordering = 100)

config_register_list(
    BooleanValue(PAYMENT_GROUP, 
        'SSL', 
        description=_("Use SSL for the module checkout pages?"), 
        default=False),

             
    BooleanValue(PAYMENT_GROUP, 
        'LIVE', 
        description=_("Accept real payments"),
        help_text=_("False if you want to be in test mode"),
        default=False),

        
    ModuleValue(PAYMENT_GROUP,
        'MODULE',
        description=_('Implementation module'),
        hidden=True,
        default = 'store.bank_transfer'), 
        
    StringValue(PAYMENT_GROUP,
        'KEY',
        description=_("Module key"),
        hidden=True,
        default = 'BANK_TRANSFER'),
        
    StringValue(PAYMENT_GROUP,
        'LABEL',
        description=_('English name for this group on the checkout screens'),
        default = 'Bank Transfer',
        help_text = _('This will be passed to the translation utility')),
        
    StringValue(PAYMENT_GROUP,
        'URL_BASE',
        description=_('The url base used for constructing urlpatterns which will use this module'),
        default = '^bank_transfer/'),                
                       
    StringValue(PAYMENT_GROUP,
        'OWNER',
        description=_("Account Owner"),
        hidden=False,
        default = ''),
        
    StringValue(PAYMENT_GROUP,
        'IBAN',
        description=_("IBAN"),
        hidden=False,
        default = ''),
        
    StringValue(PAYMENT_GROUP,
        'SWIFT',
        description=_("SWIFT"),
        hidden=False,
        default = ''),    

    StringValue(PAYMENT_GROUP,
        'INFORMATIONS',
        description=_("Other Informations, shown on email confirm and success page."),
        hidden=False,
        default = ''),              

#    BooleanValue(PAYMENT_GROUP, 
#        'SSL', 
#        description=_("Use SSL for the module checkout pages?"), 
#        default=False),
#        
#    BooleanValue(PAYMENT_GROUP, 
#        'LIVE', 
#        description=_("Accept real payments"),
#        help_text=_("False if you want to be in test mode"),
#        default=False),
        
#    ModuleValue(PAYMENT_GROUP,
#        'MODULE',
#        description=_('Implementation module'),
#        hidden=True,
#        default = 'satchmo.payment.modules.postepay'),
        
#    StringValue(PAYMENT_GROUP,
#        'KEY',
#        description=_("Module key"),
#        hidden=True,
#        default = 'POSTEPAY'),

#    StringValue(PAYMENT_GROUP,
#        'LABEL',
#        description=_('PostePay'),
#        default = 'Payment PostePay module',
#        help_text = _('PostePay is a special rechargeable Credit Card from Poste Italiane SPA')),

#    StringValue(PAYMENT_GROUP,
#        'URL_BASE',
#        description=_('The url base used for constructing urlpatterns which will use this module'),
#        default = '^postepay/'),

    #MultipleStringValue(PAYMENT_GROUP,
    #    'CREDITCHOICES',
    #    description=_('Available credit cards'),
    #    choices = (
    #        (('Visa','Visa')),
    #        (('Mastercard','Mastercard')),
    #        (('Discover','Discover')),
    #        (('American Express', 'American Express'))),
    #    default = ('Visa', 'Mastercard', 'Discover', 'American Express'))
)
