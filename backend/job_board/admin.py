from django.contrib import admin

from .models import Job

class JobAdmin(admin.ModelAdmin):
  list_display = ("title", "company", "link", "job_id")

admin.site.register(Job, JobAdmin)
