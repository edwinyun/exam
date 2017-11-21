from __future__ import unicode_literals

from django.db import models
from ..login_app.models import User

# Create your models here.


class QuoteManager(models.Manager):
    def validate(self, postData):
        results = {'errors':[]}
        
        if len(postData['quoted_by']) < 4:
            results['errors'].append('Must be atleast 3 characters.')  
        if len(postData['message']) < 11:
            results['errors'].append('Message must be more than 10 characters.')  
        

        return results







class Quote(models.Model):
    quoted_by = models.CharField(max_length = 255)
    message = models.CharField(max_length = 700)

    quotelist = models.ManyToManyField(User, related_name='quotelist')
    created_by = models.ForeignKey(User, related_name = 'quotes_made', null=True)
    objects = QuoteManager()