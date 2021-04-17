from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.response import Response
from .models import Announcement
from .serializers import AnnouncementSerializer, BigAnnouncementSerializer


class ListAnnoncementView(ListAPIView):
    queryset = Announcement.objects.all()
    serializer_class = AnnouncementSerializer

class SeeAnnouncmentView(RetrieveAPIView):
    queryset = Announcement.objects.all()
    serializer_class = BigAnnouncementSerializer
