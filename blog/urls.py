from django.urls import path
from .views import blog, BlogSingle

urlpatterns = [
    path('blog/', blog, name='blog'),
    path('blog/<slug:slug>/', BlogSingle.as_view(), name='blog_single'),
]