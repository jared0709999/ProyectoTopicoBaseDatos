from django.contrib.auth.models import User, Group
from core.models import *
from directorio.models import *
from expediente.models import*
from galeria.models import*
from politicas.models import*

# importar los demas modelos aquí
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']


class AreaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Area
        fields = ['nombre', 'rango', 'foto']

    def create(self, validated_data):
        return Area.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.nombre = validated_data.get('nombre', instance.nombre)
        instance.rango = validated_data.get('rango', instance.rango)
        instance.foto = validated_data.get('foto', instance.foto)
        instance.save()
        return instance

class RegistroSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Registro
        fields = ['nombre', 'apellido', 'seccion', 'area', 'ingreso', 'ingreso', 'nacimiento', 'curp', 'nss', 'telefono', 'direccion', 'type', 'gender', 'foto']

    def create(self, validated_data):
        return Registro.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.nombre = validated_data.get('nombre', instance.nombre)
        instance.apellido = validated_data.get('apellido', instance.apellido)
        instance.seccion = validated_data.get('seccion', instance.seccion)
        instance.area = validated_data.get('area', instance.area)
        instance.ingreso = validated_data.get('ingreso', instance.ingreso)
        instance.nacimiento = validated_data.get('nacimiento', instance.nacimiento)
        instance.curp = validated_data.get('curp', instance.curp)
        instance.nss = validated_data.get('nss', instance.nss)
        instance.telefono = validated_data.get('telefono', instance.telefono)
        instance.direccion = validated_data.get('direccion', instance.direccion)
        instance.type = validated_data.get('type', instance.type)
        instance.gender = validated_data.get('gender', instance.gender)
        instance.foto = validated_data.get('foto', instance.foto)
        instance.save()
        return instance

class EncargadoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Encargado
        fields = ['nombre', 'type', 'foto']

    def create(self, validated_data):
        return Encargado.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.nombre = validated_data.get('nombre', instance.nombre)
        instance.type = validated_data.get('type', instance.type)
        instance.foto = validated_data.get('foto', instance.foto)
        instance.save()
        return instance

class CompraSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Compra
        fields = ['nombre', 'descripcion']

    def create(self, validated_data):
        return Compra.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.nombre = validated_data.get('nombre', instance.nombre)
        instance.descripcion = validated_data.get('descripcion', instance.descripcion)
        instance.save()
        return instance

class AlmacenSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Almacen
        fields = ['nombre', 'ingreso', 'area']

    def create(self, validated_data):
        return Almacen.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.Compra = validated_data.get('Compra', instance.Compra)
        instance.ingreso = validated_data.get('ingreso', instance.descripcion)
        instance.area = validated_data.get('area', instance.area)
        instance.save()
        return instance

class FotoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Foto
        fields = ['fecha', 'type', 'detalles', 'foto']

    def create(self, validated_data):
        return Foto.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.fecha = validated_data.get('fecha', instance.fecha)
        instance.type = validated_data.get('type', instance.type)
        instance.detalles = validated_data.get('detalles', instance.detalles)
        instance.foto = validated_data.get('foto', instance.foto)
        instance.save()
        return instance

class ContenidoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Contenido
        fields = ['nombre', 'detalles', 'type', 'foto']

    def create(self, validated_data):
        return Contenido.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.nombre = validated_data.get('nombre', instance.nombre)
        instance.detalles = validated_data.get('detalles', instance.detalles)
        instance.type = validated_data.get('type', instance.type)
        instance.foto = validated_data.get('foto', instance.foto)
        instance.save()
        return instance