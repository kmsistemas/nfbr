from django.conf import settings
from django.shortcuts import resolve_url as r
# from django.apps import apps
from nfbr.core.models import Tbcontribuinte, Tbcfop, Tbcst, TbentradaNf, Tbproduto, Tbuf, TbunidadeMedida, Tbncm, \
    Tbpessoa


def context_processor(request):
    menu_items = (
        {
            'title': 'início',
            'icon': 'dashboard',
            'link': r('home'),
            'model_name': 'home',
        },
        {
            'title': Tbcontribuinte._meta.verbose_name_plural,
            'icon': 'dashboard',
            'link': r('list_contribuinte'),
            'model_name': Tbcontribuinte._meta.model_name,
        },
        {
            'title': 'padrões',
            'icon': 'dashboard',
            'link': '#menu_padroes',
            'model_name': 'menu_padroes',
            'submenus': (
                {
                    'title': TbunidadeMedida._meta.verbose_name_plural,
                    'icon': 'dashboard',
                    'link': r('list_unidade_medida'),
                    'model_name': TbunidadeMedida._meta.model_name,
                },
                {
                    'title': Tbuf._meta.verbose_name_plural,
                    'icon': 'dashboard',
                    'link': r('list_uf'),
                    'model_name': Tbuf._meta.model_name,
                },
                {
                    'title': Tbcst._meta.verbose_name_plural,
                    'icon': 'dashboard',
                    'link': r('list_cst'),
                    'model_name': Tbcst._meta.model_name,
                },
                {
                    'title': Tbncm._meta.verbose_name_plural,
                    'icon': 'dashboard',
                    'link': r('list_ncm'),
                    'model_name': Tbncm._meta.model_name,
                },
                {
                    'title': Tbcfop._meta.verbose_name_plural,
                    'icon': 'dashboard',
                    'link': r('list_cfop'),
                    'model_name': Tbcfop._meta.model_name,
                },
            )
        },
        {
            'title': 'cadastros',
            'icon': 'dashboard',
            'link': '#menu_cadastros',
            'model_name': 'menu_cadastros',
            'submenus': (
                {
                    'title': Tbpessoa._meta.verbose_name_plural,
                    'icon': 'dashboard',
                    'link': r('list_pessoa'),
                    'model_name': Tbpessoa._meta.model_name,
                },
                {
                    'title': Tbproduto._meta.verbose_name_plural,
                    'icon': 'dashboard',
                    'link': r('list_produto'),
                    'model_name': Tbproduto._meta.model_name,
                },
            ),
        },
        {
            'title': TbentradaNf._meta.verbose_name_plural,
            'icon': 'dashboard',
            'link': r('list_entrada_nf'),
            'model_name': TbentradaNf._meta.model_name,
        },
    )

    my_dict = {
        'site_name': settings.SITE_NAME,
        'site_title': settings.SITE_TITLE,
        'menu_items': menu_items,
    }

    return my_dict
