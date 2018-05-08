from django.db import models

# Create your models here.
from AXF.models import User


class Cookies(models.Model):
    ticket = models.CharField(max_length=100)
    create_time = models.IntegerField()
    u = models.ForeignKey(User)

    class Meta:
        db_table = 'u_cookies'

