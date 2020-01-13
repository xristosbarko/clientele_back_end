from rest_framework import serializers
from .models import Device

class DeviceListSerializer(serializers.ModelSerializer):
	class Meta:
		model = Device
		fields = (
			'id',
			'name',
			'app',
		)

class DeviceSerializer(serializers.ModelSerializer):
	class Meta:
		model = Device
		fields = (
			'id',
			'name',
			'app',
		)

class Choice(object):
	def __init__(self, id, name):
		self.id = id
		self.name = name

class ChoiceSerializer(serializers.Serializer):
	id = serializers.IntegerField(max_value=9)
	name = serializers.CharField(max_length=20)