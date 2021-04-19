from rest_framework import serializers
from .models import Announcement
from accounts.serializers import UserSerializer

class AnnouncementSerializer(serializers.ModelSerializer):
    author = UserSerializer()
    is_favs = serializers.SerializerMethodField("is_favs_field")

    class Meta:
        model = Announcement
        fields = ("title", "company", "basicAddr", "sal", "closeDt", "regDt", "explain", "is_favs", "author")

        # no validate
        read_only_fields = ('author', 'id', 'created', 'updated')

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

    def is_favs_field(self, post):
        if 'request' in self.context:
            user = self.context["request"].user
            return post.like_user_set.filter(pk=user.pk).exists()
        return False
