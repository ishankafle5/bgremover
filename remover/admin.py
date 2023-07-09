from django.contrib import admin

from remover.models import ImageDetails, User

# Register your models here.
admin.site.register(User)
admin.site.register(ImageDetails)
