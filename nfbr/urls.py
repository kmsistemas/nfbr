from django.conf import settings
from django.conf.urls import url, include
from django.contrib import admin
from django.conf.urls.static import static
from django.contrib.admin.views.decorators import staff_member_required

from nfbr.core.views import list_contribuinte, update_contribuinte, list_cfop, update_cfop, list_cst, update_cst, \
    list_entrada_nf, update_entrada_nf, list_produto, update_produto, home, create_cfop, create_contribuinte, \
    create_cst, create_entrada_nf, create_produto, list_uf, create_uf, changelist_contribuinte, \
    changelist_contribuinte_post, update_uf, list_unidade_medida, create_unidade_medida, update_unidade_medida, \
    list_ncm, create_ncm, update_ncm, delete_unidade_medida

urlpatterns = [
    url('^', include('django.contrib.auth.urls')),
    url(r'^admin/', admin.site.urls),

    url(r'^$', home, name='home'),

    url(r'^alterar_contribuinte/$', changelist_contribuinte, name='changelist_contribuinte'),
    url(r'^alterar_contribuinte_post/$', changelist_contribuinte_post, name='changelist_contribuinte_post'),

    url(r'^contribuinte/$', list_contribuinte, name='list_contribuinte'),
    url(r'^contribuinte/novo/$', staff_member_required(create_contribuinte), name='create_contribuinte'),
    url(r'^contribuinte/(?P<pk>\d+)/$', staff_member_required(update_contribuinte), name='update_contribuinte'),


    # Padrões

    url(r'^unidade_medida/$', list_unidade_medida, name='list_unidade_medida'),
    url(r'^unidade_medida/novo/$', staff_member_required(create_unidade_medida), name='create_unidade_medida'),
    url(r'^unidade_medida/(?P<pk>\d+)/$', staff_member_required(update_unidade_medida), name='update_unidade_medida'),
    url(r'^unidade_medida/(?P<pk>\d+)/remover/$', staff_member_required(delete_unidade_medida), name='delete_unidade_medida'),

    url(r'^uf/$', list_uf, name='list_uf'),
    url(r'^uf/novo/$', staff_member_required(create_uf), name='create_uf'),
    url(r'^uf/(?P<pk>\d+)/$', staff_member_required(update_uf), name='update_uf'),

    url(r'^cst/$', list_cst, name='list_cst'),
    url(r'^cst/novo/$', staff_member_required(create_cst), name='create_cst'),
    url(r'^cst/(?P<pk>\d+)/$', staff_member_required(update_cst), name='update_cst'),

    url(r'^ncm/$', list_ncm, name='list_ncm'),
    url(r'^ncm/novo/$', staff_member_required(create_ncm), name='create_ncm'),
    url(r'^ncm/(?P<pk>\d+)/$', staff_member_required(update_ncm), name='update_ncm'),

    url(r'^cfop/$', list_cfop, name='list_cfop'),
    url(r'^cfop/novo/$', staff_member_required(create_cfop), name='create_cfop'),
    url(r'^cfop/(?P<pk>\d+)/$', staff_member_required(update_cfop), name='update_cfop'),



    url(r'^entrada_nf/$', list_entrada_nf, name='list_entrada_nf'),
    url(r'^entrada_nf/novo/$', create_entrada_nf, name='create_entrada_nf'),
    url(r'^entrada_nf/(?P<pk>\d+)/$', update_entrada_nf, name='update_entrada_nf'),

    url(r'^produto/$', list_produto, name='list_produto'),
    url(r'^produto/novo/$', create_produto, name='create_produto'),
    url(r'^produto/(?P<pk>\d+)/$', update_produto, name='update_produto'),



] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ]
