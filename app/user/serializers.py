"""Serializers for the user APIview"""
from django.contrib.auth import (
    get_user_model,
    authenticate
    )
from django.utils.translation import gettext as _
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    """Serializer for the user objects"""
    
    class Meta:
        model = get_user_model()
        fields = ['email','password','name']
        extra_kwargs = {'password':{'write_only':True,'min_length':5}}
        
    def create(self, validated_data):
        """Create and return a user with encripted pass"""
        return get_user_model().objects.create_user(**validated_data)
    
    def update(self, instance, validated_data):
        """uPDATE and return users"""
        password = validated_data.pop('password', None) #Firstly, the method checks if a password has been provided in the validated_data dictionary by using the pop() method to remove the password field from the dictionary. The None value is returned if the password field is not present.
        user = super().update(instance,validated_data)
        
        if password:
            user.set_password(password)
            user.save()
        return user


class AuthTokenSerializer(serializers.Serializer):
    """Serializer fro the user auth token"""
    email = serializers.EmailField()
    password = serializers.CharField(
         style={'input_type':'password'},
         trim_whitespace = False,
        )
    
    def validate(self, attrs):
        """Validate and authernticate the usuer"""
        email = attrs.get('email')
        password = attrs.get('password')
        user = authenticate(
            request=self.context.get('request'),
            username=email,
            password = password,  
        )
        
        if not user:
            msg = _('Unable to uthenticate with provided creds')
            raise serializers.ValidationError(msg,code='authrization')
        
        attrs['user'] = user
        return attrs