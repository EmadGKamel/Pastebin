from django.contrib import admin
from app.models import Snippet, CustomUser
admin.site.register(Snippet)
admin.site.register(CustomUser)