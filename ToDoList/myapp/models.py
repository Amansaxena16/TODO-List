from django.db import models

class Task(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(blank=True, null=True, max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title
