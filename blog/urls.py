from django.urls import path
from . import views
urlpatterns = [
    path('blog/', views.blog, name="blog"),
    path('blog-single/', views.blog_single, name="blog-single"),
]