from rest_framework import serializers
from .models import Article


class ArticleSerializer(serializers.ModelSerializer):
    author = serializers.CharField(max_length=250, read_only=True)

    class Meta:
        model = Article
        fields = ['id', 'title', 'content', 'created', 'author']
