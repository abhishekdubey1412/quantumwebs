from django.contrib import admin
from .models import Category, Tag, Post, Comment

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    search_fields = ('name',)
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    search_fields = ('name',)
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'created_at', 'updated_at', 'is_published', 'views_count', 'comment_count')
    search_fields = ('title', 'content', 'category__name')
    list_filter = ('created_at', 'updated_at', 'is_published', 'category')
    prepopulated_fields = {'slug': ('title',)}
    autocomplete_fields = ('category', 'tags')
    readonly_fields = ('views_count', 'comment_count')
    fieldsets = (
        (None, {
            'fields': ('title', 'slug', 'content', 'excerpt', 'category', 'tags', 'is_published')
        }),
        ('Media', {
            'fields': ('featured_image', 'featured_title', 'featured_alt_text')
        }),
        ('Metadata', {
            'fields': ('meta_title', 'meta_description', 'meta_keywords')
        }),
        ('Statistics', {
            'fields': ('views_count', 'comment_count')
        }),
    )

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'post', 'created_at', 'approved')
    search_fields = ('name', 'email', 'content', 'post__title')
    list_filter = ('created_at', 'approved', 'post')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(approved=True)
    approve_comments.short_description = "Approve selected comments"
