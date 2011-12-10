from django.db import models
from django.forms import ModelForm
import datetime

# Create your models here.

class Player(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(max_length=75)
    #tags = TaggableManager()
    added = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    def __unicode__(self):
            return self.email
            
class Sticker(models.Model):
    name = models.CharField(max_length=30)
    lat = models.FloatField()
    lon = models.FloatField()
    keyword = models.CharField(max_length=10)
    #tags = TaggableManager()
    added = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
class Clue(models.Model):
    text = models.TextField()
    sticker = models.ForeignKey(Sticker)
    #tags = TaggableManager()
    added = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    
class Collection(models.Model):
    player = models.ForeignKey(Player)
    sticker = models.ForeignKey(Sticker)
    #tags = TaggableManager()
    added = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    def __unicode__(self):
            rtn_str = (self.visitor.email + " collected " + self.sticker.name + " @ " + str(self.added))
            return rtn_str