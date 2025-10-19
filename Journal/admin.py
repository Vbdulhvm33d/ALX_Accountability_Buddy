from django.contrib import admin
from .models import Goals, JournalEntries, ProgressTrackers

admin.site.register(Goals)
admin.site.register(JournalEntries)
admin.site.register(ProgressTrackers)


# Register your models here.
