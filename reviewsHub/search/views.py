from django.shortcuts import render
from haystack.query import SearchQuerySet

from reviewInfo.models import product_name

from haystack.utils import Highlighter
from django.utils.html import strip_tags

class NoCropHighlighter(Highlighter):
    def highlight(self, text_block):
        self.text_block = strip_tags(text_block)
        highlight_locations = self.find_highlightable_words()
        start_offset, end_offset = self.find_window(highlight_locations)
        start_offset = 0
        return self.render_html(highlight_locations, start_offset, end_offset)

def search(request):
    sku = request.GET.get('sku')
    query = request.GET.get('q')

    product = None
    if sku:
        product = product_name(int(sku))
        if product == '???':
            product = None

    results = SearchQuerySet().filter(text=query)
    if sku:
        results = results.filter(sku=sku)

    return render(request, 'search/search.html', 
        {'query': query, 'results': results, 'product': product})