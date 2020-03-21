from django.db import models
from jsonfield import JSONField
from datetime import datetime

# Create your models here.

def test_path(instance, filename):
    # file will be uploaded to tests/test_<id>/<filename>
    return 'tests/test_{0}/{1}'.format(datetime.now().strftime("%d_%m_%Y_%H_%M_%S"), filename)


class Test(models.Model):
    frontal = models.ImageField(blank=True, upload_to=test_path)
    lateral = models.ImageField(blank=True, upload_to=test_path)
    prediction = JSONField(null=True, blank=True)
    explanations = JSONField(null=True, blank=True)