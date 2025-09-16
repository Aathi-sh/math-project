from rest_framework import viewsets
from .models import Item
from rest_framework.serializers import ModelSerializer

class TempSerializer(ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'
        
class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = TempSerializer        