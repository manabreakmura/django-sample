from rest_framework.serializers import ModelSerializer

from posts.models import Post


class PostSerializer(ModelSerializer):

    class Meta:
        model = Post
        fields = ("id", "title", "body", "created_at", "updated_at", "user")
        extra_kwargs = {
            "id": {"read_only": True},
            "created_at": {"read_only": True},
            "updated_at": {"read_only": True},
            "user": {"read_only": True},
        }
