from rest_framework import serializers
from .models import Item

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'
        
class LevelItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ['id', 'difficulty', 'created_by', 'updated_by', 'active']        