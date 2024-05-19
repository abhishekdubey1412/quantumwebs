from django.db import models

# Create your models here.
# class Category(models.Model):
#     name = models.CharField(max_length=100)
#     slug = models.SlugField(unique=True)  # Slug for SEO-friendly URLs
    
#     def __str__(self):
#         return self.name

# class Tag(models.Model):
#     name = models.CharField(max_length=100)
#     slug = models.SlugField(unique=True)
    
#     def __str__(self):
#         return self.name
    
# class Post(models.Model):
#     title = models.CharField(max_length=200)
#     slug = models.SlugField(unique=True)
#     content = models.TextField()
#     excerpt = models.TextField(blank=True)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
#     category = models.ForeignKey(Category, on_delete=models.CASCADE)
#     tags = models.ManyToManyField(Tag)
#     featured_image = models.ImageField(upload_to='post_images/')
#     featured_title = models.CharField(max_length=50)
#     featured_alt_text = models.CharField(max_length=50)
#     views_count = models.PositiveIntegerField(default=0)
#     comment_count = models.PositiveIntegerField(default=0)
#     is_published = models.BooleanField(default=False)
#     meta_title = models.CharField(max_length=200, blank=True)
#     meta_description = models.TextField(blank=True)
#     meta_keywords = models.CharField(max_length=200, blank=True)

# class Comment(models.Model):
#     post = models.ForeignKey(Post, on_delete=models.CASCADE)
#     name = models.CharField(max_length=100)
#     email = models.EmailField()
#     content = models.TextField()
#     created_at = models.DateTimeField(auto_now_add=True)
#     approved = models.BooleanField(default=False)
    
#     def __str__(self):
#         return f'Comment by {self.name} on {self.post.title}'