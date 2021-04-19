from rest_framework.routers import DefaultRouter
from . import views

app_name = "recruit"

router = DefaultRouter()
router.register("", views.AnnouncementViewSet)

urlpatterns = router.urls
