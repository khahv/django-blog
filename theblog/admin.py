from django.contrib import admin
from .models import Post, Category, MachineTemplate
# Register your models here.

# admin.site.register(Post)
# admin.site.register(Category)
admin.site.register(Category)


@admin.register(MachineTemplate)
class MachineTemplateAdmin(admin.ModelAdmin):
    search_fields = ['name']

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ('title',)
    filter_horizontal = ('machines',) 