from django.db import models
from jsonfield import JSONField

# Create your models here.


class Test(models.Model):
    frontal = models.ImageField(blank=True, upload_to='tests')
    lateral = models.ImageField(blank=True, upload_to='tests')
    prediction = JSONField(null=True, blank=True)
    explanations = JSONField(null=True, blank=True)