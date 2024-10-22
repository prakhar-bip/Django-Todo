from django.contrib import admin

from TODO.models import Task
from . import *
# Register your models here.
admin.site.register(Task)