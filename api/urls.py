from django.urls import path
from .views import CulpritList, CulpritDetail
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

urlpatterns = [
    path('api/', CulpritList.as_view()),
    path('api/<int:pk>/', CulpritDetail.as_view()),
    path('api/schema/', SpectacularAPIView.as_view(), name="schema"),
    path('api/schema/docs/', SpectacularSwaggerView.as_view(url_name='schema'))
]