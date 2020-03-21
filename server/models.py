from django.db import models

# Create your models here.


class Test(models.Model):
    frontal = models.ImageField(blank=True, upload_to='tests')
    lateral = models.ImageField(blank=True, upload_to='tests')