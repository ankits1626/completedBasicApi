from rest_framework import serializers
from profiles_api import models

class HelloSerializer(serializers.Serializer):
    
    name = serializers.CharField(max_length=10)


class HelloSerializer2(serializers.Serializer):
    email = serializers.EmailField(max_length=255)
    dob = serializers.DateField()
    is_Active = serializers.BooleanField(default=False)


class UserProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.UserProfile
        fields = ('id','email', 'name', 'password')
        extra_kwargs ={
            'password':{
                'write_only' : True,
                'style':{'input_type' : 'password'}
            }
        }

    def create(self, validated_data):
        user = models.UserProfile.objects.create_user(
            email=validated_data['email'],
            name=validated_data['name'],
            password=validated_data['password'],
        )
        return user

class ProfileFeedItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.ProfileFeedItem
        fields = ('id', 'user_profile', 'status_text', 'created_on')
        extra_kwargs = {'user_profile' :{'read_only' : True}}

class PostItemSeializer(serializers.ModelSerializer):

    class Meta:
        model = models.Post
        fields = ('id','user_profile', 'post_content', 'is_published', 'created_on')
        extra_kwargs = {'user_profile' :{'read_only' : True}}