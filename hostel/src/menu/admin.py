from django.contrib import admin

# Register your models here.
from .models import Item, Timing
class AdminItem(admin.ModelAdmin):
	list_display = ['day', 'breakfast', 'lunch', 'evening', 'dinner']

admin.site.register(Item,AdminItem)
admin.site.register(Timing)
