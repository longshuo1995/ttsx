from django.template import Library
register = Library()


@register.filter
def change(num1):
    return int(num1)*-1
