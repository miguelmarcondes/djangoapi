from django.urls import path
from .views import CulpritList, CulpritDetail, CulpritInsert

urlpatterns = [
    path('', CulpritList.as_view(), name='culprit-list'),
    path('<int:pk>', CulpritDetail.as_view(), name='culprit-detail'),
    path('insert', CulpritInsert.as_view(), name='culprit-insert'),
]