from django.db import models
from datetime import datetime

# Create your models here.

class Publisher(models.Model):
    name = models.CharField(max_length=200)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)
    description = models.TextField(blank=True)
    phone = models.CharField(max_length=200)
    email = models.EmailField()
    registered_date = models.DateTimeField(default=datetime.now, blank=True)
    is_mvp = models.BooleanField(default=False)

    def __str__(self):
        return self.name
