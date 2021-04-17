from rest_framework import serializers
from .models import Announcement
from accounts.serializers import UserSerializer

class AnnouncementSerializer(serializers.ModelSerializer):
    author = UserSerializer()

    class Meta:
        model = Announcement
        fields = ("company", "title", "smodifyDtm", "author")

class BigAnnouncementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Announcement
        fields = ("__all__")

class WriteAnnouncementSerializer(serializers.Serializer):
    company = serializers.CharField(max_length=100)
    title = serializers.CharField(max_length=100)
    career = serializers.CharField(max_length=100)
    regDt = serializers.DateField()

    def create(self, validated_data):
        print(validated_data)
        #print(**validated_data)
        return Announcement.objects.create(**validated_data)
