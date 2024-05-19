from django.contrib import admin
from .models import Subscribe, Reviews, Faqs

@admin.register(Subscribe)
class SubscribeAdmin(admin.ModelAdmin):
    list_display = ('email', 'subscribed_at', 'unsubscribed')
    search_fields = ('email',)
    list_filter = ('subscribed_at', 'unsubscribed')

@admin.register(Reviews)
class ReviewsAdmin(admin.ModelAdmin):
    list_display = ('name', 'content', 'rating', 'created_at')
    search_fields = ('name', 'content')
    list_filter = ('rating', 'created_at')

@admin.register(Faqs)
class FaqsAdmin(admin.ModelAdmin):
    list_display = ('question', 'answer', 'created_at', 'updated_at')
    search_fields = ('question', 'answer')
    list_filter = ('created_at', 'updated_at')