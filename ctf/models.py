from django.db import models
from django.forms import ModelForm
import datetime

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
    information = models.TextField()
    #tags = TaggableManager()
    added = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    def __unicode__(self):
        return self.name
    
class Clue(models.Model):
    text = models.TextField()
    sticker = models.ForeignKey(Sticker)
    #tags = TaggableManager()
    added = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
 
class Game(models.Model):
    name = models.CharField(max_length=30)
    isActive = models.BooleanField()
    #tags = TaggableManager()
    added = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    def __unicode__(self):
        return self.name
            
class GameNode(models.Model):
    game = models.ForeignKey(Game)
    sticker = models.ForeignKey(Sticker)
    nodeNumber = models.IntegerField()
    isFlag = models.BooleanField()
    
    def __unicode__(self):
        return (self.game.name + " node " + str(self.nodeNumber))

class Collection(models.Model):
    player = models.ForeignKey(Player)
    gameNode = models.ForeignKey(GameNode)
    #tags = TaggableManager()
    added = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    def __unicode__(self):
        return (self.player.email + " collected " + self.sticker.name + " @ " + str(self.added))
 
