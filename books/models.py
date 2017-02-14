from django.db import models
from django.utils.datetime_safe import datetime


# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=200, help_text="Maximum 200 letters")
    authors = models.ManyToManyField("Author", related_name="books")
    comment = models.TextField(blank=True, null=True)
    date_commented = models.DateTimeField(default=datetime.now, blank=True)
    is_bookmarked = models.BooleanField(verbose_name="Is favourite?", default=False)

    def __str__(self):
        return "%s by %s" % (self.title, self.list_authors())

    def list_authors(self):
        return ", ".join([author.name for author in self.authors.all()])


class Author(models.Model):
    name = models.CharField(max_length=100, help_text="Maximum 100 letters", unique=True)

    def __str__(self):
        return self.name
