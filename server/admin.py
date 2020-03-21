from django.contrib import admin
from .models import Test
from django.db import models

class TestAdmin(admin.ModelAdmin):
    list_display = ('id', )
    list_filter = ['id']
    search_fields = ['id']

admin.site.register(Test, TestAdmin)