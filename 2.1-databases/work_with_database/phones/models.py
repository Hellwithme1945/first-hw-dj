from django.db import models

class Phone(models.Model):
    name = models.CharField(max_length=100)
    image = models.URLField()
    price = models.FloatField()
    release_date = models.DateField()
    lte_exists = models.BooleanField()

    def __str__(self):
        return self.name
