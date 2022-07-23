from rest_framework import serializers
from .models import Videos
class PostsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Videos
        fields = '__all__'