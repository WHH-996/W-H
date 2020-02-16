from django.db import models


# Create your models here.
class Vote(models.Model):
    title = models.CharField(max_length=20)

    def __str__(self):
        return self.title


class Option(models.Model):
    content = models.CharField(max_length=20, default=0)
    num = models.IntegerField(max_length=5, default=0)
    vote = models.ForeignKey(Vote, on_delete=models.CASCADE)
