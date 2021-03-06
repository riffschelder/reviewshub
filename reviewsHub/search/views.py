from django.shortcuts import render
from haystack.query import SearchQuerySet

from reviewInfo.models import product_name, sku_number

from haystack.utils import Highlighter
from django.utils.html import strip_tags

class NoCropHighlighter(Highlighter):
    def highlight(self, text_block):
        self.text_block = strip_tags(text_block)
        highlight_locations = self.find_highlightable_words()
        # start_offset, end_offset = self.find_window(highlight_locations)
        start_offset = 0
        end_offset = len(self.text_block)
        return self.render_html(highlight_locations, start_offset, end_offset)

def search(request):
    product_sku_or_name = request.GET.get('sku')
    query = request.GET.get('q')

    # is it a number?
    if product_sku_or_name.isdigit():
        sku = int(product_sku_or_name)
    # otherwise, is it a name?
    else:
        sku = sku_number(product_sku_or_name)

    product = product_name(sku)
    if product == '???':
        product = None

    results = SearchQuerySet().filter(text=query)
    if product:
        results = results.filter(sku=sku)

    return render(request, 'search/search.html', 
        {'query': query, 'results': results, 'product': product})