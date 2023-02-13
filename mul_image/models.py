from django.db import models
from django.utils.safestring import mark_safe

class MultipleImage(models.Model):
    # title=models.CharField(max_length=100)
    images = models.FileField()
    def image_tag(self): # new
        return mark_safe('<img src="/../../media/%s" width="150" height="150" />' % (self.images))