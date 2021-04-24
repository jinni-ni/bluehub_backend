from rest_framework import permissions
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.viewsets import ModelViewSet

from .models import Announcement
from .serializers import AnnouncementSerializer
from .permissions import IsSelf


class AnnouncementViewSet(ModelViewSet):
    queryset = Announcement.objects.all()
    serializer_class = AnnouncementSerializer

    def get_permissions(self):
        # print(self.action)
        if self.action == 'list' or self.action == 'retrieve':
            permission_classes = [permissions.AllowAny]
        elif self.action == 'create':
            permission_classes = [permissions.IsAdminUser]
        else:
            permission_classes = [IsSelf]

        return [permission() for permission in permission_classes]

    @action(detail=False)
    def search(self, request):
        # search 로 통합
        #title = request.GET.get('title', None)
        #company = request.GET.get('company', None)
        search = request.GET.get('search', None)
        basicAddr = request.GET.get('basicAddr', None)
        sal = request.GET.get('sal', None)
        closeDt = request.GET.get('closeDt', None)

        filter_kwargs = {}

        if search is not None:
            filter_kwargs["title__icontains"] = search
            filter_kwargs["company__icontains"] = search

        if basicAddr is not None:
            filter_kwargs["basicAddr__icontains"] = basicAddr

        if sal is not None:
            filter_kwargs["sal__gte"] = sal

        if closeDt is not None:
            filter_kwargs["closeDt__gte"] = closeDt

        paginator = self.paginator
        paginator.page_size = 20

        try:
            anno = Announcement.objects.filter(**filter_kwargs)
        except ValueError:
            anno = Announcement.objects.all()

        results = paginator.paginate_queryset(anno, request)
        serializers = AnnouncementSerializer(results, many=True, context={'request': request})
        return paginator.get_paginated_response(serializers.data)
