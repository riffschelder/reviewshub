from django import template
from reviewInfo.models import ReviewInfo
from summarize import SimpleSummarizer
register = template.Library()



@register.filter
def sum_long (long_input):
    Simple = SimpleSummarizer()
    return Simple.summarize(long_input, 2)

