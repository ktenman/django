from django.db import models

# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    comment = models.TextField(blank=True, null=True)
    date_commented = models.DateField(blank=True, null=True)
    is_bookmarked = models.BooleanField(default=False)

    def __str__(self): # adding toString() method to represent objects
        return ("{title = '%s', author = '%s'}"% (self.title, self.author))