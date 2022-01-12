from __future__ import unicode_literals
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User

# Create your models here.


class Url(models.Model):
    original_url = models.URLField(_("Original Key"),
     help_text= "Add the original URL that you want to shorten.")

    editable_key = models.CharField(max_length=255, blank=True, null=True,
    help_text= "Add any random characters of your choice to shorten it.")

    user = models.ForeignKey('auth.User', on_delete=models.CASCADE, default=1)
    
    

    def __str__(self):
        return self.original_url 

    def __unicode__(self):
        return 

