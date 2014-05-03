from django.db import models

# Create your models here.
class ReviewInfo(models.Model):
    sku = models.IntegerField()
    rating = models.FloatField()
    title = models.CharField(max_length = 200)
    comment = models.TextField()
    submissionTime = models.DateTimeField()
    reviewer = models.CharField(max_length = 200)
