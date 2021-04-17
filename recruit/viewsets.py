from rest_framework import viewsets
from .models import Announcement
from .serializers import BigAnnouncementSerializer

class AnnonceViewSet(viewsets.ModelViewSet):
    queryset = Announcement.objects.all()
    serializer_class = BigAnnouncementSerializer
