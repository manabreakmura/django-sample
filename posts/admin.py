from django.contrib import admin

from posts.models import Post


class PostAdmin(admin.ModelAdmin):
    readonly_fields = (
        "created_at",
        "updated_at",
    )


admin.site.register(Post, PostAdmin)
