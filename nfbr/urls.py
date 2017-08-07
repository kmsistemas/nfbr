from django.conf import settings
from django.conf.urls import url, include
from django.contrib import admin
from django.conf.urls.static import static

from nfbr.core.views import list_contribuinte, update_contribuinte, list_cfop, update_cfop, list_cst, update_cst, \
    list_entrada_nf, update_entrada_nf, list_produto, update_produto, home, create_cfop, create_contribuinte, \
    create_cst, create_entrada_nf, create_produto

urlpatterns = [
    url(r'^admin/', admin.site.urls),

    url(r'^$', home, name='home'),

    url(r'^contribuinte/$', list_contribuinte, name='list_contribuinte'),
    url(r'^contribuinte/novo/$', create_contribuinte, name='create_contribuinte'),
    url(r'^contribuinte/(?P<pk>\d+)/$', update_contribuinte, name='update_contribuinte'),

    url(r'^cfop/$', list_cfop, name='list_cfop'),
    url(r'^cfop/novo/$', create_cfop, name='create_cfop'),
    url(r'^cfop/(?P<pk>\d+)/$', update_cfop, name='update_cfop'),

    url(r'^cst/$', list_cst, name='list_cst'),
    url(r'^cst/novo/$', create_cst, name='create_cst'),
    url(r'^cst/(?P<pk>\d+)/$', update_cst, name='update_cst'),

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
