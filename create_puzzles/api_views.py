from rest_framework import viewsets
from rest_framework.response import Response
from .models import Item
from rest_framework.serializers import ModelSerializer

class ItemSerializer(ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'

class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

    # Override retrieve to handle both ID and difficulty level
    def retrieve(self, request, pk=None):
     
        if pk.isdigit():
            return super().retrieve(request, pk)
        
        elif pk.lower() in ["easy", "medium", "hard"]:
            items = Item.objects.filter(difficulty__iexact=pk)
            serializer = self.get_serializer(items, many=True)
            return Response(serializer.data)
        
     
        else:
            return Response({"error": "Invalid parameter"}, status=400)