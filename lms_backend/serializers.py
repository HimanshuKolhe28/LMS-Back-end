from rest_framework import serializers


from lms_backend.models import Student
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User  
        fields = ['id', 'username', 'email', 'first_name', 'last_name']


class StudentSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    user_id = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), source='user')
    
    class Meta:
        model = Student  
        fields = "__all__"