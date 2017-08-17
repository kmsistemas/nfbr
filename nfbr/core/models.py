from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils.translation import ugettext_lazy as _
from django.shortcuts import resolve_url as r

from nfbr.core.managers import TbusuarioManager, TbcontribuinteManager, ModelPerUserManager

SIM_NAO_CHOICES = (
    ('S', 'Sim'),
    ('N', 'Não'),
)


class CustomModel(models.Model):
    def list_display(self):
        return []

    def list_display_title(self):
        return [(self._meta.get_field(field)) for field in self.list_display()]

    # def list_display_value(self):
    #     return [(getattr(self, field)) for field in self.list_display()]

    class Meta:
        abstract = True


class Tbcfop(CustomModel):
    id_cfop = models.AutoField(primary_key=True)
    codigo = models.CharField(unique=True, max_length=4)
    descricao = models.CharField(max_length=120)
    combustivel = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'tbcfop'
        verbose_name = 'cfop'
        verbose_name_plural = 'cfops'

    def __str__(self):
        return self.codigo

    @staticmethod
    def get_add_url():
        return r('create_cfop')

    def get_edit_url(self):
        return r('update_cfop', self.pk)

    def get_delete_url(self):
        return r('delete_cfop', self.pk)

    def list_display(self):
        return [
            'codigo',
            'descricao',
        ]


class Tbcontribuinte(CustomModel):
    id_contribuinte = models.AutoField(primary_key=True)
    razao = models.CharField('razão social', max_length=120)
    fantasia = models.CharField('nome fantasia', max_length=120, blank=True, null=True)
    situacao = models.CharField(max_length=1)
    cep = models.CharField(max_length=10, blank=True, null=True)
    logradouro = models.CharField(max_length=60, blank=True, null=True)
    nro_logradouro = models.CharField(max_length=60, blank=True, null=True)
    complemento = models.CharField(max_length=60, blank=True, null=True)
    bairro = models.CharField(max_length=60, blank=True, null=True)
    municipio = models.CharField('município', max_length=60, blank=True, null=True)
    ibge_municipio = models.CharField('IBGE município', max_length=7, blank=True, null=True)
    fone = models.CharField('telefone', max_length=20, blank=True, null=True)
    fax = models.CharField(max_length=20, blank=True, null=True)
    cnpj = models.CharField(unique=True, max_length=20, blank=True, null=True)
    ie = models.CharField(max_length=20, blank=True, null=True)
    email = models.CharField(max_length=60, blank=True, null=True)
    REGIME_TRIBUTARIO_CHOICES = (
        ('1', '1 - Simples Nacional'),
        ('2', '2 - Simples Nacional (Excesso de sublimite de receita bruta)'),
        ('3', '3 - Regime Normal'),
    )
    regime_tributario = models.CharField('regime tributário', max_length=1, blank=True, null=True, choices=REGIME_TRIBUTARIO_CHOICES)
    id_token_nfce = models.CharField('id. token', max_length=20, blank=True, null=True)
    codigo_token_nfce = models.CharField('código token', max_length=60, blank=True, null=True)
    servidor_email_nfce = models.CharField('servidor de envio de e-mail (SMTP)', max_length=100, blank=True, null=True)
    porta_email_nfce = models.CharField('porta de envio de e-mail', max_length=4, blank=True, null=True)
    login_email_nfce = models.CharField('login e-mail', max_length=60, blank=True, null=True)
    senha_email_nfce = models.CharField('senha e-mail', max_length=60, blank=True, null=True)
    requer_autenticacao_email_nfce = models.NullBooleanField('requerido autenticação e-mail')
    timeout_email_nfce = models.IntegerField('tempo de espera e-mail', blank=True, null=True)
    remetente_email_nfce = models.CharField('remetente e-mail', max_length=60, blank=True, null=True)
    assunto_email_nfce = models.CharField('assunto e-mail', max_length=120, blank=True, null=True)
    cc_email_nfce = models.CharField('Com Cópia e-mail', max_length=200, blank=True, null=True)
    cco_email_nfce = models.CharField('Com Cópia Oculta e-mail', max_length=200, blank=True, null=True)
    mensagem_email_nfce = models.TextField('mensagem e-mail', blank=True, null=True)
    id_uf = models.ForeignKey('Tbuf', models.DO_NOTHING, verbose_name='estado', db_column='id_uf', blank=True,
                              null=True)
    validade_licenca = models.DateField('validade licença', blank=True, null=True)
    AMBIENTE_CHOICES = (
        (1, 'Produção'),
        (2, 'Homologação'),
    )
    ambiente = models.IntegerField(choices=AMBIENTE_CHOICES)
    certificado = models.CharField(max_length=255, blank=True, null=True)
    fuso_horario = models.CharField('fuso horário', max_length=6)
    numero_inicial_nfce = models.IntegerField('número inicial')
    TIPO_IMPRESSAO_NFCE_CHOICES = (
        ('1', 'Direta'),
        ('2', 'Imprime'),
        ('3', 'Visualiza'),
    )
    tipo_impressao_nfce = models.CharField('tipo de impressão', max_length=1, choices=TIPO_IMPRESSAO_NFCE_CHOICES)
    controla_estoque = models.CharField(max_length=1, choices=SIM_NAO_CHOICES)
    controla_financeiro = models.CharField(max_length=1, choices=SIM_NAO_CHOICES)
    orcamento = models.CharField('controla orçamento', max_length=1, choices=SIM_NAO_CHOICES)
    financeiro_km_gerado = models.CharField(max_length=1, blank=True, null=True)
    ultimo_aviso = models.DateField(blank=True, null=True)
    TIPO_IMPRESSAO_ORCAMENTO_CHOICES = (
        ('1', 'A4'),
        ('2', 'Cupom'),
    )
    tipo_imp_orcamento = models.CharField('tipo orçamento', max_length=1, blank=True, null=True, choices=TIPO_IMPRESSAO_ORCAMENTO_CHOICES)

    objects_per_user = TbcontribuinteManager()

    class Meta:
        managed = False
        db_table = 'tbcontribuinte'
        verbose_name = 'contribuinte'
        verbose_name_plural = 'contribuintes'

    def __str__(self):
        return self.razao

    @staticmethod
    def get_add_url():
        return r('create_contribuinte')

    def get_edit_url(self):
        return r('update_contribuinte', self.pk)

    def list_display(self):
        return [
            'razao',
            'fantasia',
            'municipio',
        ]

    @staticmethod
    def tabs():
        return (
            {
                'name': 'tab_dados', 'title': 'Dados',
                'fields': (
                    ({'name': 'razao', 'columns': 12},),
                    ({'name': 'fantasia', 'columns': 12},),
                    (
                        {'name': 'cep', 'columns': 3},
                        {'name': 'logradouro', 'columns': 4},
                        {'name': 'nro_logradouro', 'columns': 2},
                        {'name': 'complemento', 'columns': 3},
                    ),
                    (
                        {'name': 'bairro', 'columns': 3},
                        {'name': 'municipio', 'columns': 4},
                        {'name': 'ibge_municipio', 'columns': 2},
                        {'name': 'id_uf', 'columns': 3},
                    ),
                    (
                        {'name': 'fone', 'columns': 3},
                        {'name': 'fax', 'columns': 3},
                        {'name': 'cnpj', 'columns': 3},
                        {'name': 'ie', 'columns': 3},
                    ),
                    ({'name': 'email', 'columns': 12},),
                    (
                        {'name': 'validade_licenca', 'columns': 2},
                        {'name': 'controla_financeiro', 'columns': 2},
                        {'name': 'controla_estoque', 'columns': 2},
                        {'name': 'orcamento', 'columns': 2},
                        {'name': 'tipo_imp_orcamento', 'columns': 2},
                        {'name': 'ambiente', 'columns': 2},
                    ),
                )
            },
            {
                'name': 'tab_tributacao', 'title': 'Tributação',
                'fields': (
                    ({'name': 'regime_tributario', 'columns': 12},),
                    ({'name': 'certificado', 'columns': 12},),
                    (
                        {'name': 'fuso_horario', 'columns': 3},
                        {'name': 'numero_inicial_nfce', 'columns': 3},
                        {'name': 'tipo_impressao_nfce', 'columns': 6},
                    ),
                    (
                        {'name': 'id_token_nfce', 'columns': 2},
                        {'name': 'codigo_token_nfce', 'columns': 10},
                    ),
                    (
                        {'name': 'servidor_email_nfce', 'columns': 8},
                        {'name': 'porta_email_nfce', 'columns': 4},
                    ),
                    (
                        {'name': 'login_email_nfce', 'columns': 6},
                        {'name': 'senha_email_nfce', 'columns': 6},
                    ),
                    (
                        {'name': 'timeout_email_nfce', 'columns': 6},
                        {'name': 'requer_autenticacao_email_nfce', 'columns': 6},
                    ),
                    ({'name': 'remetente_email_nfce', 'columns': 12},),
                    ({'name': 'cc_email_nfce', 'columns': 12},),
                    ({'name': 'cco_email_nfce', 'columns': 12},),
                    ({'name': 'assunto_email_nfce', 'columns': 12},),
                    ({'name': 'mensagem_email_nfce', 'columns': 12},),
                )
            },
        )


class Tbcst(CustomModel):
    id_cst = models.AutoField(primary_key=True)
    codigo = models.CharField(max_length=3)
    tipo = models.CharField(max_length=1)
    descricao = models.TextField()

    class Meta:
        managed = False
        db_table = 'tbcst'
        unique_together = (('codigo', 'tipo'),)
        verbose_name = 'cst'
        verbose_name_plural = 'csts'

    def __str__(self):
        return self.codigo

    @staticmethod
    def get_add_url():
        return r('create_cst')

    def get_edit_url(self):
        return r('update_cst', self.pk)

    def get_delete_url(self):
        return r('delete_cst', self.pk)

    def list_display(self):
        return [
            'codigo',
            'descricao',
        ]


class TbentradaNf(CustomModel):
    id_entrada_nf = models.AutoField(primary_key=True)
    data_nf = models.DateField()
    id_pessoa = models.ForeignKey('Tbpessoa', models.DO_NOTHING, db_column='id_pessoa')
    valor_nf = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    id_contribuinte = models.ForeignKey(Tbcontribuinte, models.DO_NOTHING, db_column='id_contribuinte')

    objects_per_user = ModelPerUserManager()

    class Meta:
        managed = False
        db_table = 'tbentrada_nf'
        verbose_name = 'entrada de nota'
        verbose_name_plural = 'entrada de notas'

    def __str__(self):
        return self.id_entrada_nf

    @staticmethod
    def get_add_url():
        return r('create_entrada_nf')

    def get_edit_url(self):
        return r('update_entrada_nf', self.pk)

    def list_display(self):
        return [
            'data_nf',
            'id_pessoa',
        ]


class TbentradaNfItem(CustomModel):
    id_entrada_nf_item = models.AutoField(primary_key=True)
    id_entrada_nf = models.ForeignKey(TbentradaNf, models.DO_NOTHING, db_column='id_entrada_nf')
    id_produto = models.ForeignKey('Tbproduto', models.DO_NOTHING, db_column='id_produto')
    quantidade = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    preco = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbentrada_nf_item'


# class Tberros(CustomModel):
#     id_erro = models.AutoField(primary_key=True)
#     mensagem = models.TextField(unique=True)
#     traducao = models.TextField(blank=True, null=True)
#     tela = models.CharField(max_length=100, blank=True, null=True)
#     objeto = models.CharField(max_length=100, blank=True, null=True)
#     data_hora = models.DateTimeField(blank=True, null=True)
#     email_usuario = models.CharField(max_length=120, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tberros'


class TbitmodVenda(CustomModel):
    id_itmod_venda = models.AutoField(primary_key=True)
    quantidade = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    preco = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    calcula = models.CharField(max_length=1)
    id_produto = models.ForeignKey('Tbproduto', models.DO_NOTHING, db_column='id_produto')
    id_mod_venda = models.ForeignKey('TbmodVenda', models.DO_NOTHING, db_column='id_mod_venda')

    class Meta:
        managed = False
        db_table = 'tbitmod_venda'


class Tbitnfe(CustomModel):
    id_itnfe = models.AutoField(primary_key=True)
    qcom_i10 = models.DecimalField(max_digits=65535, decimal_places=65535)
    vuncom_i10a = models.DecimalField(max_digits=65535, decimal_places=65535)
    vprod_i11 = models.DecimalField(max_digits=65535, decimal_places=65535)
    vtottrib_m02 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    id_produto = models.ForeignKey('Tbproduto', models.DO_NOTHING, db_column='id_produto')
    id_nfe = models.ForeignKey('Tbnfe', models.DO_NOTHING, db_column='id_nfe')
    cprod_i02 = models.CharField(max_length=60)
    xprod_i04 = models.CharField(max_length=120)
    indtot_i17b = models.IntegerField()
    ncm_i05 = models.CharField(max_length=8, blank=True, null=True)
    cfop_i08 = models.CharField(max_length=4, blank=True, null=True)
    orig_n11 = models.IntegerField()
    cst_n12 = models.CharField(max_length=3, blank=True, null=True)
    ucom_i09 = models.CharField(max_length=6, blank=True, null=True)
    modbc_n13 = models.IntegerField(blank=True, null=True)
    vbc_n15 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    picms_n16 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    vicms_n17 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    predbc_n14 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    cean_i03 = models.CharField(max_length=14, blank=True, null=True)
    vbcstret_n26 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    vicmsstret_n27 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    vicmsdeson_n27a = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    motdesicms_n28 = models.IntegerField(blank=True, null=True)
    cst_q06 = models.CharField(max_length=2, blank=True, null=True)
    vbc_q07 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    ppis_q08 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    vpis_q09 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    qbcprod_q10 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    valiqprod_q11 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    cst_s06 = models.CharField(max_length=2, blank=True, null=True)
    vbc_s07 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    pcofins_s08 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    vcofins_s11 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    qbcprod_s09 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    valiqprod_s10 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    vfrete_i15 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    vdesc_i17 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    cprodanp_la02 = models.CharField(max_length=9, blank=True, null=True)
    pmixgn_la03 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    codif_la04 = models.CharField(max_length=21, blank=True, null=True)
    qtemp_la05 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    cest_i05c = models.CharField(max_length=7, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbitnfe'


# class Tblog(models.Model):
#     id = models.BigAutoField(primary_key=True)
#     nome_campo = models.CharField(max_length=60, blank=True, null=True)
#     nome_tabela = models.CharField(max_length=60, blank=True, null=True)
#     valor_antigo = models.CharField(max_length=-1, blank=True, null=True)
#     valor_novo = models.CharField(max_length=-1, blank=True, null=True)
#     operacao = models.CharField(max_length=20, blank=True, null=True)
#     usuario = models.CharField(max_length=120, blank=True, null=True)
#     pktabela = models.IntegerField(blank=True, null=True)
#     datahora = models.DateTimeField(blank=True, null=True)
#     usuario_maquina = models.CharField(max_length=100, blank=True, null=True)
#     nome_maquina = models.CharField(max_length=100, blank=True, null=True)
#     ip_maquina = models.CharField(max_length=100, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tblog'


class TbmodVenda(CustomModel):
    id_mod_venda = models.AutoField(primary_key=True)
    id_contribuinte = models.ForeignKey(Tbcontribuinte, models.DO_NOTHING, db_column='id_contribuinte')
    descricao = models.CharField(max_length=60, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbmod_venda'
        verbose_name = 'modelo de venda'
        verbose_name_plural = 'modelos de venda'

    def __str__(self):
        return self.descricao

    def list_display(self):
        return [
            'descricao',
        ]


class Tbncm(CustomModel):
    id_ncm = models.AutoField(primary_key=True)
    codigo = models.CharField(unique=True, max_length=8)
    descricao = models.TextField()

    class Meta:
        managed = False
        db_table = 'tbncm'
        verbose_name = 'ncm'
        verbose_name_plural = 'ncms'

    def __str__(self):
        return self.codigo

    @staticmethod
    def get_add_url():
        return r('create_ncm')

    def get_edit_url(self):
        return r('update_ncm', self.pk)

    def get_delete_url(self):
        return r('delete_ncm', self.pk)

    def list_display(self):
        return [
            'codigo',
            'descricao',
        ]


class TbncmIbpt(CustomModel):
    id_ncm_ibpt = models.AutoField(primary_key=True)
    codigo_ncm = models.CharField(max_length=8)
    id_uf = models.ForeignKey('Tbuf', models.DO_NOTHING, db_column='id_uf')
    aliquota_fed_nacional = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    aliquota_fed_importada = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    aliquota_estadual = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    aliquota_municipal = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    data_inicio = models.DateField(blank=True, null=True)
    data_fim = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbncm_ibpt'


class Tbnfe(CustomModel):
    id_nfe = models.AutoField(primary_key=True)
    id_contribuinte = models.ForeignKey(Tbcontribuinte, models.DO_NOTHING, db_column='id_contribuinte')
    id_pessoa = models.ForeignKey('Tbpessoa', models.DO_NOTHING, db_column='id_pessoa', blank=True, null=True)
    dhemi_b09 = models.DateTimeField(blank=True, null=True)
    vbc_w03 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    vicms_w04 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    vbcst_w05 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    vst_w06 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    vprod_w07 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    vicmsdeson_w04a = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    vfrete_w08 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    vseg_w09 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    vdesc_w10 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    vii_w11 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    vipi_w12 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    vpis_w13 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    vcofins_w14 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    voutro_w15 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    vnf_w16 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    vtottrib_w16a = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    vlr_dinheiro = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    vlr_cheque = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    vlr_cartao_cre = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    vlr_cartao_deb = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    vlr_outros = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    serie_b07 = models.IntegerField(blank=True, null=True)
    nnf_b08 = models.IntegerField(blank=True, null=True)
    data_finalizacao = models.DateTimeField(blank=True, null=True)
    xml_limpo = models.TextField(blank=True, null=True)
    xml_assinado = models.TextField(blank=True, null=True)
    xml_enviado = models.TextField(blank=True, null=True)
    protocolo_envio = models.CharField(max_length=120, blank=True, null=True)
    id_a03 = models.CharField(max_length=44, blank=True, null=True)
    data_cancelamento = models.DateTimeField(blank=True, null=True)
    xml_cancelado = models.TextField(blank=True, null=True)
    xml_destinatario = models.TextField(blank=True, null=True)
    id_usuario = models.ForeignKey('Tbusuario', models.DO_NOTHING, db_column='id_usuario')
    data_autorizacao = models.DateTimeField(blank=True, null=True)
    tpamb_b24 = models.IntegerField()
    protocolo_cancelamento = models.CharField(max_length=120, blank=True, null=True)
    infcpl_z03 = models.TextField(blank=True, null=True)
    indpres_b25b = models.IntegerField()
    modfrete_x02 = models.IntegerField()
    tpemis_b22 = models.CharField(max_length=1)
    email_e19 = models.CharField(max_length=60, blank=True, null=True)
    cnpj_e02 = models.CharField(max_length=14, blank=True, null=True)
    cpf_e03 = models.CharField(max_length=11, blank=True, null=True)
    xnome_e04 = models.CharField(max_length=60, blank=True, null=True)
    xlgr_e06 = models.CharField(max_length=60, blank=True, null=True)
    nro_e07 = models.CharField(max_length=60, blank=True, null=True)
    xcpl_e08 = models.CharField(max_length=60, blank=True, null=True)
    xbairro_e09 = models.CharField(max_length=60, blank=True, null=True)
    cmun_e10 = models.CharField(max_length=7, blank=True, null=True)
    xmun_e11 = models.CharField(max_length=60, blank=True, null=True)
    uf_e12 = models.CharField(max_length=2, blank=True, null=True)
    cep_e13 = models.CharField(max_length=8, blank=True, null=True)
    cpais_e14 = models.CharField(max_length=4, blank=True, null=True)
    xpais_e15 = models.CharField(max_length=60, blank=True, null=True)
    fone_e16 = models.CharField(max_length=14, blank=True, null=True)
    id_mod_venda = models.ForeignKey(TbmodVenda, models.DO_NOTHING, db_column='id_mod_venda', blank=True, null=True)
    lancamentos = models.CharField(max_length=1)
    cstat = models.CharField(max_length=3, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbnfe'
        verbose_name = 'nfe'
        verbose_name_plural = 'nfes'

    def __str__(self):
        return self.nnf_b08

    def list_display(self):
        return [
            'nnf_b08',
        ]


class TbnfeInutilizada(CustomModel):
    id_nfe_inutilizada = models.AutoField(primary_key=True)
    ano = models.IntegerField()
    modelo = models.IntegerField()
    serie = models.IntegerField()
    inicio = models.IntegerField()
    fim = models.IntegerField()
    justificativa = models.CharField(max_length=255)
    id_contribuinte = models.ForeignKey(Tbcontribuinte, models.DO_NOTHING, db_column='id_contribuinte')
    ambiente = models.IntegerField()
    data_inutilizacao = models.DateTimeField(blank=True, null=True)
    xml_inutilizado = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbnfe_inutilizada'


class Tbpessoa(CustomModel):
    id_pessoa = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=120, blank=True, null=True)
    id_contribuinte = models.ForeignKey(Tbcontribuinte, models.DO_NOTHING, db_column='id_contribuinte')
    cpf = models.CharField(max_length=20, blank=True, null=True)
    cnpj = models.CharField(max_length=20, blank=True, null=True)
    ie = models.CharField(max_length=20, blank=True, null=True)
    cep = models.CharField(max_length=10, blank=True, null=True)
    logradouro = models.CharField(max_length=60, blank=True, null=True)
    nro_logradouro = models.CharField(max_length=60, blank=True, null=True)
    complemento = models.CharField(max_length=60, blank=True, null=True)
    bairro = models.CharField(max_length=60, blank=True, null=True)
    municipio = models.CharField(max_length=60, blank=True, null=True)
    ibge_municipio = models.CharField(max_length=7, blank=True, null=True)
    email = models.CharField(max_length=60, blank=True, null=True)
    id_uf = models.ForeignKey('Tbuf', models.DO_NOTHING, db_column='id_uf', blank=True, null=True)
    fone = models.CharField(max_length=14, blank=True, null=True)
    cliente = models.BooleanField()
    fornecedor = models.BooleanField()
    observacao = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbpessoa'
        verbose_name = 'pessoa'
        verbose_name_plural = 'pessoas'

    def __str__(self):
        return self.nome

    def list_display(self):
        return [
            'nome',
        ]


class Tbproduto(CustomModel):
    id_produto = models.AutoField(primary_key=True)
    codigo = models.CharField(max_length=20)
    descricao = models.CharField('descrição', max_length=120)
    situacao = models.CharField(max_length=1)
    preco_venda = models.DecimalField(max_digits=65535, decimal_places=65535)
    origem = models.IntegerField()
    id_contribuinte = models.ForeignKey(Tbcontribuinte, models.DO_NOTHING, db_column='id_contribuinte')
    id_unidade_medida = models.ForeignKey('TbunidadeMedida', models.DO_NOTHING, db_column='id_unidade_medida')
    id_ncm = models.ForeignKey(Tbncm, models.DO_NOTHING, db_column='id_ncm')
    id_tributacao = models.ForeignKey('Tbtributacao', models.DO_NOTHING, db_column='id_tributacao', blank=True,
                                      null=True)
    id_cst_icms = models.ForeignKey(Tbcst, models.DO_NOTHING, db_column='id_cst_icms', related_name='produtosIcms')
    aliq_icms = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    id_cst_pis = models.ForeignKey(Tbcst, models.DO_NOTHING, db_column='id_cst_pis', related_name='produtosPis')
    aliq_pis = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    id_cst_cofins = models.ForeignKey(Tbcst, models.DO_NOTHING, db_column='id_cst_cofins',
                                      related_name='produtosCofins')
    aliq_cofins = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    id_cfop = models.ForeignKey(Tbcfop, models.DO_NOTHING, db_column='id_cfop', blank=True, null=True)
    cod_barra = models.CharField(max_length=14, blank=True, null=True)
    modbcicms = models.IntegerField(blank=True, null=True)
    pcredbcicms = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    saldo_estoque = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    estoque_minimo = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    cprodanp_la02 = models.CharField(max_length=9, blank=True, null=True)
    pmixgn_la03 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    codif_la04 = models.CharField(max_length=21, blank=True, null=True)
    cest_i05c = models.CharField(max_length=7, blank=True, null=True)

    objects_per_user = ModelPerUserManager()

    class Meta:
        managed = False
        db_table = 'tbproduto'
        unique_together = (('id_contribuinte', 'codigo'), ('id_contribuinte', 'descricao'),)
        verbose_name = 'produto'
        verbose_name_plural = 'produtos'

    def __str__(self):
        return self.descricao

    @staticmethod
    def get_add_url():
        return r('create_produto')

    def get_edit_url(self):
        return r('update_produto', self.pk)

    def list_display(self):
        return [
            'codigo',
            'descricao',
            'saldo_estoque'
        ]

    @staticmethod
    def tabs():
        return (
            {
                'name': 'tab_dados', 'title': 'Dados',
                'fields': (
                    ({'name': 'descricao', 'columns': 12},),
                    ({'name': 'id_unidade_medida', 'columns': 12},),
                )
            },
        )


class TbtempProd(CustomModel):
    id_contribuinte = models.BigIntegerField(blank=True, null=True)
    codigo = models.CharField(max_length=20, blank=True, null=True)
    produto = models.CharField(max_length=60, blank=True, null=True)
    preco = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    cfop = models.CharField(max_length=4, blank=True, null=True)
    codbarras = models.CharField(max_length=14, blank=True, null=True)
    ncm = models.CharField(max_length=8, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbtemp_prod'


class Tbtitulo(CustomModel):
    id_titulo = models.AutoField(primary_key=True)
    tipo = models.CharField(max_length=1)
    codigo = models.CharField(max_length=120, blank=True, null=True)
    descricao = models.CharField(max_length=120)
    emissao = models.DateField()
    vencimento = models.DateField()
    valor = models.DecimalField(max_digits=65535, decimal_places=65535)
    id_pessoa = models.ForeignKey(Tbpessoa, models.DO_NOTHING, db_column='id_pessoa')
    liquidacao = models.DateField(blank=True, null=True)
    valor_pago = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    valor_desconto = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    valor_juro = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    id_contribuinte = models.ForeignKey(Tbcontribuinte, models.DO_NOTHING, db_column='id_contribuinte')
    id_entrada_nf = models.ForeignKey(TbentradaNf, models.DO_NOTHING, db_column='id_entrada_nf', blank=True, null=True)
    id_nfe = models.ForeignKey(Tbnfe, models.DO_NOTHING, db_column='id_nfe', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbtitulo'
        verbose_name = 'titulo'
        verbose_name_plural = 'titulos'

    def __str__(self):
        return self.descricao

    def list_display(self):
        return [
            'codigo',
            'descricao',
            'emissao',
            'vencimento',
            'valor',
        ]


class Tbtributacao(CustomModel):
    id_tributacao = models.AutoField(primary_key=True)
    codigo = models.CharField(max_length=20)
    descricao = models.CharField(max_length=120)
    id_cst_icms = models.ForeignKey(Tbcst, models.DO_NOTHING, db_column='id_cst_icms', related_name='tributacoesIcms')
    aliq_icms = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    id_cst_pis = models.ForeignKey(Tbcst, models.DO_NOTHING, db_column='id_cst_pis', related_name='tributacoesPis')
    aliq_pis = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    id_cst_cofins = models.ForeignKey(Tbcst, models.DO_NOTHING, db_column='id_cst_cofins',
                                      related_name='tributacoesCofins')
    aliq_cofins = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    id_contribuinte = models.ForeignKey(Tbcontribuinte, models.DO_NOTHING, db_column='id_contribuinte')
    id_cfop = models.ForeignKey(Tbcfop, models.DO_NOTHING, db_column='id_cfop')
    modbcicms = models.IntegerField(blank=True, null=True)
    pcredbcicms = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbtributacao'
        unique_together = (('id_contribuinte', 'codigo'), ('id_contribuinte', 'descricao'),)
        verbose_name = 'tributação'
        verbose_name_plural = 'tributações'

    def __str__(self):
        return self.descricao

    def list_display(self):
        return [
            'codigo',
            'descricao',
        ]


class Tbuf(CustomModel):
    id_uf = models.AutoField(primary_key=True)
    sigla = models.CharField(unique=True, max_length=2)
    descricao = models.CharField('descrição', max_length=60)
    ibge = models.CharField(unique=True, max_length=2)

    class Meta:
        managed = False
        db_table = 'tbuf'
        verbose_name = 'unidade federativa'
        verbose_name_plural = 'unidades federativas'

    def __str__(self):
        return self.sigla

    @staticmethod
    def get_add_url():
        return r('create_uf')

    def get_edit_url(self):
        return r('update_uf', self.pk)

    def get_delete_url(self):
        return r('delete_uf', self.pk)

    def list_display(self):
        return [
            'sigla',
            'descricao',
            'ibge',
        ]


class TbunidadeMedida(CustomModel):
    id_unidade_medida = models.AutoField(primary_key=True)
    sigla = models.CharField(unique=True, max_length=6)
    descricao = models.CharField(unique=True, max_length=30)

    class Meta:
        managed = False
        db_table = 'tbunidade_medida'
        verbose_name = 'unidade de medida'
        verbose_name_plural = 'unidades de medida'

    def __str__(self):
        return self.descricao

    @staticmethod
    def get_add_url():
        return r('create_unidade_medida')

    def get_edit_url(self):
        return r('update_unidade_medida', self.pk)

    def get_delete_url(self):
        return r('delete_unidade_medida', self.pk)

    def list_display(self):
        return [
            'sigla',
            'descricao',
        ]


class Tbusuario(AbstractBaseUser, PermissionsMixin, CustomModel):
    id_usuario = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=120, blank=True, null=True)
    email = models.CharField(unique=True, max_length=120)
    senha = models.CharField(max_length=120)
    usuario_contabil = models.CharField(max_length=1)
    usuario_suporte_sistema = models.CharField(max_length=1)
    is_active = models.BooleanField(
        _('active'),
        default=True,
        help_text=_(
            'Designates whether this user should be treated as active. '
            'Unselect this instead of deleting accounts.'
        ),
    )
    is_staff = models.BooleanField(
        _('staff status'),
        default=False,
        help_text=_('Designates whether the user can log into this admin site.'),
    )
    id_contribuinte = models.ForeignKey(Tbcontribuinte, models.DO_NOTHING, db_column='id_contribuinte', blank=True,
                                        null=True)

    objects = TbusuarioManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['usuario_contabil', 'usuario_suporte_sistema']

    class Meta:
        managed = False
        db_table = 'tbusuario'

    def get_short_name(self):
        return self.nome

    def get_full_name(self):
        return self.nome


class TbusuarioContribuinte(CustomModel):
    id_usuario = models.ForeignKey(Tbusuario, models.DO_NOTHING, db_column='id_usuario', primary_key=True)
    id_contribuinte = models.ForeignKey(Tbcontribuinte, models.DO_NOTHING, db_column='id_contribuinte')

    class Meta:
        managed = False
        db_table = 'tbusuario_contribuinte'
        unique_together = (('id_usuario', 'id_contribuinte'),)


# class Tbviewlog(CustomModel):
#     nome_tabela = models.CharField(primary_key=True, max_length=60)
#     nome_campo = models.CharField(max_length=60)
#     descricao_campo = models.CharField(max_length=60, blank=True, null=True)
#     formula = models.CharField(max_length=4000, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tbviewlog'
#         unique_together = (('nome_tabela', 'nome_campo'),)


# class Tmpuser(CustomModel):
#     pid = models.BigIntegerField(primary_key=True)
#     usuario = models.CharField(max_length=120, blank=True, null=True)
#     usuario_pc = models.CharField(max_length=100, blank=True, null=True)
#     nome_pc = models.CharField(max_length=100, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tmpuser'
