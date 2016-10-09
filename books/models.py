from django.db import models

# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=200, help_text="Maximum 200 letters")
    authors = models.ManyToManyField("Author", related_name="books")
    comment = models.TextField(blank=True, null=True)
    date_commented = models.DateField(blank=True, null=True)
    is_bookmarked = models.BooleanField(default=False, verbose_name="Is favourite?")

    def __str__(self):
        return self.title

class Author(models.Model):
    name = models.CharField(max_length=100, help_text="Maximum 100 letters", unique=True)

    def __str__(self):
        return self.name