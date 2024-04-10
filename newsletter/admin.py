from django.contrib import admin
from .models import Subscriber


class SubscriberAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'email', 'subscribed_at',)

admin.site.register(Subscriber, SubscriberAdmin)