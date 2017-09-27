from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import ListView, UpdateView, TemplateView, CreateView, DeleteView
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework import filters, permissions, pagination

from nfbr.core.forms import TbcontribuinteForm, TbcfopForm, TbcstForm, TbentradaNfForm, TbprodutoForm, TbufForm, \
    TbunidadeMedidaForm, TbncmForm, TbpessoaForm
from nfbr.core.models import Tbcontribuinte, Tbcfop, Tbcst, TbentradaNf, Tbproduto, Tbuf, TbunidadeMedida, Tbncm, \
    Tbpessoa
from .serializers import *


# from nfbr.core.services import consulta_notas


class TemplateViewCustom(LoginRequiredMixin, TemplateView):
    class Meta:
        abstract = True


class ListViewCustom(LoginRequiredMixin, ListView):
    template_name = 'core/model_list.html'
    paginate_by = 15

    def get_queryset(self):
        if self.model._default_manager.name == 'objects':
            return self.model._default_manager.all()
        return self.model.objects_per_user.all(self.request.user)

    class Meta:
        abstract = True


class CreateViewCustom(LoginRequiredMixin, CreateView):
    template_name = 'core/model_form.html'

    class Meta:
        abstract = True


class CreateViewCustomPerUser(CreateViewCustom):
    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.id_contribuinte = self.request.user.id_contribuinte
        instance.save()
        return super(CreateViewCustomPerUser, self).form_valid(form)

    def get_form_kwargs(self):
        kw = super(CreateViewCustomPerUser, self).get_form_kwargs()
        kw['request'] = self.request
        return kw

    class Meta:
        abstract = True


class UpdateViewCustom(LoginRequiredMixin, UpdateView):
    template_name = 'core/model_form.html'

    def get_queryset(self):
        if self.model._default_manager.name == 'objects':
            return self.model._default_manager.all()
        return self.model.objects_per_user.all(self.request.user)

    class Meta:
        abstract = True


class DeleteViewCustom(LoginRequiredMixin, DeleteView):
    template_name = 'core/model_confirm_delete.html'

    def get_queryset(self):
        if self.model._default_manager.name == 'objects':
            return self.model._default_manager.all()
        return self.model.objects_per_user.all(self.request.user)

    class Meta:
        abstract = True


class ModelViewSetBase:
    filter_backends = (filters.DjangoFilterBackend, filters.SearchFilter,)
    filter_fields = '__all__'

    class Meta:
        abstract = True


class ModelViewSetBaseLookup(ModelViewSet):
    filter_backends = (filters.DjangoFilterBackend, filters.SearchFilter,)
    filter_fields = '__all__'
    pagination_class = pagination.PageNumberPagination

    class Meta:
        abstract = True


# Views Base


class _HomeView(TemplateViewCustom):
    def get_context_data(self, **kwargs):
        context = super(_HomeView, self).get_context_data(**kwargs)
        # context['notas'] = consulta_notas()
        return context


home = _HomeView.as_view(template_name='index.html')

changelist_contribuinte = ListViewCustom.as_view(model=Tbcontribuinte,
                                                 template_name='core/changelist_contribuinte.html')


def changelist_contribuinte_post(request):
    contribuinte = Tbcontribuinte.objects_per_user.get(pk=request.POST.get('pk'))
    user = get_user_model().objects.get(pk=request.user.pk)
    user.id_contribuinte = contribuinte
    user.save()
    return HttpResponseRedirect(reverse_lazy('home'))


list_contribuinte = ListViewCustom.as_view(model=Tbcontribuinte)

create_contribuinte = CreateViewCustom.as_view(model=Tbcontribuinte,
                                               form_class=TbcontribuinteForm)

update_contribuinte = UpdateViewCustom.as_view(model=Tbcontribuinte,
                                               form_class=TbcontribuinteForm,
                                               success_url=reverse_lazy('list_contribuinte'))

delete_contribuinte = DeleteViewCustom.as_view(model=Tbcontribuinte,
                                               success_url=reverse_lazy('list_contribuinte'))


class TbcontribuinteViewSet(ModelViewSet, ModelViewSetBase):
    serializer_class = TbcontribuinteSerializer
    search_fields = ('razao', 'fantasia')

    def get_queryset(self):
        return Tbcontribuinte.objects_per_user.all(self.request.user)


@api_view(['POST'])
@permission_classes((permissions.IsAuthenticated,))
def api_contribuinte_post(request):
    # print('--------')
    # print(request.data.get('pk'))
    # print(request.user)
    contribuinte = Tbcontribuinte.objects_per_user.get(pk=request.data.get('pk'))
    user = get_user_model().objects.get(pk=request.user.pk)
    user.id_contribuinte = contribuinte
    user.save()
    # print(str(user.id_contribuinte))
    return Response({'contribuinte': str(user.id_contribuinte)})


# Views Padrões

# Unidade de Medida

list_unidade_medida = ListViewCustom.as_view(model=TbunidadeMedida)

create_unidade_medida = CreateViewCustom.as_view(model=TbunidadeMedida,
                                                 form_class=TbunidadeMedidaForm,
                                                 success_url=reverse_lazy('list_unidade_medida'))

update_unidade_medida = UpdateViewCustom.as_view(model=TbunidadeMedida,
                                                 form_class=TbunidadeMedidaForm,
                                                 success_url=reverse_lazy('list_unidade_medida'))

delete_unidade_medida = DeleteViewCustom.as_view(model=TbunidadeMedida,
                                                 success_url=reverse_lazy('list_unidade_medida'))


class TbunidadeMedidaViewSet(ModelViewSet, ModelViewSetBase):
    queryset = TbunidadeMedida.objects.all()
    serializer_class = TbunidadeMedidaSerializer
    search_fields = ('sigla', 'descricao')


class TbunidadeMedidaLookupViewSet(ModelViewSetBaseLookup):
    queryset = TbunidadeMedida.objects.all()
    serializer_class = TbunidadeMedidaLookupSerializer
    search_fields = ('sigla', 'descricao')


# UF

list_uf = ListViewCustom.as_view(model=Tbuf)

create_uf = CreateViewCustom.as_view(model=Tbuf,
                                     form_class=TbufForm,
                                     success_url=reverse_lazy('list_uf'))

update_uf = UpdateViewCustom.as_view(model=Tbuf,
                                     form_class=TbufForm,
                                     success_url=reverse_lazy('list_uf'))

delete_uf = DeleteViewCustom.as_view(model=Tbuf,
                                     success_url=reverse_lazy('list_uf'))


class TbufViewSet(ModelViewSet, ModelViewSetBase):
    queryset = Tbuf.objects.all()
    serializer_class = TbufSerializer
    search_fields = ('sigla', 'descricao')


# CST

list_cst = ListViewCustom.as_view(model=Tbcst)

create_cst = CreateViewCustom.as_view(model=Tbcst,
                                      form_class=TbcstForm,
                                      success_url=reverse_lazy('list_cst'))

update_cst = UpdateViewCustom.as_view(model=Tbcst,
                                      form_class=TbcstForm,
                                      success_url=reverse_lazy('list_cst'))

delete_cst = DeleteViewCustom.as_view(model=Tbcst,
                                      success_url=reverse_lazy('list_cst'))


class TbcstViewSet(ModelViewSet, ModelViewSetBase):
    queryset = Tbcst.objects.all()
    serializer_class = TbcstSerializer
    search_fields = ('codigo', 'descricao')


class TbcstLookupViewSet(ModelViewSetBaseLookup):
    # queryset = Tbcst.objects.all()
    serializer_class = TbcstLookupSerializer
    search_fields = ('codigo',)

    def get_queryset(self):
        queryset = Tbcst.objects.all()
        icms = self.request.query_params.get('icms', None)
        if icms is not None:
            user = self.request.user
            if user.id_contribuinte.regime_tributario == '3':
                queryset = queryset.filter(tipo='N')
            else:
                queryset = queryset.filter(tipo='S')

        pis = self.request.query_params.get('pis', None)
        cofins = self.request.query_params.get('cofins', None)
        if pis or cofins is not None:
            queryset = queryset.filter(tipo='C')

        return queryset


# NCM

list_ncm = ListViewCustom.as_view(model=Tbncm)

create_ncm = CreateViewCustom.as_view(model=Tbncm,
                                      form_class=TbncmForm,
                                      success_url=reverse_lazy('list_ncm'))

update_ncm = UpdateViewCustom.as_view(model=Tbncm,
                                      form_class=TbncmForm,
                                      success_url=reverse_lazy('list_ncm'))

delete_ncm = DeleteViewCustom.as_view(model=Tbncm,
                                      success_url=reverse_lazy('list_ncm'))


class TbncmViewSet(ModelViewSet, ModelViewSetBase):
    queryset = Tbncm.objects.all()
    serializer_class = TbncmSerializer
    search_fields = ('codigo', 'descricao')


class TbncmLookupViewSet(ModelViewSetBaseLookup):
    queryset = Tbncm.objects.all()
    serializer_class = TbncmLookupSerializer
    search_fields = ('codigo',)


# CFOP

list_cfop = ListViewCustom.as_view(model=Tbcfop)

create_cfop = CreateViewCustom.as_view(model=Tbcfop,
                                       form_class=TbcfopForm,
                                       success_url=reverse_lazy('list_cfop'))

update_cfop = UpdateViewCustom.as_view(model=Tbcfop,
                                       form_class=TbcfopForm,
                                       success_url=reverse_lazy('list_cfop'))

delete_cfop = DeleteViewCustom.as_view(model=Tbcfop,
                                       success_url=reverse_lazy('list_cfop'))


class TbcfopViewSet(ModelViewSet, ModelViewSetBase):
    queryset = Tbcfop.objects.all()
    serializer_class = TbcfopSerializer
    search_fields = ('codigo', 'descricao')


class TbcfopLookupViewSet(ModelViewSetBaseLookup):
    queryset = Tbcfop.objects.all()
    serializer_class = TbcfopLookupSerializer
    search_fields = ('codigo',)


# Views Cadastros

# Pessoa

list_pessoa = ListViewCustom.as_view(model=Tbpessoa)

create_pessoa = CreateViewCustomPerUser.as_view(model=Tbpessoa,
                                                form_class=TbpessoaForm,
                                                success_url=reverse_lazy('list_pessoa'))

update_pessoa = UpdateViewCustom.as_view(model=Tbpessoa,
                                         form_class=TbpessoaForm,
                                         success_url=reverse_lazy('list_pessoa'))

delete_pessoa = DeleteViewCustom.as_view(model=Tbpessoa,
                                         success_url=reverse_lazy('list_pessoa'))

# Produto

list_produto = ListViewCustom.as_view(model=Tbproduto)

create_produto = CreateViewCustomPerUser.as_view(model=Tbproduto,
                                                 form_class=TbprodutoForm,
                                                 success_url=reverse_lazy('list_produto'))


update_produto = UpdateViewCustom.as_view(model=Tbproduto,
                                          form_class=TbprodutoForm,
                                          success_url=reverse_lazy('list_produto'))

delete_produto = DeleteViewCustom.as_view(model=Tbproduto,
                                          success_url=reverse_lazy('list_produto'))


class TbprodutoViewSet(ModelViewSet):
    filter_backends = (filters.DjangoFilterBackend, filters.SearchFilter,)
    filter_fields = '__all__'
    serializer_class = TbprodutoSerializer
    search_fields = ('codigo', 'descricao')
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        return Tbproduto.objects_per_user.all(self.request.user)

    def perform_create(self, serializer):
        serializer.save(id_contribuinte=self.request.user.id_contribuinte)

    # def __init__(self, *args, **kwargs):
    #     super(TbprodutoViewSet, self).__init__(*args, **kwargs)
    #     self.fields['id_contribuinte'] = self.request.user.id_contribuinte


# Views Movimentos

# Entrada de Nota

list_entrada_nf = ListViewCustom.as_view(model=TbentradaNf)

create_entrada_nf = CreateViewCustom.as_view(model=TbentradaNf,
                                             form_class=TbentradaNfForm,
                                             success_url=reverse_lazy('list_entrada_nf'))

update_entrada_nf = UpdateViewCustom.as_view(model=TbentradaNf,
                                             form_class=TbentradaNfForm,
                                             success_url=reverse_lazy('list_entrada_nf'))

delete_entrada_nf = DeleteViewCustom.as_view(model=TbentradaNf,
                                             success_url=reverse_lazy('list_entrada_nf'))

teste = TemplateViewCustom.as_view(template_name='index.html')
