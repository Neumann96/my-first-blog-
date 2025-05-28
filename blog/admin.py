from django.contrib import admin
from .models import Post, kkexam

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'publish']
    # ist_filter = ['status', 'created', 'publish', 'author']
    # search_fields = ['title', 'body']
    # prepopulated_fields = {'slug': ('title',)}
    # raw_id_fields = ['author']
    # date_hierarchy = 'publish'
    # ordering = ['status', 'publish']


@admin.register(kkexam)
class KKExamAdmin(admin.ModelAdmin):
    list_display = ['name', 'exam_date', 'is_public', 'created_at']
    list_filter = ['is_public', 'created_at']
    search_fields = ['name', 'users__email']
    date_hierarchy = 'exam_date'
    filter_horizontal = ['users']