from django.db import models

class Birthday(models.Model):
    bday_name = models.CharField(max_length=300)
    bday_date = models.CharField(max_length=6)

    class Meta:
        ordering = ['bday_name']

    def __str__(self):
        return self.bday_name + ' :: ' + self.bday_date