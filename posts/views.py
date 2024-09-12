from rest_framework import filters, mixins, status, viewsets
from rest_framework.response import Response

from posts.models import Post
from posts.permissions import PostPermission
from posts.serializers import PostSerializer


class PostViewSet(
    viewsets.GenericViewSet,
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (PostPermission,)
    filter_backends = [filters.SearchFilter]
    search_fields = ["title"]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.validated_data["user"] = request.user
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(
            serializer.data, status=status.HTTP_201_CREATED, headers=headers
        )
