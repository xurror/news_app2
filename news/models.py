from django.db import models
from datetime import datetime
from publishers.models import Publisher

# Create your models here.
class NewsDetail(models.Model):
    title           = models.CharField(max_length=200)
    publisher       = models.ForeignKey(Publisher, on_delete=models.DO_NOTHING)
    description     = models.TextField()
    file_1          = models.FileField(upload_to='files/%Y/%m/%d', blank=True)
    file_2          = models.FileField(upload_to='files/%Y/%m/%d', blank=True)
    photo_main      = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)
    photo_secondary = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)
    published_date  = models.DateTimeField(default=datetime.now, blank=True)
    is_published    = models.BooleanField(default=True)

    def __str__(self):
        return self.title
