from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import ListView, UpdateView, TemplateView, CreateView, DeleteView
from rest_framework.viewsets import ModelViewSet

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


class TbunidadeMedidaViewSet(ModelViewSet):
    queryset = TbunidadeMedida.objects.all()
    serializer_class = TbunidadeMedidaSerializer


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


class TbufViewSet(ModelViewSet):
    queryset = Tbuf.objects.all()
    serializer_class = TbufSerializer


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


class TbcstViewSet(ModelViewSet):
    queryset = Tbcst.objects.all()
    serializer_class = TbcstSerializer


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


class TbncmViewSet(ModelViewSet):
    queryset = Tbncm.objects.all()
    serializer_class = TbncmSerializer


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


class TbcfopViewSet(ModelViewSet):
    queryset = Tbcfop.objects.all()
    serializer_class = TbcfopSerializer


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
    serializer_class = TbprodutoSerializer

    def get_queryset(self):
        return Tbproduto.objects_per_user.all(self.request.user)
        # return self.request.user.accounts.all()


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
