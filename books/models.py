from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


# Create your models here.

class Cage(models.Model):
    number = models.IntegerField(verbose_name='cage number',
                                 validators=[MinValueValidator(1), MaxValueValidator(100)])
    roadway = models.CharField(max_length=250, null=False, blank=False, verbose_name='A title for roadway')

    def __str__(self):
        return f"{self.roadway} : {self.number}"


class Author(models.Model):
    nationality_fields = [('I', 'Internal'), ('E', 'External')]
    first_name = models.CharField(max_length=50, null=False, blank=False)
    last_name = models.CharField(max_length=80, null=False, blank=False)
    nationality = models.CharField(choices=nationality_fields, max_length=1)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Book(models.Model):
    title = models.CharField(max_length=250, null=False, blank=False)
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True)
    year_of_publish = models.DateField(blank=True, help_text='The time of publish book')
    publisher = models.CharField(max_length=250, null=False, blank=True)
    ISBN_code = models.CharField(max_length=250, null=False, blank=False)
    language = models.CharField(max_length=100, blank=False, null=False)
    cage_info = models.ForeignKey(Cage, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"{self.title} wrote by {self.author}"
