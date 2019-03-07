from rest_framework import serializers
from . models import Sofmodel

class SoftSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sofmodel
        user = serializers.ReadOnlyField(source='user.username')
        fields = '__all__'

        #fields = ('id','first_name','last_name','dob','email','url','created_date','address','user')


from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    sof = serializers.PrimaryKeyRelatedField(queryset=Sofmodel.objects.all())

    class Meta:
        model = User
        fields = ('id', 'username', 'sof')