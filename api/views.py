from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from .models import Culprit
from .serializers import CulpritSerializer

class CulpritList(generics.ListCreateAPIView):
    serializer_class = CulpritSerializer

    def get_queryset(self):
        queryset = Culprit.objects.all()
        return queryset
    
    def post(self, request, *args, **kwargs):
        serialized_data = CulpritSerializer(data=request.data, many=True)

        if serialized_data.is_valid():
            serialized_data.save()
            return Response(serialized_data.data, status=status.HTTP_201_CREATED)
        
        return Response(serialized_data.errors, status=status.HTTP_400_BAD_REQUEST)
    
class CulpritDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CulpritSerializer
    queryset = Culprit.objects.all()
