from django.db import models
from django.utils.timezone import now

class Book(models.Model):
    title = models.CharField(max_length=200, help_text="Maximum 200 letters")
    authors = models.ManyToManyField("Author", related_name="books")
    comment = models.TextField(blank=True, null=True)
    date_commented = models.DateTimeField(blank=True, null=True)
    is_bookmarked = models.BooleanField(default=False, verbose_name="Is favourite?")

    def __str__(self):
        return "{} by {}".format(self.title, self.list_authors())

    def list_authors(self):
        return ", ".join([author.name for author in self.authors.all()])

    def save(self, *args, **kwargs):
        if self.comment and self.date_commented is None:
            self.date_commented = now()

        super(Book, self).save(*args, **kwargs) # Extends save() method after our if-logic


class Author(models.Model):
    name = models.CharField(max_length=100, help_text="Maximum 100 letters", unique=True)

    def __str__(self):
        return self.name