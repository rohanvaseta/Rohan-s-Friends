from django.contrib import admin

from .models import Friends
from . models import Question, Choice

admin.site.register(Friends)
admin.site.register(Question)
admin.site.register(Choice)
