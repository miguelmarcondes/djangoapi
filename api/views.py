from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from .models import Culprit
from .serializers import CulpritSerializer
from .utils import fbiRequest
from rest_framework.views import APIView

class CulpritList(generics.ListCreateAPIView):
    serializer_class = CulpritSerializer

    def get_queryset(self):
        queryset = Culprit.objects.all()
        return queryset


class CulpritDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CulpritSerializer
    queryset = Culprit.objects.all()

class CulpritInsert(APIView):
    serializer_class = CulpritSerializer

    def post(self, request, *args, **kwargs):
        df = fbiRequest.fetch_data_from_fbi_api()
        serialized_data = CulpritSerializer(data=df.to_dict('records'), many=True)

        if serialized_data.is_valid():
            serialized_data.save()
            return Response(serialized_data.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serialized_data.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, *args, **kwargs):
        return Response({"detail": "Method \"GET\" not allowed."}, status=status.HTTP_405_METHOD_NOT_ALLOWED)