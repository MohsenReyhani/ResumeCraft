from django import template

register = template.Library()


@register.filter
def items(dictionary):
    return dictionary.items()


@register.filter(name='calculate_progress')
def calculate_progress(level, max_level=5):
    try:
        return (level / max_level) * 100
    except (TypeError, ZeroDivisionError):
        return 0

