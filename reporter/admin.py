from django.contrib import admin
from .models import TestCase, TestSuite

# Register your models here.

admin.site.register(TestCase)
admin.site.register(TestSuite)
