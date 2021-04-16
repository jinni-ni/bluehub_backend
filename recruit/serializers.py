from rest_framework import serializers

class AnnouncementSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=100)
    company = serializers.CharField(max_length=100)
    regDt = serializers.DateField()
    closeDt = serializers.DateField()
    smodifyDtm = serializers.DateField()
