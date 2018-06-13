from django.contrib import admin

from .models import (
    Tag,
    Topic,
    Post
)


class TagAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('id', 'name')
    list_per_page = 25


class TopicAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'domain', 'created_by', 'created_on', 'updated_on')
    list_display_links = ('id', 'created_by')
    search_fields = ('id', 'title')
    list_per_page = 25


class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'text', 'author', 'topic', 'created_date', 'published_date')
    list_display_links = ('id', 'author', 'topic')
    search_fields = ('id', 'title')
    list_per_page = 25


admin.site.register(Tag, TagAdmin)
admin.site.register(Topic, TopicAdmin)
admin.site.register(Post, PostAdmin)
