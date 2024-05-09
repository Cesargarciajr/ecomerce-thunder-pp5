from django import template

# Custom template filter to iterate number of stars rated
register = template.Library()

@register.filter
def to_range(value):
    return range(int(value))