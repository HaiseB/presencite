from django import template
register = template.Library()

@register.filter
def index(sequence, position):
    try:
        return sequence[position]
    except (IndexError, TypeError):
        return ''

@register.filter
def last(sequence):
    try:
        return sequence[-1]
    except (IndexError, TypeError):
        return '' 