from django.db import models
from django.utils.html import mark_safe
from django.utils.timezone import now
from django.utils.translation import gettext_lazy as _


# Create your models here.
class LiveVideos(models.Model):
    date = models.DateTimeField(_('The Date and Time when the event will go live'),default=now)
    streamingvideoheader = models.CharField(_('Live Streaming Video Header'),max_length=600)

    live = models.BooleanField(_('Live Video'), help_text=_('Check this only if the video is live'), default=True)

    streamingvideolink = models.URLField(_('Live Video Link'), null=True, blank=True)
    videoid = models.CharField(_('Facebook/YouTube Video ID'),max_length=500, null=True, blank=True)
    usernamefb = models.CharField(_('Facebook User ID'),max_length=500, null=True, blank=True)
    embeedlink = models.URLField(_('Embeed Link of Posts or Video'),null=True, blank=True)
    streamingvideodescription_left = models.TextField(_('Streaming Video Short Description Left'))
    streamingvideodescription_right = models.TextField(_('Streaming Video Short Description Right'))

    def __str__(self):
        return self.streamingvideoheader
    
    def facebook_posts(self):
        '''This is method to generate the facebook video in an iframe'''
        url = f'https://www.facebook.com/plugins/video.php?href=https%3A%2F%2Fwww.facebook.com%2F{self.usernamefb}%2Fvideos%2F{self.videoid}%2F&show_text=false&width=734&height=504&appId'
        return mark_safe(f'<iframe src="{url}" width="734" height="504" style="border:none;overflow:hidden" scrolling="no" frameborder="0" allowTransparency="true" allow="encrypted-media" allowFullScreen="true"></iframe>')
    
    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        #Setting this field as the live field and setting all other false
        if self.live:
            LiveVideos.objects.update(live=False)
            self.live = self.live

        #setting up the link embedder
        if self.streamingvideolink[-1] != '/':
            self.streamingvideolink = self.streamingvideolink + '/'
        a = self.streamingvideolink.lstrip('https://www.facebook.com/')
        lista = a.split('/')
        if len(lista) == 4:
            self.videoid = lista[-2]  
        elif len(lista) == 3:
            self.videoid = lista[-1]
        self.usernamefb = lista[0]
        self.embeedlink = f'https://www.facebook.com/plugins/video.php?href=https%3A%2F%2Fwww.facebook.com%2F{self.usernamefb}%2Fvideos%2F{self.videoid}%2F&show_text=false&width=380&height=476&appId'

        return super().save(force_insert=force_insert, force_update=force_update, using=using, update_fields=update_fields)
    
    class Meta:
        verbose_name_plural = "Live Videos"
