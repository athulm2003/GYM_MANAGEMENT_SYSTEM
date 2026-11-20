from rest_framework import serializers
from django.contrib.auth.models import User
from BeFit.models import MemberShipDb

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['id','username','email','password']

    def  create(self, validated_data):
        return User.objects.create_user(**validated_data)

class MemberShipSerializer(serializers.ModelSerializer):
    class Meta:
        model = MemberShipDb
        fields = "__all__"
        read_only_fields = ['id','created_at', 'updated_at']