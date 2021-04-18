from rest_framework import status

from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

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
            return Response(data=serializer.errors ,status=status.HTTP_400_BAD_REQUEST)


class AnnoncsView(APIView):
    def get(self, request):
        anns = Announcement.objects.all()
        serializer = AnnouncementSerializer(anns, many=True).data
        return Response(serializer)

    def post(self, request):
        if not request.user.is_authenticated:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
        serializer = WriteAnnouncementSerializer(data=request.data)
        print(dir(serializer))
        if serializer.is_valid():
            annon = serializer.save(author=request.user)
            annon_serializer = AnnouncementSerializer(annon).data
            return Response(data=annon_serializer, status=status.HTTP_201_CREATED)
        else:
            return Response(data=serializer.errors ,status=status.HTTP_400_BAD_REQUEST)


class ListAnnoncementView(ListAPIView):
    queryset = Announcement.objects.all()
    serializer_class = AnnouncementSerializer

class SeeAnnouncmentView(RetrieveAPIView):
    queryset = Announcement.objects.all()
    serializer_class = BigAnnouncementSerializer

class AnnoncView(APIView):
    def get_annon(self, pk):
        try:
            annon = Announcement.objects.get(pk=pk)
            return annon
        except Announcement.DoesNotExist:
            return None

    def get(self, request, pk):
        annon = self.get_annon(pk)
        if annon is not None:
            serializer = AnnouncementSerializer(annon).data
            return Response(serializer)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def put(self, request, pk):
        annon = self.get_annon(pk)
        if annon is not None:
            if annon.author != request.user:
                return Response(status=status.HTTP_401_UNAUTHORIZED)
            serializer = WriteAnnouncementSerializer(annon, data=request.data, partial=True)
            #print(serializer.is_valid(), serializer.errors)
            if serializer.is_valid():
                annon= serializer.save()
                return Response(AnnouncementSerializer(annon).data, status=status.HTTP_200_OK)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk):
        annon = self.get_annon(pk)
        if annon is not None:
            if annon.author != request.user:
                return Response(status=status.HTTP_401_UNAUTHORIZED)
            annon.delete()
            return Response(status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)
