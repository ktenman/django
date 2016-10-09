from django.db import models

# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=200, help_text="Maximum 200 letters")
    author = models.CharField(max_length=100, help_text="Maximum 100 letters")
    comment = models.TextField(blank=True, null=True)
    date_commented = models.DateField(blank=True, null=True)
    is_bookmarked = models.BooleanField(default=False, verbose_name="Is favourite?")

    def __str__(self): # adding toString() method to represent objects
        return ("{title = '%s', author = '%s'}"% (self.title, self.author))

