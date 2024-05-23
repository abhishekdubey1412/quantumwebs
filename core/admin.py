from django.contrib import admin
from .models import Subscribe, Review, Faq, Contact, JobListing, JobApplication

@admin.register(Subscribe)
class SubscribeAdmin(admin.ModelAdmin):
    list_display = ('email', 'subscribed_at', 'unsubscribed')
    search_fields = ('email',)
    list_filter = ('subscribed_at', 'unsubscribed')

@admin.register(Review)
class ReviewsAdmin(admin.ModelAdmin):
    list_display = ('name', 'content', 'rating', 'created_at')
    search_fields = ('name', 'content')
    list_filter = ('rating', 'created_at')

@admin.register(Faq)
class FaqsAdmin(admin.ModelAdmin):
    list_display = ('question', 'answer', 'created_at', 'updated_at')
    search_fields = ('question', 'answer')
    list_filter = ('created_at', 'updated_at')

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'company')
    search_fields = ('name', 'email', 'company')

@admin.register(JobListing)
class JobListingAdmin(admin.ModelAdmin):
    list_display = ('title', 'department', 'industry', 'location', 'job_type', 'salary')
    list_filter = ('department', 'industry', 'job_type', 'location')
    search_fields = ('title', 'department', 'industry', 'location', 'skills', 'experience', 'educational_requirements')
    ordering = ('title',)

@admin.register(JobApplication)
class JobApplicationAdmin(admin.ModelAdmin):
    list_display = ('applicant_name', 'email', 'phone', 'job_profile')
    search_fields = ('applicant_name', 'email', 'phone', 'job_profile__title')
    list_filter = ('job_profile',)
    ordering = ('applicant_name',)