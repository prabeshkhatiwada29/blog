from django.contrib import admin
from .models import Post

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')
    search_fields = ('title',)
    readonly_fields = ('created_at',)
    
admin.site.register(Post, PostAdmin)
