from django.contrib import admin
from .models import Semester, Subject, Assignment

# Register your models here.
admin.site.register(Semester)
admin.site.register(Subject)
admin.site.register(Assignment)