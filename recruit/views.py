from rest_framework import status
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Announcement
from .serializers import AnnouncementSerializer, BigAnnouncementSerializer, WriteAnnouncementSerializer


@api_view(["GET", "POST"])
def ann_view(request):
    if request.method == 'GET':
        anns = Announcement.objects.all()
        serializer = AnnouncementSerializer(anns, many=True).data
        return Response(serializer)

    elif request.method == 'POST':
        if not request.user.is_authenticated:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
        serializer = WriteAnnouncementSerializer(data=request.data)
        print(dir(serializer))
        if serializer.is_valid():
            annon = serializer.save(author=request.user)
            annon_serializer = AnnouncementSerializer(annon).data
            return Response(data=annon_serializer, status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)


class ListAnnoncementView(ListAPIView):
    queryset = Announcement.objects.all()
    serializer_class = AnnouncementSerializer

class SeeAnnouncmentView(RetrieveAPIView):
    queryset = Announcement.objects.all()
    serializer_class = BigAnnouncementSerializer
