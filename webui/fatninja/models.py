from django.db import models

# Create your models here.
#Tweet table : Holds the tweet text and meta data information.

class Tweet(models.Model):
      tweet_text  = models.charField(max_length=140)
      tweet_stamp = models.DateTimeField('Tweet Stamp')

class MetaData(models.Model):
      search_key   = models.Charfield(max_length = 30)
      search_stamp = models.DateTimeField('Query Stamp') 