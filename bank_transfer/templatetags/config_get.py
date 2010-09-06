from django import template
from livesettings import config_get_group
         
#payment_method = self.payment.encode()
#return config_get_group('PAYMENT_' + payment_method)
# {% config_get_group order.payments.all.0.payment as payment_config %}

register = template.Library()

class GetConfigNode(template.Node):
    
    def __init__(self, order_var, save_var):
        self.order_var = order_var
        self.save_var = save_var
        
    def render(self, context):
        
        order = context[self.order_var]
        payment_type = order.payments.all()[0].payment
                
        context[self.save_var] = config_get_group('PAYMENT_' + payment_type)
        
        return ''
        
#usage:  {% bank_info for order as payment_info %}
@register.tag(name="bank_info")
def bank_info(parser, token):
    try:
        # split_contents() knows not to split quoted strings.
        tag_name, f, var, a, save_var = token.split_contents()
    except ValueError:
        raise template.TemplateSyntaxError, "%r tag requires exactly three arguments" % token.contents.split()[0]
    return GetConfigNode(var, save_var)