from django.contrib import admin
from .models import MultipleImage

# admin.site.register(MultipleImage)

class imageAdmin(admin.ModelAdmin):
    list_display = ["id","image_tag", "images"] # new

admin.site.register(MultipleImage, imageAdmin)