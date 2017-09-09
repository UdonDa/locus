from __future__ import unicode_literals

from django.db import models


class Document(models.Model):
    description = models.CharField(max_length=255, blank=True)
    document = models.ImageField(upload_to='documents/', default='')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def thumbnail(self):
        if self.document:
            return '<img src="{}" style="width:100px;height:auto;">'.format(self.document.url)
        else:
            return 'no image'
    thumbnail.allow_tags = True
