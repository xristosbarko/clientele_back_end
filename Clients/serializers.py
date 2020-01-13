from rest_framework import serializers
from .models import Client, Phone

class StringListField(serializers.ListField):
	child = serializers.CharField()

class ClientListSerializer(serializers.ModelSerializer):
	class Meta:
		model = Client
		fields = (
			'id',
			'last_name',
			'first_name',
		)

class ClientCreateUpdateSerializer(serializers.ModelSerializer):
	phone_numbers_pop = StringListField(write_only=True)

	class Meta:
		model = Client
		fields = (
			'id',
			'last_name',
			'first_name',
			'city',
			'address',
			'phone_numbers_pop',
			'fax',
			'email',
			'info',
			'responsible',
		)

	def create(self, validated_data):
		last_name = validated_data["last_name"].strip().replace(" ", "").lower()
		first_name = validated_data["first_name"].strip().replace(" ", "").lower()
		slug = last_name + first_name
		validated_data["slug"] = slug

		phone_numbers = validated_data.pop('phone_numbers_pop')

		client = Client.objects.create(**validated_data)

		for phone_number in phone_numbers:
			Phone.objects.create(client_id=client, phone_number=phone_number)
		return client

	def update(self, instance, validated_data):
		last_name = validated_data["last_name"].strip().replace(" ", "").lower()
		first_name = validated_data["first_name"].strip().replace(" ", "").lower()
		slug = last_name + first_name
		validated_data["slug"] = slug

		validated_phone_numbers = validated_data.pop('phone_numbers_pop')

		instance.slug = validated_data.get('slug', "")
		instance.last_name = validated_data.get('last_name', "")
		instance.first_name = validated_data.get('first_name', "")
		instance.city = validated_data.get('city', "")
		instance.address = validated_data.get('address', "")
		instance.fax = validated_data.get('fax', "")
		instance.email = validated_data.get('email', "")
		instance.info = validated_data.get('info', "")
		instance.responsible = validated_data.get('responsible', "")

		model_phone_numbers = Phone.objects.filter(client_id=instance.id)

		for validated_phone in validated_phone_numbers:
			if validated_phone not in [model_phone.phone_number for model_phone in model_phone_numbers]:
				Phone.objects.create(client_id=instance, phone_number=validated_phone)
		for model_phone in model_phone_numbers:
			if model_phone.phone_number not in validated_phone_numbers:
				model_phone.delete()

		instance.save()
		return instance


class ClientDetailsSerializer(serializers.ModelSerializer):
	phone_numbers = serializers.SlugRelatedField(slug_field='phone_number', read_only=True, many=True)

	class Meta:
		model = Client
		fields = (
			'id',
			'last_name',
			'first_name',
			'city',
			'address',
			'phone_numbers',
			'fax',
			'email',
			'info',
			'responsible',
		)