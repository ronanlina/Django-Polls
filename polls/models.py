from django.db import models

# Create your models here.
# This is where we create database models (ORM)
# Take notes later about migrating models.
# Migrations are how Django stores changes to your models (and thus your database schema) - they’re just files on disk.
# python manage.py migrate. migrates database models to sql databases.

class Question(models.Model):
    #table column           datatype    length/format/etc.
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0) 
