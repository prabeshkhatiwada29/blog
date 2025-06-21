from django.contrib import admin
from .models import Post

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'author', 'is_published', 'comments_count', 'likes_count')
    search_fields = ('title',)
    list_filter = ('is_published', 'author')


    
admin.site.register(Post, PostAdmin)
