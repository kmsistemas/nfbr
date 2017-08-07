from django.conf import settings


def context_processor(request):
    my_dict = {
        'site_name': settings.SITE_NAME,
        'site_title': settings.SITE_TITLE,
    }

    return my_dict
