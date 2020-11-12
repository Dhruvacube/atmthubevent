from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.
class LiveVideos(models.Model):
    date = models.DateTimeField(_('The Date and Time when the event will go live'))
    streamingvideoheader = models.CharField(_('Live Streaming Video Header'),max_length=600)

    streamingvideolink = models.URLField(_('Live Video Link'), null=True, blank=True)
    videoid = models.CharField(_('Facebook/YouTube Video ID'),max_length=500, null=True, blank=True)
    usernamefb = models.CharField(_('Facebook User ID'),max_length=500, null=True, blank=True)
    embeedlink = models.URLField(_('Embeed Link of Posts or Video'),null=True, blank=True)
    streamingvideodescription = models.TextField(_('Streaming Video Short Description'), help_text='This is optional', null=True,blank=True)

    def __str__(self):
        return self.streamingvideoheader
    
    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        #Setting this field as the live field and setting all other false
        if self.live:
            LiveVideos.objects.update(live=False)
            self.live = self.live

        return super().save(force_insert=force_insert, force_update=force_update, using=using, update_fields=update_field)
    
    class Meta:
        verbose_name_plural = "Live Videos"