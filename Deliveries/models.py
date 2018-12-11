from django.db import models

class Delivery(models.Model):
    user = models.CharField(max_length=30)
    from_address = models.TextField()
    to_address = models.TextField()
    organization = models.CharField(max_length=50)
    other_info = models.TextField()