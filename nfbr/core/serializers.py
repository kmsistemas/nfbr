from rest_framework import serializers
from .models import *


class TbusuarioSerializer(serializers.ModelSerializer):
    contribuinte = serializers.ReadOnlyField(source='id_contribuinte.__str__', read_only=True)

    class Meta:
        model = Tbusuario
        fields = ('email', 'contribuinte', 'get_avatar_url')


class TbunidadeMedidaSerializer(serializers.ModelSerializer):

    class Meta:
        model = TbunidadeMedida
        fields = '__all__'


class TbufSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tbuf
        fields = '__all__'


class TbcstSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tbcst
        fields = '__all__'


class TbncmSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tbncm
        fields = '__all__'


class TbcfopSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tbcfop
        fields = '__all__'


class TbprodutoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tbproduto
        # fields = '__all__'
        exclude = ('id_contribuinte',)
