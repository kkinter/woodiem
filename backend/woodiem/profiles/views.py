from config.settings.local import DEFAULT_FROM_EMAIL
from django.contrib.auth import get_user_model
from django.core.mail import send_mail
from django.shortcuts import get_object_or_404
from rest_framework import generics, status
from rest_framework.exceptions import NotFound
from rest_framework.parsers import MultiPartParser
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .exceptions import CantFollowYourself
from .models import Profile
from .pagination import ProfilePagination
from .renderers import ProfileJSONRenderer, ProfilesJSONRenderer
from .serializers import (
    FollowingSerializer,
    ProfileSerializer,
    UpdateProfileSerializer,
)

User = get_user_model()


class ProfileListAPIView(generics.ListAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    pagination_class = ProfilePagination
    renderer_classes = (ProfilesJSONRenderer,)


class ProfileDetailAPIView(generics.RetrieveAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = ProfileSerializer
    renderer_classes = (ProfileJSONRenderer,)

    def get_queryset(self):
        queryset = Profile.objects.select_related("user")
        return queryset

    def get_object(self):
        user = self.request.user
        profile = self.get_queryset().get(user=user)
        return profile


class UpdateProfileAPIView(generics.RetrieveAPIView):
    serializer_class = UpdateProfileSerializer
    permission_classes = (IsAuthenticated,)
    parser_classes = (MultiPartParser,)
    renderer_classes = (ProfileJSONRenderer,)

    def get_object(self):
        profile = self.request.user.profile
        return profile

    def patch(self, requset, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=requset.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)


class FollowerListView(generics.ListAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = FollowingSerializer

    def get_queryset(self):
        user = self.request.user
        profile = get_object_or_404(Profile, user=user)
        return profile.followers.all()

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        formatted_response = {
            "status_code": status.HTTP_200_OK,
            "followers_count": queryset.count(),
            "followers": serializer.data,
        }
        return Response(formatted_response)


class FollowingListView(generics.ListAPIView):
    serializer_class = FollowingSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        user_id = self.kwargs["user_id"]
        profile = get_object_or_404(Profile, user__id=user_id)
        following_profiles = profile.following.all()
        return [p.user for p in following_profiles]

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        formatted_response = {
            "status_code": status.HTTP_200_OK,
            "following_count": queryset.count(),
            "users_i_follow": serializer.data,
        }
        return Response(formatted_response)


class FollowAPIView(APIView):
    def post(self, request, user_id, format=None):
        try:
            follower = request.user.profile
            profile = Profile.objects.get(user__id=user_id)

            if profile == follower:
                raise CantFollowYourself()

            if follower.check_following(profile):
                formatted_response = {
                    "status_code": status.HTTP_400_BAD_REQUEST,
                    "message": f"{profile.user.first_name} {profile.user.last_name} 님을 이미 팔로우하고 있습니다.",
                }
                return Response(formatted_response, status=status.HTTP_400_BAD_REQUEST)

            follower.follow(profile)
            subject = "새로운 팔로워가 생겼습니다."
            message = f"안녕하세요, {profile.user.first_name}님! {follower.user.first_name} {follower.user.last_name} 님이 회원님을 팔로우하기 시작했습니다."
            from_email = DEFAULT_FROM_EMAIL
            recipient_list = [profile.user.email]
            send_mail(subject, message, from_email, recipient_list, fail_silently=True)

            return Response(
                {
                    "status_code": status.HTTP_200_OK,
                    "message": f"{profile.user.first_name} {profile.user.last_name} 님을 팔로우하기 시작했습니다.",
                },
                status=status.HTTP_200_OK,
            )
        except Profile.DoesNotExist:
            raise NotFound("존재하지 않는 프로필은 팔로우할 수 없습니다.")


class UnfollowAPIView(APIView):
    def post(self, request, user_id, *args, **kwargs):
        user_profile = request.user.profile
        try:
            profile = Profile.objects.get(user__id=user_id)

            if not user_profile.check_following(profile):
                formatted_response = {
                    "status_code": status.HTTP_400_BAD_REQUEST,
                    "message": f"{profile.user.first_name} {profile.user.last_name} 님을 팔로우하고 있지 않아 언팔로우할 수 없습니다.",
                }
                return Response(formatted_response, status=status.HTTP_400_BAD_REQUEST)

            user_profile.unfollow(profile)
            formatted_response = {
                "status_code": status.HTTP_200_OK,
                "message": f"{profile.user.first_name} {profile.user.last_name} 님을 언팔로우했습니다.",
            }
            return Response(formatted_response, status=status.HTTP_200_OK)

        except Profile.DoesNotExist:
            raise NotFound("존재하지 않는 프로필은 언팔로우할 수 없습니다.")
