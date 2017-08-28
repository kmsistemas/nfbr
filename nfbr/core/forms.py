from django.contrib import admin
from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField

from nfbr.core.models import Tbusuario, Tbcontribuinte, Tbcfop, Tbcst, TbentradaNf, Tbproduto, Tbncm, Tbuf, \
    TbunidadeMedida, Tbpessoa


admin.autodiscover()


class UserCreationForm(forms.ModelForm):
    """A form for creating new users. Includes all the required
    fields, plus a repeated password."""
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = Tbusuario
        fields = ('email', 'nome')

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError(_("Passwords don't match"))
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super(UserCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class UserChangeForm(forms.ModelForm):
    """A form for updating users. Includes all the fields on
    the user, but replaces the password field with admin's
    password hash display field.
    """
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = Tbusuario
        fields = ('email', 'password', 'nome')

    def clean_password(self):
        # Regardless of what the user provides, return the initial value.
        # This is done here, rather than on the field, because the
        # field does not have access to the initial value
        return self.initial["password"]


class TbcontribuinteForm(forms.ModelForm):
    senha_email_nfce = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Tbcontribuinte
        fields = '__all__'


class TbunidadeMedidaForm(forms.ModelForm):
    class Meta:
        model = TbunidadeMedida
        fields = '__all__'


class TbncmForm(forms.ModelForm):
    class Meta:
        model = Tbncm
        fields = '__all__'


class TbcfopForm(forms.ModelForm):
    class Meta:
        model = Tbcfop
        fields = '__all__'


class TbcstForm(forms.ModelForm):
    class Meta:
        model = Tbcst
        fields = '__all__'


class TbentradaNfForm(forms.ModelForm):
    class Meta:
        model = TbentradaNf
        fields = '__all__'


class TbpessoaForm(forms.ModelForm):
    class Meta:
        model = Tbpessoa
        exclude = ('id_contribuinte', )


class TbprodutoForm(forms.ModelForm):
    # id_ncm = forms.ModelChoiceField(queryset=Tbncm.objects.all(),
    #                                 widget=forms.TextInput)
    # id_ncm = forms.CharField(
    #     label='Type the name of a fruit (AutoCompleteWidget)',
    #     widget=AutoCompleteWidget(TbncmLookup),
    #     required=False,
    # )
    # db_field = Tbproduto._meta.get_field('id_ncm')
    # id_ncm = forms.ModelChoiceField(
    #     queryset=Tbncm.objects.all(),
    #     widget=ForeignKeyRawIdWidget(db_field.rel, admin.site),
    #     required=False
    # )
    # id_ncm = forms.ChoiceField(
    #     widget=ModelSelect2Widget(
    #         model=Tbncm,
    #         search_fields=['codigo__icontains']
    #     )
    # )

    class Meta:
        model = Tbproduto
        exclude = ('id_contribuinte',)
        # fields = ('codigo', 'id_ncm')
        # widgets = {
        #     'id_ncm': Select2Widget
        # }

    # class Media:
    #     js = ('admin/js/admin/RelatedObjectLookups.js',)

    def __init__(self, *args, **kwargs):
        self.id_contribuinte = None
        if 'request' in kwargs:
            request = kwargs.pop('request')
            self.id_contribuinte = request.user.id_contribuinte

        super(TbprodutoForm, self).__init__(*args, **kwargs)

        if self.id_contribuinte is None:
            self.id_contribuinte = self.instance.id_contribuinte

        if self.id_contribuinte.regime_tributario == '3':
            self.fields['id_cst_icms'].queryset = Tbcst.objects.filter(tipo='N')
        else:
            self.fields['id_cst_icms'].queryset = Tbcst.objects.filter(tipo='S')
        self.fields['id_cst_pis'].queryset = Tbcst.objects.filter(tipo='C')
        self.fields['id_cst_cofins'].queryset = Tbcst.objects.filter(tipo='C')


class TbufForm(forms.ModelForm):
    class Meta:
        model = Tbuf
        fields = '__all__'
