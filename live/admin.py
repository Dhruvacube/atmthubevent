from django.contrib import admin, messages
from django.contrib.auth.admin import Group
from django.utils.translation import gettext_lazy as _
from django.utils.translation import ngettext

from .models import *


# Register your models here.
class LiveVideosAdmin(admin.ModelAdmin):
    list_display = ('streamingvideoheader','date','live')
    list_filter = ('date','live')
    search_fields = list_display + list_filter + ('streamingvideolink',)
    readonly_fields = ('videoid','usernamefb','facebook_posts')
    list_per_page = 100

    fieldsets = (
        (_('Streaming Video Data'),{'fields':('streamingvideoheader','streamingvideodescription_left','streamingvideodescription_right','date')}),
        (_('Streaming Video Links Data'),{'fields':('streamingvideolink','live',)+readonly_fields})
    )

    ## Custom Actions
    #live
    def make_events_live(self, request, queryset):
        if len(queryset) > 1:
            self.message_user(
                request,
                'Please select only one event',
                messages.ERROR
            )
        else:
            updated  = queryset.update(live=True)
            
            self.message_user(
                    request, 
                    ngettext(
                    '%d event was succesfully made live',
                    '%d events were succesfully made live',
                    updated,
                ) % updated, 
                messages.SUCCESS
            )
    make_events_live.short_description = "Make the selected events go live"

    #offline
    def make_events_offline(self, request, queryset):
        updated = queryset.update(live=False)
        self.message_user(request, ngettext(
            '%d event was succesfully made offline',
            '%d events were succesfully made offline',
            updated,
        ) % updated, messages.SUCCESS)
    make_events_offline.short_description = "Make the selected events go offline"

    #Registering the custom actions
    actions = [make_events_live, make_events_offline]

admin.site.unregister(Group)
admin.site.register(LiveVideos, LiveVideosAdmin)

admin.site.site_header = admin.site.site_title = 'Aarush GOC Pvt Ltd (ATMT HUB)'
admin.site.site_title = 'Aarush GOC Pvt Ltd (ATMT HUB)'
admin.site.index_title = 'Welcome to ATMT HUB cPanel'
