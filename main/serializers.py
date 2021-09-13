from rest_framework import serializers

from main.models import News, ImageNews, Law, Publication, FavouriteLaws


class NewsListSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = 'id tittle publication_data image short_description'.split()

class ImageNewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImageNews
        fields = 'id image'.split()

class NewsItemSerializer(serializers.ModelSerializer):
    images = ImageNewsSerializer(many=True)

    class Meta:
        model = News
        fields = 'id tittle link full_description images'.split()

class FavouriteLawsSerializer(serializers.ModelSerializer):
    class Meta:
        model = FavouriteLaws
        fields = 'id name'.split()

class LawsByTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Law
        fields = 'id title text'.split()

class LawItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Law
        fields = 'id title text law_type'.split()

class PublicationsByTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publication
        fields = 'id title text file'.split()

class PublicationItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publication
        fields = 'id title text file types'.split()