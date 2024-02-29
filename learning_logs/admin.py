from django.contrib.admin import ModelAdmin, register
from .models import Topic,Entry


@register(Topic)
class TopicAdmin(ModelAdmin):
    pass


@register(Entry)
class EntryAdmin(ModelAdmin):
    pass