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
