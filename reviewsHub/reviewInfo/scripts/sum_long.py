from reviewInfo.models import ReviewInfo
from re import sub
#import re
from summarize import SimpleSummarizer


def get_all_reviews(product_sku):
    all_reviews = ReviewInfo.objects.all().filter(sku=product_sku)
    review_list = [ sub('-', "", ((e.comment.lower()).encode('utf-8'))) for e in all_reviews ]
    return review_list



samsung_reviews = get_all_reviews(5717547)
#print len(samsung_reviews)
for each_review in samsung_reviews:
    #print len(each_review)
    if len(each_review) > 500:
        print "----Original----"
        print each_review
        print "----summarized----"
        Simple = SimpleSummarizer()
        print Simple.summarize(each_review,2)

