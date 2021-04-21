from rest_framework import serializers
from .models import Announcement
from accounts.serializers import UserSerializer

class AnnouncementSerializer(serializers.ModelSerializer):
    author = UserSerializer()
    is_favs = serializers.SerializerMethodField()

    class Meta:
        model = Announcement
        fields = ("id", "title", "company", "basicAddr", "sal", "regDt", "closeDt", "explain", "region", "is_favs", "author")

        # no validate
        read_only_fields = ('author', 'created', 'updated')

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

        if regDt > closeDt:
            raise serializers.ValidationError("등록일자와 마감일자를 확인해주세요")

        return data

    def get_is_favs(self, obj):
        request = self.context.get('request')
        if request:
            user = request.user
            if user.is_authenticated:
                return obj in user.favs.all()
        return False
