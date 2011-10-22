from django.contrib import admin

from rainbows.models import Rainbow

class RainbowAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'pub_date')
    fields = ['name', 'slug', 'pub_date']
    prepopulated_fields = {"slug": ("name",)}
    save_on_top = True
    search_fields = ['name']

admin.site.register(Rainbow, RainbowAdmin)
