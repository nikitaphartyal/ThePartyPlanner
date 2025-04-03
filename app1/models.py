from django.db import models

class PartyDetails(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    party_date = models.DateField()
    suppliers_date = models.DateField()
    guest_count = models.IntegerField()
    party_type = models.CharField(max_length=100)
    budget = models.IntegerField()
    theme = models.CharField(max_length=100)
    additional_info = models.TextField()
class Query(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
class Feedback(models.Model):
    message = models.TextField()
    def __str__(self):
        return f"Feedback: {self.message}"
    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Photo(models.Model):
    image = models.ImageField(upload_to='photos/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        app_label = 'app1'  # Replace 'plannerapp' with your actual app name

class Document(models.Model):
    title = models.CharField(max_length=255)
    file = models.ImageField(upload_to='documents/')
    upload_date = models.DateTimeField(auto_now_add=True)

    # def __str__(self):
    #     return self.title

