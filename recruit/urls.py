# from rest_framework.routers import DefaultRouter
# from django.urls import path
# from . import viewsets

# app_name = 'recruit'
#
# router = DefaultRouter()
# router.register("recruit", viewsets.AnnonceViewSet, basename='recruit')
# urlpatterns = router.urls

from django.urls import path
from . import views

app_name = 'recruit'
urlpatterns = [
    # path('', views.ListAnnoncementView.as_view()),
    path('fv/', views.ann_view),
    # path("<int:pk>/", views.SeeAnnouncmentView.as_view()),
    path('', views.AnnoncsView.as_view()),
    path("<int:pk>/", views.AnnoncView.as_view()),
]
