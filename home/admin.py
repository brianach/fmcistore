from django.contrib import admin
from .models import PartnerImages


# Register your models here.
class PartnerImagesAdmin(admin.ModelAdmin):
    list_display = (
        'p_name',
        'p_link',
    )


admin.site.register(PartnerImages, PartnerImagesAdmin)
