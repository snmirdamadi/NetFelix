from django.contrib import admin

from .models import VideoAllProxy, VideoPublishedProxy


class VideoAllAdmin(admin.ModelAdmin):
    list_display = ['title', 'id', 'state', 'video_id', 'is_published']
    search_fields = ['title']
    list_filter = ['state', 'active']
    readonly_fields = ['id', 'is_published', 'publish_timestamps']
    class Meta:
        model = VideoAllProxy




admin.site.register(VideoAllProxy, VideoAllAdmin)


class VideoProxyAdmin(admin.ModelAdmin):
    list_display = ['title', 'video_id']
    search_fields = ['title']

    # list_filter = ['video_id']
    class Meta:
        model = VideoPublishedProxy

    def get_queryset(self, request):
        return VideoPublishedProxy.objects.filter(active=True)


admin.site.register(VideoPublishedProxy, VideoProxyAdmin)
