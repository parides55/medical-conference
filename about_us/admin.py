from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import PresidentMessage

# Register your models here.
@admin.register(PresidentMessage)
class PresidentMessageAdmin(SummernoteModelAdmin):

    list_display = ('title')
    summernote_fields = ('message',)