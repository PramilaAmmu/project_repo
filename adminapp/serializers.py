from rest_framework.serializers import ModelSerializer

from adminapp.models import * 

class CreateUserSerializer(ModelSerializer):
	class Meta:
		model = CreateUser
		fields = '__all__'


class imagesSerializer(ModelSerializer):
	class Meta:
		model = images
		fields = '__all__'


class uploadedFileDetailsSerializer(ModelSerializer):
	class Meta:
		model = uploadedFileDetails
		fields = '__all__'
