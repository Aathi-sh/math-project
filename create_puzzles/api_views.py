from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import Item, Difficulty,puzzleLevel
from .serializers import ItemSerializer, LimitedItemSerializer,levelTableSerializer

# Full table viewset
class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        difficulty = self.request.query_params.get('difficulty')
        if difficulty:
            if difficulty.isdigit():
                queryset = queryset.filter(difficulty__value=int(difficulty))
            else:
                queryset = queryset.filter(difficulty__name__iexact=difficulty)
        return queryset

    def list(self, request):
        items = self.get_queryset()
        serializer = self.get_serializer(items, many=True)
        return Response({
            "status": "success",
            "message": "Items retrieved successfully",
            "full_data": serializer.data
        }, status=status.HTTP_200_OK)

    def retrieve(self, request, pk=None):
        try:
            item = self.get_queryset().get(pk=pk)
            serializer = self.get_serializer(item)
            return Response({
                "status": "success",
                "message": "Item retrieved successfully",
                "full_data": [serializer.data]
            }, status=status.HTTP_200_OK)
        except Item.DoesNotExist:
            return Response({
                "status": "failed",
                "message": "Item not found",
                "full_data": []
            }, status=status.HTTP_404_NOT_FOUND)

    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            item = serializer.save()
            return Response({
                "status": "success",
                "message": "Item created successfully",
                "full_data": [serializer.data]
            }, status=status.HTTP_201_CREATED)
        return Response({
            "status": "failed",
            "message": "Item creation failed",
            "full_data": serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        try:
            item = self.get_queryset().get(pk=pk)
            serializer = self.get_serializer(item, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({
                    "status": "success",
                    "message": "Item updated successfully",
                    "full_data": [serializer.data]
                }, status=status.HTTP_200_OK)
            return Response({
                "status": "failed",
                "message": "Item update failed",
                "full_data": serializer.errors
            }, status=status.HTTP_400_BAD_REQUEST)
        except Item.DoesNotExist:
            return Response({
                "status": "failed",
                "message": "Item not found",
                "full_data": []
            }, status=status.HTTP_404_NOT_FOUND)

    def partial_update(self, request, pk=None):
        try:
            item = self.get_queryset().get(pk=pk)
            serializer = self.get_serializer(item, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response({
                    "status": "success",
                    "message": "Item partially updated successfully",
                    "full_data": [serializer.data]
                }, status=status.HTTP_200_OK)
            return Response({
                "status": "failed",
                "message": "Partial update failed",
                "full_data": serializer.errors
            }, status=status.HTTP_400_BAD_REQUEST)
        except Item.DoesNotExist:
            return Response({
                "status": "failed",
                "message": "Item not found",
                "full_data": []
            }, status=status.HTTP_404_NOT_FOUND)

    def destroy(self, request, pk=None):
        try:
            item = self.get_queryset().get(pk=pk)
            item.delete()
            return Response({
                "status": "success",
                "message": "Item deleted successfully",
                "full_data": []
            }, status=status.HTTP_200_OK)
        except Item.DoesNotExist:
            return Response({
                "status": "failed",
                "message": "Item not found",
                "full_data": []
            }, status=status.HTTP_404_NOT_FOUND)


# Limited table viewset (read-only)
class LimitedItemViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Item.objects.all()
    serializer_class = LimitedItemSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        difficulty = self.request.query_params.get('difficulty')
        if difficulty:
            if difficulty.isdigit():
                queryset = queryset.filter(difficulty__value=int(difficulty))
            else:
                queryset = queryset.filter(difficulty__name__iexact=difficulty)
        return queryset

    def list(self, request):
        items = self.get_queryset()
        serializer = self.get_serializer(items, many=True)
        return Response({
            "status": "success",
            "message": "Limited items retrieved successfully",
            "limited_data": serializer.data
        }, status=status.HTTP_200_OK)

    def retrieve(self, request, pk=None):
        try:
            item = self.get_queryset().get(pk=pk)
            serializer = self.get_serializer(item)
            return Response({
                "status": "success",
                "message": "Limited item retrieved successfully",
                "limited_data": [serializer.data]
            }, status=status.HTTP_200_OK)
        except Item.DoesNotExist:
            return Response({
                "status": "failed",
                "message": "Item not found",
                "limited_data": []
            }, status=status.HTTP_404_NOT_FOUND)
            
            
            
            
            # Limited table viewset (read-only)
class LevelTableViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = puzzleLevel.objects.all()
    serializer_class = levelTableSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        difficulty = self.request.query_params.get('difficulty')
        if difficulty:
            if difficulty.isdigit():
                queryset = queryset.filter(difficulty__value=int(difficulty))
            else:
                queryset = queryset.filter(difficulty__name__iexact=difficulty)
        return queryset

    def list(self, request):
        items = self.get_queryset()
        serializer = self.get_serializer(items, many=True)
        return Response({
            "status": "success",
            "message": "Limited items retrieved successfully",
            "limited_data": serializer.data
        }, status=status.HTTP_200_OK)

    def retrieve(self, request, pk=None):
        try:
            item = self.get_queryset().get(pk=pk)
            serializer = self.get_serializer(item)
            return Response({
                "status": "success",
                "message": "Limited item retrieved successfully",
                "limited_data": [serializer.data]
            }, status=status.HTTP_200_OK)
        except puzzleLevel.DoesNotExist:
            return Response({
                "status": "failed",
                "message": "Item not found",
                "limited_data": []
            }, status=status.HTTP_404_NOT_FOUND)