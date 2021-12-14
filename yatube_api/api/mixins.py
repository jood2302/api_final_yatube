from rest_framework import mixins
from rest_framework import viewsets
from rest_framework.exceptions import PermissionDenied

API_RAISE_403 = PermissionDenied('Изменение чужого контента запрещено!')


class CreateRetrieveViewSet(mixins.CreateModelMixin,
                            mixins.ListModelMixin,
                            mixins.UpdateModelMixin,
                            mixins.RetrieveModelMixin,
                            mixins.DestroyModelMixin,
                            viewsets.GenericViewSet):

    def perform_update(self, serializer):
        if serializer.instance.author != self.request.user:
            raise API_RAISE_403
        super().perform_update(serializer)

    def perform_destroy(self, instance):
        if instance.author != self.request.user:
            raise API_RAISE_403
        instance.delete()
