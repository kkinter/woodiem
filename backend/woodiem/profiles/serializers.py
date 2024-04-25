from rest_framework import serializers

from .models import Profile


class ProfileSerializers(serializers.ModelSerializer):
    email = serializers.EmailField(source="user.email")
    name = serializers.SerializerMethodField()
    profile_image = serializers.SerializerMethodField()

    def get_profile_image(self, obj):
        return obj.profile_image.url

    def get_name(self, obj):
        return f"{obj.user.last_name}{obj.user.first_name}"

    class Meta:
        model = Profile
        fields = ["email", "name", "profile_image", "profile_image", "nickname", "bio"]


class UpdateProfileSerializers(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ["nickname", "bio", "profile_image"]


class FollowingSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField()

    class Meta:
        model = Profile
        fields = ["nickname", "name", "bio", "profile_image"]

    def get_name(self, obj):
        return f"{obj.user.last_name}{obj.user.first_name}"
