from django.urls import reverse_lazy
from django.views.generic import ListView, UpdateView, TemplateView, CreateView

from nfbr.core.forms import TbcontribuinteForm, TbcfopForm, TbcstForm, TbentradaNfForm, TbprodutoForm
from nfbr.core.models import Tbcontribuinte, Tbcfop, Tbcst, TbentradaNf, Tbproduto


home = TemplateView.as_view(template_name='index.html')


list_contribuinte = ListView.as_view(model=Tbcontribuinte,
                                     template_name='core/model_list.html')


create_contribuinte = CreateView.as_view(model=Tbcontribuinte,
                                         form_class=TbcontribuinteForm,
                                         # template_name='core/model_form.html'
                                         )


update_contribuinte = UpdateView.as_view(model=Tbcontribuinte,
                                         form_class=TbcontribuinteForm,
                                         success_url=reverse_lazy('list_contribuinte'),
                                         # template_name='core/model_form.html'
                                         )


list_cfop = ListView.as_view(model=Tbcfop,
                             template_name='core/model_list.html')


create_cfop = CreateView.as_view(model=Tbcfop,
                                 form_class=TbcfopForm,
                                 template_name='core/model_form.html')


update_cfop = UpdateView.as_view(model=Tbcfop,
                                 form_class=TbcfopForm,
                                 success_url=reverse_lazy('list_cfop'),
                                 template_name='core/model_form.html')


list_cst = ListView.as_view(model=Tbcst,
                            template_name='core/model_list.html')


create_cst = CreateView.as_view(model=Tbcst,
                                form_class=TbcstForm,
                                template_name='core/model_form.html')


update_cst = UpdateView.as_view(model=Tbcst,
                                form_class=TbcstForm,
                                success_url=reverse_lazy('list_cst'),
                                template_name='core/model_form.html')


list_entrada_nf = ListView.as_view(model=TbentradaNf,
                                   template_name='core/model_list.html')


create_entrada_nf = CreateView.as_view(model=TbentradaNf,
                                       form_class=TbentradaNfForm,
                                       template_name='core/model_form.html')


update_entrada_nf = UpdateView.as_view(model=TbentradaNf,
                                       form_class=TbentradaNfForm,
                                       success_url=reverse_lazy('list_entrada_nf'),
                                       template_name='core/model_form.html')


list_produto = ListView.as_view(model=Tbproduto,
                                template_name='core/model_list.html')


create_produto = CreateView.as_view(model=Tbproduto,
                                    form_class=TbprodutoForm,
                                    template_name='core/model_form.html')


update_produto = UpdateView.as_view(model=Tbproduto,
                                    form_class=TbprodutoForm,
                                    success_url=reverse_lazy('list_produto'),
                                    template_name='core/model_form.html')
