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
    
class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    company = models.CharField(max_length=65)
    message = models.TextField()

    def __str__(self):
        return self.name

class JobListing(models.Model):
    department = models.CharField(max_length=100)
    industry = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    job_type = models.CharField(max_length=50)
    salary = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    skills = models.TextField(null=True)
    responsibilities = models.TextField()
    experience = models.CharField(max_length=100)
    educational_requirements = models.CharField(max_length=200)
    description = models.TextField()
    
    def __str__(self):
        return self.title

class JobApplication(models.Model):
    applicant_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    job_profile = models.CharField(max_length=100)
    message = models.TextField()

    def __str__(self):
        return f'{self.applicant_name} - {self.job_profile.title}'