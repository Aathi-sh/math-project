from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import crossMath, Difficulty,puzzleLevel
from .serializers import puzzleSerializer, puzzleLevelSerializer,levelTableSerializer

# Full table viewset
class puzzleViewSet(viewsets.ModelViewSet):
    queryset = crossMath.objects.all()
    serializer_class = puzzleSerializer

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
        except crossMath.DoesNotExist:
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
        except crossMath.DoesNotExist:
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
        except crossMath.DoesNotExist:
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
        except crossMath.DoesNotExist:
            return Response({
                "status": "failed",
                "message": "Item not found",
                "full_data": []
            }, status=status.HTTP_404_NOT_FOUND)


class puzzleLevelViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = crossMath.objects.all()
    serializer_class = puzzleLevelSerializer

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
        difficulty_order = ["Easy", "Medium", "Hard", "Expert"]

        ordered_data = []
        auto_id = 1

        # For each difficulty, pick the first matching item (if any)
        for level in difficulty_order:
            obj = items.filter(difficulty__name__iexact=level).first()
            if obj:
                serialized = self.get_serializer(obj).data
                ordered_data.append({
                    "id": auto_id,
                    "difficulty": serialized.get("difficulty"),
                    "created_by": serialized.get("created_by"),
                    "updated_by": serialized.get("updated_by"),
                    "active": serialized.get("active")
                })
                auto_id += 1

        return Response({
            "status": "success",
            "message": "Limited items retrieved successfully",
            "limited_data": ordered_data
        }, status=status.HTTP_200_OK)

# # Limited table viewset (read-only)
# class LimitedItemViewSet(viewsets.ReadOnlyModelViewSet):
#     queryset = Item.objects.all()
#     serializer_class = LimitedItemSerializer

#     def get_queryset(self):
#         queryset = super().get_queryset()
#         difficulty = self.request.query_params.get('difficulty')
#         if difficulty:
#             if difficulty.isdigit():
#                 queryset = queryset.filter(difficulty__value=int(difficulty))
#             else:
#                 queryset = queryset.filter(difficulty__name__iexact=difficulty)
#         return queryset

#     def list(self, request):
#         items = self.get_queryset()
#         serializer = self.get_serializer(items, many=True)
#         return Response({
#             "status": "success",
#             "message": "Limited items retrieved successfully",
#             "limited_data": serializer.data
#         }, status=status.HTTP_200_OK)

#     def retrieve(self, request, pk=None):
#         try:
#             item = self.get_queryset().get(pk=pk)
#             serializer = self.get_serializer(item)
#             return Response({
#                 "status": "success",
#                 "message": "Limited item retrieved successfully",
#                 "limited_data": [serializer.data]
#             }, status=status.HTTP_200_OK)
#         except Item.DoesNotExist:
#             return Response({
#                 "status": "failed",
#                 "message": "Item not found",
#                 "limited_data": []
#             }, status=status.HTTP_404_NOT_FOUND)


class LevelTableViewSet(viewsets.ModelViewSet):
    queryset = puzzleLevel.objects.all()
    serializer_class = puzzleSerializer

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
        except puzzleLevel.DoesNotExist:
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
        except puzzleLevel.DoesNotExist:
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
        except puzzleLevel.DoesNotExist:
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
        except puzzleLevel.DoesNotExist:
            return Response({
                "status": "failed",
                "message": "Item not found",
                "full_data": []
            }, status=status.HTTP_404_NOT_FOUND)
