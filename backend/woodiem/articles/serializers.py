from rest_framework import serializers

from woodiem.profiles.serializers import ProfileSerializers

from .models import Article


class ArticleSerializer(serializers.ModelSerializer):
    author = ProfileSerializers(source="author.profile", read_only=True)

    class Meta:
        model = Article
        fields = "__all__"
