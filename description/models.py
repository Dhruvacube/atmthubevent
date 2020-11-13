from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.
class Description(models.Model):
    website = models.URLField(_("The original ATMT website url"))
    facebook = models.URLField(_("The ATMT Facebook Page url"))
    twitter = models.URLField(_("The ATMT Twitter handle url"))
    instagram = models.URLField(_("The ATMT Instgram Account url"))

    facebook_check = models.BooleanField(_('Facebook'),default=True)
    twitter_check = models.BooleanField(_('Twitter'),default=True)
    instagram_check = models.BooleanField(_('Instagram'),default=True)
    
    address = models.TextField(_("The Address of ATMT office"))
    
    aboutfooter = models.CharField(_('About the ATMT for the footer'),help_text=_('This should not exceed more than 150 characters'),max_length=150)
    aboutright = models.TextField(_('About ATMT in the right side of about us section'))
    aboutleft = models.TextField(_('About ATMT in the left side of about us section'))

    def __str__(self):
        return 'About Us (Description)'

    class Meta:
        verbose_name_plural = 'About Us'
