from django.db import models

# Create your models here.

class addevent(models.Model):
    eventname = models.CharField(max_length=500)
    description = models.CharField(max_length=500)
    time = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    image = models.CharField(max_length=500)
    islike = models.IntegerField(blank=False, null=False, default=0)



    class Meta:
        db_table = 'addevent'

