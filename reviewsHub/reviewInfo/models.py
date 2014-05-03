from django.db import models

def product_name(sku):
    if sku == 9008182:
        return 'Xbox One'
    elif sku == 6238297:
        return 'Macbook Air'
    elif sku == 5717547:
        return 'Galaxy S III'
    else:
        return '???'

class ReviewInfo(models.Model):
    sku = models.IntegerField()
    rating = models.FloatField()
    title = models.CharField(max_length = 200)
    comment = models.TextField()
    submissionTime = models.DateTimeField()
    reviewer = models.CharField(max_length = 200)

    def __unicode__(self):
        return product_name(self.sku) + ": " + self.title
