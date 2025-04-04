from django import template

register = template.Library()

@register.filter(name='replace')
def replace_filter(value, arg):
    """
    Usage: {{ some_string|replace:"old,new" }}
    Replaces 'old' with 'new' in 'some_string'.
    Example:
        {{ "Hello World"|replace:"o,0" }} --> Hell0 W0rld
    """
    old, new = arg.split(',')
    return value.replace(old, new)
