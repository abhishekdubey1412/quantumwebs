from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Subscribe(models.Model):
    email = models.EmailField(max_length=254, unique=True)
    subscribed_at = models.DateTimeField(auto_now_add=True)
    unsubscribed = models.BooleanField(default=False)

    def __str__(self):
        return self.email

class Review(models.Model):
    name = models.CharField(max_length=50)
    content = models.CharField(max_length=350)
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Faq(models.Model):
    question = models.CharField(max_length=250)
    answer = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.question
