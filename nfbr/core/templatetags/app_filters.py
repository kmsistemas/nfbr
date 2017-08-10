from django import template
from django.template.defaultfilters import floatformat
register = template.Library()


@register.filter(name='verbose_name')
def verbose_name(value):
    return value._meta.verbose_name


@register.filter(name='verbose_name_plural')
def verbose_name_plural(value):
    return value._meta.verbose_name_plural


@register.filter(name='model_name')
def model_name(value):
    try:
        return value._meta.model_name
    except:
        return None


@register.filter(name='addcss')
def addcss(value, arg):
    css_classes = value.field.widget.attrs.get('class', None)  #.split(' ')
    if css_classes is None or arg not in css_classes:
        css_classes = '%s %s' % (css_classes, arg)
    return value.as_widget(attrs={'class': css_classes})


# @register.inclusion_tag('core/model_form_tabs_begin.html')
# def model_form_tabs_begin(tabs):
#     return {
#         'tabs': tabs,
#     }


@register.filter(name='getfield')
def getfield(form, arg):
    return form[arg]


@register.filter(name='field_type')
def field_type(field):
    # return field.field.widget.__class__.__name__
    return field.__class__.__name__


@register.filter(name='get_attr')
def get_attr(self, field):
    return getattr(self, field)


@register.filter(name='format_field')
def format_field(value):
    if field_type(value) == 'Decimal':
        return floatformat(value, 2)
    return value