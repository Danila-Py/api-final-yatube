from django.contrib import admin

from .models import Comment, Follow, Group, Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = (
        "text",
        "pub_date",
        "author",
        "group",
    )
    search_fields = ("text", "group__title")
    list_filter = ("pub_date", "group", "author")
    empty_value_display = "-пусто-"


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = (
        "text",
        "author",
        "post",
    )
    search_fields = ("text",)
    list_filter = ("post",)
    empty_value_display = "-пусто-"


@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = ("title", "slug")
    search_fields = ("title",)
    list_filter = ("title",)
    empty_value_display = "-пусто-"


@admin.register(Follow)
class FollowAdmin(admin.ModelAdmin):
    list_display = (
        "user",
        "following",
    )
    search_fields = ("user__username", "following__username")
    list_filter = ("user", "following")
    empty_value_display = "-пусто-"
