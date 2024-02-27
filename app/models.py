from django.db import models



class BaseTest(models.Model):

    name = models.CharField(max_length=100)