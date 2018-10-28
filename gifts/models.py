from django.db import models

# Create your models here.

class Person(models.Model):
    """
A person in the list of giving/receiving
    gift for Christmas
    """
    name = models.CharField(max_length=50)
    active = models.BooleanField(default=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """
        Return a text representation of the model
        :return:
        """
        return self.name

class Exception(models.Model):
    """
    A person can have one or more people to whom
    they cannot be assigned for Christmas gifts
    """
    name = models.CharField(max_length=50)
    exception = models.CharField(max_length=50)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """
        Return a text representation of the model
        :return:
        """
        return '%s: [%s]'%(self.name, self.exception)

class Gift(models.Model):
    """
    Each record contains a single gift assignment for
    a given year
    """
    name_from = models.CharField(max_length=50)
    name_to = models.CharField(max_length=50)
    year = models.IntegerField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """
        Return a text representation of the model
        :return:
        """
        return '%s -- From: %s  To: %s'%(self.year, self.name_from, self.name_to)