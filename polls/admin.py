from django.contrib import admin
from .models import *

# Register your models here.
# class ChoiceInline(admin.TabularInline):
# 	model = Choice
# 	extra = 3

# class PollAdmin(admin.ModelAdmin):
# 	fieldsets= [(None, {'fields': ['text']}),
# 	('Date Information', {'fields': [], 'classes': ['collapse']}),]
# 	inlines = [ChoiceInline]

# admin.site.register(Poll, PollAdmin)

admin.site.register(Poll)
admin.site.register(Choice)
admin.site.register(Vote)