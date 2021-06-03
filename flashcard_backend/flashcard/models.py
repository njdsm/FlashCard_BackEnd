from django.db import models

# Create your models here.


class Flashcard(models.Model):
    collection = models.ForeignKey(
        'collection.Collection', on_delete=models.CASCADE
    )
    front_text = models.CharField(max_length=250, null=True, blank=True)
    back_text = models.CharField(max_length=250, null=True, blank=True)

