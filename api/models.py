from django.db import models

# Create your models here.
class Languagem(models.Model):
    name = models.CharField(max_length=50, null=False)
    paradigm = models.CharField(max_length=50, null=False)

    def __str__(self):
        return self.name