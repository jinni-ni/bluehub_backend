from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Announcement
from .serializers import AnnouncementSerializer


@api_view(["GET"])
def list_announcement(request):
    annon = Announcement.objects.all()
    serialized_annon = AnnouncementSerializer(annon, many=True)
    return Response(data=serialized_annon.data)


