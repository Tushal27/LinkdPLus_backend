from rest_framework import serializers
from djoser.serializers import UserCreateSerializer
from django.contrib.auth import get_user_model
from posts.serializers import PostSerializer
User = get_user_model()

class UserSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        model = User
        fields = ['id', 'email', 'password','re_password']
        read_only_fields = ['id']

class ProfileSerializer(serializers.ModelSerializer):
    posts = PostSerializer(many=True, read_only=True)
    class Meta:
        model = User
        fields = ['id', 'avatar' , 'email', 'first_name','last_name','bio', 'posts']
        read_only_fields = ['id']

class UpdateProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'avatar', 'email', 'first_name','last_name','bio']
        read_only_fields = ['id']
    

class PasswordResetSerializer(serializers.Serializer):
    email = serializers.EmailField(source='user.email')
    old_password = serializers.CharField(source='user.email')
    new_password = serializers.CharField(source='user.email')
    confirm_password = serializers.CharField(source='user.email')

    def validate_old_password(self, value):
        user = self.context['request'].user
        if not user.check_password(value):
            raise serializers.ValidationError('Old password is incorrect.')
        return value
    def validate(self, data):
        if data['new_password'] != data['confirm_password'] :
            raise serializers.ValidationError('Passwords do not match')
        if  len(data['new_password']) < 8:
            raise serializers.ValidationError('Password must be at least 8 characters long.')
        
        if data['new_password'] == data['old_password']:
            raise serializers.ValidationError('New password cannot be the same as the old password.')
        return data
    def save(self, **kwargs):
        email=self.validated_data['email']
        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            raise serializers.ValidationError('User does not exist.')
        user.set_password(self.validated_data['new_password'])
        user.save()
        return user
    
    