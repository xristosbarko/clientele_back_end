from rest_framework import serializers
from .models import Tech

class TechSerializer(serializers.ModelSerializer):
	class Meta:
		model = Tech
		fields = (
			'id',
			'last_name',
			'first_name',
			'phone_number',
		)

	def create(self, validated_data):
		last_name = validated_data["last_name"].strip().replace(" ", "").lower()
		first_name = validated_data["first_name"].strip().replace(" ", "").lower()
		slug = last_name + first_name
		validated_data["slug"] = slug
		tech = Tech.objects.create(**validated_data)
		return tech

	def update(self, instance, validated_data):
		last_name = validated_data["last_name"].strip().replace(" ", "").lower()
		first_name = validated_data["first_name"].strip().replace(" ", "").lower()
		slug = last_name + first_name
		validated_data["slug"] = slug
		instance.slug = validated_data.get('slug', "")
		instance.last_name = validated_data.get('last_name', "")
		instance.first_name = validated_data.get('first_name', "")
		instance.phone_number = validated_data.get('phone_number', "")
		instance.save()
		return instance