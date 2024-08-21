from rest_framework import filters, mixins, viewsets

from users.models import User
from users.permissions import UserPermission
from users.serializers import UserSerializer


class UserViewSet(
    viewsets.GenericViewSet,
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (UserPermission,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ("username",)
