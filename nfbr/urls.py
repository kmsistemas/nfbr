from django.conf import settings
from django.conf.urls import url, include
from django.contrib import admin
from django.conf.urls.static import static
from django.contrib.admin.views.decorators import staff_member_required
from rest_framework import routers

from nfbr.core.views import *


create = "novo"
delete = "remover"
unidade_medida = "unidade_medida"
uf = "uf"
cst = "cst"
ncm = "ncm"
cfop = "cfop"

produto = "produto"

router = routers.DefaultRouter(trailing_slash=True)
router.register(unidade_medida, TbunidadeMedidaViewSet)
router.register(uf, TbufViewSet)
router.register(cst, TbcstViewSet)
router.register(ncm, TbncmViewSet)
router.register(cfop, TbcfopViewSet)
router.register(produto, TbprodutoViewSet, produto)

urlpatterns = [
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^api/', include(router.urls)),

    # url(r'^select2/', include('django_select2.urls')),
    # url(r'^selectable/', include('selectable.urls')),

    url('^', include('django.contrib.auth.urls')),
    url(r'^admin/', admin.site.urls),

    url(r'^$', home, name='home'),

    url(r'^alterar_contribuinte/$', changelist_contribuinte, name='changelist_contribuinte'),
    url(r'^alterar_contribuinte_post/$', changelist_contribuinte_post, name='changelist_contribuinte_post'),

    url(r'^contribuinte/$', list_contribuinte, name='list_contribuinte'),
    url(r'^contribuinte/'+create+'/$', staff_member_required(create_contribuinte), name='create_contribuinte'),
    url(r'^contribuinte/(?P<pk>\d+)/$', staff_member_required(update_contribuinte), name='update_contribuinte'),
    url(r'^contribuinte/(?P<pk>\d+)/'+delete+'/$', staff_member_required(delete_contribuinte),
        name='delete_contribuinte'),


    # Padrões

    url(r'^'+unidade_medida+'/$', list_unidade_medida, name='list_unidade_medida'),
    url(r'^'+unidade_medida+'/'+create+'/$', staff_member_required(create_unidade_medida), name='create_unidade_medida'),
    url(r'^'+unidade_medida+'/(?P<pk>\d+)/$', staff_member_required(update_unidade_medida), name='update_unidade_medida'),
    url(r'^'+unidade_medida+'/(?P<pk>\d+)/'+delete+'/$', staff_member_required(delete_unidade_medida),
        name='delete_unidade_medida'),

    url(r'^'+uf+'/$', list_uf, name='list_uf'),
    url(r'^'+uf+'/'+create+'/$', staff_member_required(create_uf), name='create_uf'),
    url(r'^'+uf+'/(?P<pk>\d+)/$', staff_member_required(update_uf), name='update_uf'),
    url(r'^'+uf+'/(?P<pk>\d+)/'+delete+'/$', staff_member_required(delete_uf), name='delete_uf'),

    url(r'^'+cst+'/$', list_cst, name='list_cst'),
    url(r'^'+cst+'/'+create+'/$', staff_member_required(create_cst), name='create_cst'),
    url(r'^'+cst+'/(?P<pk>\d+)/$', staff_member_required(update_cst), name='update_cst'),
    url(r'^'+cst+'/(?P<pk>\d+)/'+delete+'/$', staff_member_required(delete_cst), name='delete_cst'),

    url(r'^'+ncm+'/$', list_ncm, name='list_ncm'),
    url(r'^'+ncm+'/'+create+'/$', staff_member_required(create_ncm), name='create_ncm'),
    url(r'^'+ncm+'/(?P<pk>\d+)/$', staff_member_required(update_ncm), name='update_ncm'),
    url(r'^'+ncm+'/(?P<pk>\d+)/'+delete+'/$', staff_member_required(delete_ncm), name='delete_ncm'),

    url(r'^'+cfop+'/$', list_cfop, name='list_cfop'),
    url(r'^'+cfop+'/'+create+'/$', staff_member_required(create_cfop), name='create_cfop'),
    url(r'^'+cfop+'/(?P<pk>\d+)/$', staff_member_required(update_cfop), name='update_cfop'),
    url(r'^'+cfop+'/(?P<pk>\d+)/'+delete+'/$', staff_member_required(delete_cfop), name='delete_cfop'),


    # Cadastros

    url(r'^pessoa/$', list_pessoa, name='list_pessoa'),
    url(r'^pessoa/' + create + '/$', create_pessoa, name='create_pessoa'),
    url(r'^pessoa/(?P<pk>\d+)/$', update_pessoa, name='update_pessoa'),
    url(r'^pessoa/(?P<pk>\d+)/'+delete+'/$', delete_pessoa, name='delete_pessoa'),

    url(r'^produto/$', list_produto, name='list_produto'),
    url(r'^produto/' + create + '/$', create_produto, name='create_produto'),
    url(r'^produto/(?P<pk>\d+)/$', update_produto, name='update_produto'),
    url(r'^produto/(?P<pk>\d+)/'+delete+'/$', delete_produto, name='delete_produto'),


    # Movimentos

    url(r'^entrada_nf/$', list_entrada_nf, name='list_entrada_nf'),
    url(r'^entrada_nf/'+create+'/$', create_entrada_nf, name='create_entrada_nf'),
    url(r'^entrada_nf/(?P<pk>\d+)/$', update_entrada_nf, name='update_entrada_nf'),

    url(r'^teste/$', teste),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ]
