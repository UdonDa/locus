from django.contrib import admin
from django.utils.html import format_html
# Register your models here.
from .models import Document

class ImageAdmin(admin.ModelAdmin):
    # list_display = ('thumbnail', 'document', 'description', 'uploaded_at')
    list_display = ('pk', 'thumbnail', 'document', 'uploaded_at')


admin.site.register(Document, ImageAdmin)
