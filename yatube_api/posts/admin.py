from django.contrib import admin
from django.contrib.auth import get_user_model

from .models import Comment, Follow, Group, Post

User = get_user_model()


class PostsInstanceInline(admin.TabularInline):
    model = Post


class CommentsInstanceInline(admin.TabularInline):
    model = Comment


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'text', 'pub_date', 'author', 'group')
    search_fields = ('text', 'author__username', 'group__title')
    list_filter = ('pub_date', 'author', 'group')
    inlines = (CommentsInstanceInline,)
    empty_value_display = '-пусто-'


@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'slug', 'description')
    search_fields = ('title', 'description', 'slug')
    inlines = (PostsInstanceInline,)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'text', 'created', 'author', 'post')
    search_fields = ('text', 'author__username')
    list_filter = ('created', 'author')


@admin.register(Follow)
class FollowAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'following')
    search_fields = ('user__username', 'following__username')
    list_filter = ('user', 'following')
