from django.shortcuts import render, redirect
from reviewInfo.scripts.visualization import compare_visualization
#from reviewInfo.scripts.summarize import SimpleSummarizer
from reviewInfo.models import product_name, sku_number

# Create your views here.
def visualize(request):
    compare_phrase = request.GET.get('p', 'better than')
    product_sku_or_name = request.GET.get('sku', '5717547')
    
    # is it a number?
    if product_sku_or_name.isdigit():
        sku = int(product_sku_or_name)
    # otherwise, is it a name?
    else:
        sku = sku_number(product_sku_or_name)

    product = product_name(sku)
    if product == '???':
        product = None

    if product:
        if compare_visualization(sku, compare_phrase):
            return redirect('/static/compare_visualization/index.html')
        else:
            return redirect('/static/not_found.html')
    else:
        return redirect('/')

