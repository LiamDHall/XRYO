from django import template


register = template.Library()


@register.filter(name='subtotal_price_calc')
def subtotal_price_calc(price, quantity):
    return price * quantity
