from rest_framework import serializers
from .models import crossMath, Difficulty,puzzleLevel

class puzzleSerializer(serializers.ModelSerializer):
    # Show difficulty text in API response
    difficulty_name = serializers.CharField(source='difficulty.name', read_only=True)
    # Accept numeric value (1,2,3) from API requests
    difficulty = serializers.IntegerField(write_only=True)

    class Meta:
        model = crossMath
        fields = [
            'id', 'title','description',  'difficulty', 'difficulty_name',
            'row', 'column', 'grid', 'solution', 'choices',
            'created_at', 'updated_at', 'created_by', 'updated_by', 'active'
        ]

    def create(self, validated_data):
        difficulty_value = validated_data.pop('difficulty')
        difficulty_obj = Difficulty.objects.get(value=difficulty_value)
        validated_data['difficulty'] = difficulty_obj
        return super().create(validated_data)

    def update(self, instance, validated_data):
        if 'difficulty' in validated_data:
            difficulty_value = validated_data.pop('difficulty')
            difficulty_obj = Difficulty.objects.get(value=difficulty_value)
            instance.difficulty = difficulty_obj
        return super().update(instance, validated_data)


class puzzleLevelSerializer(serializers.ModelSerializer):
    # Only show numeric difficulty
    difficulty = serializers.CharField(source='difficulty.name', read_only=True)

    class Meta:
        model = crossMath
        fields = ['id', 'difficulty', 'created_by', 'updated_by', 'active']
        
        
        
        
        
        
class levelTableSerializer(serializers.ModelSerializer):
    # Show difficulty text in API response
    difficulty_name = serializers.CharField(source='difficulty.name', read_only=True)
    # Accept numeric value (1,2,3) from API requests
    difficulty = serializers.IntegerField(write_only=True)

    class Meta:
        model = puzzleLevel
        fields = [
            'Level id', 'difficulty', 'difficulty_name',
            'created_at', 'updated_at', 'created_by', 'updated_by'
        ]

    def create(self, validated_data):
        difficulty_value = validated_data.pop('difficulty')
        difficulty_obj = Difficulty.objects.get(value=difficulty_value)
        validated_data['difficulty'] = difficulty_obj
        return super().create(validated_data)

    def update(self, instance, validated_data):
        if 'difficulty' in validated_data:
            difficulty_value = validated_data.pop('difficulty')
            difficulty_obj = Difficulty.objects.get(value=difficulty_value)
            instance.difficulty = difficulty_obj
        return super().update(instance, validated_data)
        
        