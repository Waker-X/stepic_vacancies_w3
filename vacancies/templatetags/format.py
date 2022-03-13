from django import template

register = template.Library()


@register.filter()
def format_int(digital):
    if digital:
        return '{0:,}'.format(digital).replace(',', ' ')
    else:
        return digital
