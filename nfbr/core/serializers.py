from rest_framework import serializers
from .models import *


class TbusuarioSerializer(serializers.ModelSerializer):
    contribuinte = serializers.ReadOnlyField(source='id_contribuinte.__str__', read_only=True)

    class Meta:
        model = Tbusuario
        fields = ('email', 'contribuinte', 'get_avatar_url')


class TbcontribuinteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tbcontribuinte
        fields = '__all__'


class TbunidadeMedidaSerializer(serializers.ModelSerializer):

    class Meta:
        model = TbunidadeMedida
        fields = '__all__'


class TbunidadeMedidaLookupSerializer(serializers.ModelSerializer):
    id = serializers.PrimaryKeyRelatedField(source='pk', read_only=True)
    text = serializers.ReadOnlyField(source='__str__', read_only=True)

    class Meta:
        model = TbunidadeMedida
        fields = ('id', 'text')


class TbufSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tbuf
        fields = '__all__'


class TbcstSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tbcst
        fields = '__all__'


class TbcstLookupSerializer(serializers.ModelSerializer):
    id = serializers.PrimaryKeyRelatedField(source='pk', read_only=True)
    text = serializers.ReadOnlyField(source='__str__', read_only=True)

    class Meta:
        model = Tbcst
        fields = ('id', 'text')


class TbncmSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tbncm
        fields = '__all__'


class TbncmLookupSerializer(serializers.ModelSerializer):
    id = serializers.PrimaryKeyRelatedField(source='pk', read_only=True)
    text = serializers.ReadOnlyField(source='__str__', read_only=True)

    class Meta:
        model = Tbncm
        fields = ('id', 'text')


class TbcfopSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tbcfop
        fields = '__all__'


class TbcfopLookupSerializer(serializers.ModelSerializer):
    id = serializers.PrimaryKeyRelatedField(source='pk', read_only=True)
    text = serializers.ReadOnlyField(source='__str__', read_only=True)

    class Meta:
        model = Tbcfop
        fields = ('id', 'text')


class TbprodutoSerializer(serializers.ModelSerializer):
    unidade_medida = serializers.ReadOnlyField(source='id_unidade_medida.__str__', read_only=True)
    ncm = serializers.ReadOnlyField(source='id_ncm.__str__', read_only=True)
    cst_icms = serializers.ReadOnlyField(source='id_cst_icms.__str__', read_only=True)
    cst_pis = serializers.ReadOnlyField(source='id_cst_pis.__str__', read_only=True)
    cst_cofins = serializers.ReadOnlyField(source='id_cst_cofins.__str__', read_only=True)
    cfop = serializers.ReadOnlyField(source='id_cfop.__str__', read_only=True)

    def create(self, validated_data):
        print("createeeeee")
        obj = Tbproduto.objects_per_user.create(**validated_data)
        obj.save()
        return obj

    class Meta:
        model = Tbproduto
        # fields = '__all__'
        exclude = ('id_contribuinte',)
