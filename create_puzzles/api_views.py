from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import Item
from rest_framework.serializers import ModelSerializer

# Serializer returning only required fields
class ItemSerializer(ModelSerializer):
    class Meta:
        model = Item
        fields = ['id', 'title', 'difficulty']  # Only the required fields

# ViewSet with standardized responses
class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

    def list(self, request):
        items = self.get_queryset()
        serializer = self.get_serializer(items, many=True)
        return Response({
            "status": "success",
            "message": "Items retrieved successfully",
            "data": serializer.data
        }, status=status.HTTP_200_OK)

    def retrieve(self, request, pk=None):
        # Filter by ID
        if pk.isdigit():
            try:
                item = self.get_queryset().get(pk=pk)
                serializer = self.get_serializer(item)
                return Response({
                    "status": "success",
                    "message": "Item retrieved successfully",
                    "data": [serializer.data]
                }, status=status.HTTP_200_OK)
            except Item.DoesNotExist:
                return Response({
                    "status": "failed",
                    "message": "Item not found",
                    "data": []
                }, status=status.HTTP_404_NOT_FOUND)

        # Filter by difficulty
        elif pk.lower() in ["easy", "medium", "hard"]:
            items = self.get_queryset().filter(difficulty__iexact=pk)
            serializer = self.get_serializer(items, many=True)
            return Response({
                "status": "success",
                "message": f"{pk.capitalize()} items retrieved successfully",
                "data": serializer.data
            }, status=status.HTTP_200_OK)

        else:
            return Response({
                "status": "failed",
                "message": "Invalid parameter",
                "data": []
            }, status=status.HTTP_400_BAD_REQUEST)

    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                "status": "success",
                "message": "Item created successfully",
                "data": [serializer.data]
            }, status=status.HTTP_201_CREATED)
        return Response({
            "status": "failed",
            "message": "Item creation failed",
            "data": serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        try:
            item = self.get_queryset().get(pk=pk)
            serializer = self.get_serializer(item, data=request.data, partial=False)
            if serializer.is_valid():
                serializer.save()
                return Response({
                    "status": "success",
                    "message": "Item updated successfully",
                    "data": [serializer.data]
                }, status=status.HTTP_200_OK)
            else:
                return Response({
                    "status": "failed",
                    "message": "Item update failed",
                    "data": serializer.errors
                }, status=status.HTTP_400_BAD_REQUEST)
        except Item.DoesNotExist:
            return Response({
                "status": "failed",
                "message": "Item not found",
                "data": []
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
                    "data": [serializer.data]
                }, status=status.HTTP_200_OK)
            else:
                return Response({
                    "status": "failed",
                    "message": "Partial update failed",
                    "data": serializer.errors
                }, status=status.HTTP_400_BAD_REQUEST)
        except Item.DoesNotExist:
            return Response({
                "status": "failed",
                "message": "Item not found",
                "data": []
            }, status=status.HTTP_404_NOT_FOUND)

    def destroy(self, request, pk=None):
        try:
            item = self.get_queryset().get(pk=pk)
            item.delete()
            return Response({
                "status": "success",
                "message": "Item deleted successfully",
                "data": []
            }, status=status.HTTP_200_OK)
        except Item.DoesNotExist:
            return Response({
                "status": "failed",
                "message": "Item not found",
                "data": []
            }, status=status.HTTP_404_NOT_FOUND) 
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import Item
from rest_framework.serializers import ModelSerializer

# Serializer returning only required fields
class ItemSerializer(ModelSerializer):
    class Meta:
        model = Item
        fields = ['id', 'title', 'difficulty']  # Only the required fields

# ViewSet with standardized responses
class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

    def list(self, request):
        items = self.get_queryset()
        serializer = self.get_serializer(items, many=True)
        return Response({
            "status": "success",
            "message": "Items retrieved successfully",
            "data": serializer.data
        }, status=status.HTTP_200_OK)

    def retrieve(self, request, pk=None):
        # Filter by ID
        if pk.isdigit():
            try:
                item = self.get_queryset().get(pk=pk)
                serializer = self.get_serializer(item)
                return Response({
                    "status": "success",
                    "message": "Item retrieved successfully",
                    "data": [serializer.data]
                }, status=status.HTTP_200_OK)
            except Item.DoesNotExist:
                return Response({
                    "status": "failed",
                    "message": "Item not found",
                    "data": []
                }, status=status.HTTP_404_NOT_FOUND)

        # Filter by difficulty
        elif pk.lower() in ["easy", "medium", "hard"]:
            items = self.get_queryset().filter(difficulty__iexact=pk)
            serializer = self.get_serializer(items, many=True)
            return Response({
                "status": "success",
                "message": f"{pk.capitalize()} items retrieved successfully",
                "data": serializer.data
            }, status=status.HTTP_200_OK)

        else:
            return Response({
                "status": "failed",
                "message": "Invalid parameter",
                "data": []
            }, status=status.HTTP_400_BAD_REQUEST)

    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                "status": "success",
                "message": "Item created successfully",
                "data": [serializer.data]
            }, status=status.HTTP_201_CREATED)
        return Response({
            "status": "failed",
            "message": "Item creation failed",
            "data": serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        try:
            item = self.get_queryset().get(pk=pk)
            serializer = self.get_serializer(item, data=request.data, partial=False)
            if serializer.is_valid():
                serializer.save()
                return Response({
                    "status": "success",
                    "message": "Item updated successfully",
                    "data": [serializer.data]
                }, status=status.HTTP_200_OK)
            else:
                return Response({
                    "status": "failed",
                    "message": "Item update failed",
                    "data": serializer.errors
                }, status=status.HTTP_400_BAD_REQUEST)
        except Item.DoesNotExist:
            return Response({
                "status": "failed",
                "message": "Item not found",
                "data": []
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
                    "data": [serializer.data]
                }, status=status.HTTP_200_OK)
            else:
                return Response({
                    "status": "failed",
                    "message": "Partial update failed",
                    "data": serializer.errors
                }, status=status.HTTP_400_BAD_REQUEST)
        except Item.DoesNotExist:
            return Response({
                "status": "failed",
                "message": "Item not found",
                "data": []
            }, status=status.HTTP_404_NOT_FOUND)

    def destroy(self, request, pk=None):
        try:
            item = self.get_queryset().get(pk=pk)
            item.delete()
            return Response({
                "status": "success",
                "message": "Item deleted successfully",
                "data": []
            }, status=status.HTTP_200_OK)
        except Item.DoesNotExist:
            return Response({
                "status": "failed",
                "message": "Item not found",
                "data": []
            }, status=status.HTTP_404_NOT_FOUND)