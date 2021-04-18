from rest_framework import serializers
from .models import Announcement
from accounts.serializers import UserSerializer

class AnnouncementSerializer(serializers.ModelSerializer):
    author = UserSerializer()

    class Meta:
        model = Announcement
        fields = ("company", "title", "smodifyDtm", "regDt", "closeDt" ,"author")
        # validate 되지 않아야 될 필드
        # modelserializer 에서만 동작
        read_only_fields = ('author', 'id', 'created', 'updated')

class BigAnnouncementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Announcement
        fields = ("__all__")

class WriteAnnouncementSerializer(serializers.Serializer):
    company = serializers.CharField(max_length=100)
    title = serializers.CharField(max_length=100)
    career = serializers.CharField(max_length=100)
    regDt = serializers.DateField()
    closeDt = serializers.DateField()

    def create(self, validated_data):
        print(validated_data)
        #print(**validated_data)
        return Announcement.objects.create(**validated_data)

    def validate_title(self, title):
        if title == '내용 없음':
            raise serializers.ValidationError("내용 없음은 사용할 수 없습니다.")
        else:
            return title

    def validate(self, data):
        # update
        if self.instance:
            # update 시 regDt, closeDt를 수정 하지 않는 경우
            regDt = data.get("regDt", self.instance.regDt)
            closeDt = data.get("closeDt", self.instance.closeDt)
        # create
        else:
            regDt = data.get('regDt')
            closeDt = data.get('closeDt')

        if regDt == closeDt:
            raise serializers.ValidationError("closeDt는 나중이 되어야 한다")
        return data


    def update(self, instance, validated_data):
        print(instance, validated_data)
        instance.company = validated_data.get("company", instance.company)
        instance.title = validated_data.get("title", instance.title)
        instance.career = validated_data.get("career", instance.career)
        instance.regDt = validated_data.get("regDt", instance.regDt)
        instance.closeDt = validated_data.get("closeDt", instance.closeDt)
        instance.save()
        return instance
