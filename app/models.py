from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    def __str__(self):
        return self.title

class Chapter(models.Model):
    title = models.CharField(max_length=50)
    book = models.ForeignKey(Book)
    def __str__(self):
        return self.title

class Character(models.Model):
    name = models.CharField(max_length=50)
    appears = models.ForeignKey(Chapter)
    def __str__(self):
        return self.name

class Sidekick(models.Model):
    name = models.CharField(max_length=50)
    helps = models.ForeignKey(Character)
    def __str__(self):
        return self.name

class Item(models.Model):
    The_One_Ring = models.ManyToManyField(Character)
    Gandalf = models.ManyToManyField(Book)
