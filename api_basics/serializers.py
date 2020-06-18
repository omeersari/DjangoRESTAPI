from rest_framework import serializers
from .models import Article

"""
Serializer kullanma amacımız, sitemizde yer alan veriyi JSON şeklinde kullanabilmek ve tekrardan JSON gelen veriyi veritabanımıza
uygun şekilde dönüştürebilmek.
"""


# Serializer >>> Özelleştirmeye daha uygun olan. Fakat daha uzun ve yazımı karışık.

"""
class ArticleSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=100)
    author = serializers.CharField(max_length=100)
    email = serializers.EmailField(max_length=100)
    date = serializers.DateField()

    def create(self, validated_data):
        return Article.objects.create(validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.author = validated_data.get('author', instance.author)
        instance.email = validated_data.get('email', instance.email)
        instance.date = validated_data.get('date', instance.date)
        instance.save()
        return instance

"""

# ModelSerializer >>> Özelleştirme az fakat kısa ve etkili.

class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ['id', 'title', 'author']