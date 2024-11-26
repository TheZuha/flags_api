from django.db import models

# Create your models here.
class Flags(models.Model):
    image = models.ImageField(upload_to='flags_image/')
    country_name = models.TextField()

    def __str__(self):
        return self.country_name