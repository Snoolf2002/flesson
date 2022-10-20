from django.db import models

# Create your models here.
class Todo(models.Model):
    image = models.ImageField(upload_to='images/')
    title = models.CharField(max_length=255, null=False, blank=False)
    description = models.TextField(null=False, blank=False)
    status = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

