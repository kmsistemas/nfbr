from django import template
register = template.Library()


@register.filter(name='verbose_name')
def verbose_name(value):
    return value._meta.verbose_name


@register.filter(name='verbose_name_plural')
def verbose_name_plural(value):
    return value._meta.verbose_name_plural


@register.filter(name='addcss')
def addcss(value, arg):
    css_classes = value.field.widget.attrs.get('class', None)  #.split(' ')
    if css_classes is None or arg not in css_classes:
        css_classes = '%s %s' % (css_classes, arg)
    return value.as_widget(attrs={'class': css_classes})
