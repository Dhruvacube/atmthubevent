from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from django.utils.translation import ngettext

from .models import *

# Register your models here.
class DescriptionAdmin(admin.ModelAdmin):
    fieldsets = (
        (_('Around the web'),{'fields':('website','facebook','twitter','instagram')}),
        (_('Which Social Medis links needs to be displayed?'),{'fields':('facebook_check','twitter_check','instagram_check')}),
        (_('Location'),{'fields':('address',)}),
        (_('About Us Section'),{'fields':('aboutleft','aboutright')}),
        (_('Footer About Us Section'),{'fields':('aboutfooter',)})
    )

    def has_add_permission(self, request):
        num_objects = Description.objects.count()
        if num_objects >= 1:
            return False
        return super(DescriptionAdmin, self).has_add_permission(request)
    
    def has_delete_permission(self, request, obj=None):
        num_objects = Description.objects.count()
        if num_objects >= 1:
            return False
        return super(DescriptionAdmin, self).has_delete_permission(request,  obj=obj)

admin.site.register(Description, DescriptionAdmin)