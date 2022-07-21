import email
from operator import mod
from django.db import models

# Create your models here.

class Mail(models.Model):
    mail_id = models.AutoField(primary_key=True)
    emailad = models.EmailField(null=False)
    mailsub = models.CharField(max_length=70)
    mailtext = models.CharField(default='' ,max_length=256)
