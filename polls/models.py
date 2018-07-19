import datetime

from django.db import models
from django.utils import timezone

# Create your models here.
# This is where we create database models (ORM)
# Take notes later about migrating models.
# Migrations are how Django stores changes to your models (and thus your database schema) - they’re just files on disk.
# python manage.py migrate. migrates database models to sql databases.

class Question(models.Model):
    #table column           datatype    length/format/etc.
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    
    #It’s important to add __str__() methods to your models, 
    # not only for your own convenience when dealing with the interactive prompt,
    # but also because objects’ representations are used throughout Django’s 
    # automatically-generated admin.
    # -djangoproject
    
    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now
    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0) 

    def __str__(self):
        return self.choice_text