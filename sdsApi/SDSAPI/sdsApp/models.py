from django.db import models

# Create your models here.

class SDS(models.Model):
    document = models.FileField(blank=True, null=True,  upload_to="documents")
    folder = models.CharField(max_length=100)
    topic = models.CharField(max_length=100)



