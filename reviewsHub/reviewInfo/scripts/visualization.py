from pattern.web    import plaintext
from pattern.en     import parsetree
from pattern.search import search
from pattern.graph  import Graph
from reviewInfo.models import ReviewInfo

def compare_visualization(product_sku, compare_phrase):
    all_reviews = ReviewInfo.objects.all().filter(sku=product_sku)
    g = Graph()

    count = 0.0
    for e in all_reviews :
        s = e.comment.lower() 
        s = plaintext(s)
        s = parsetree(s)
        #p = '{NP} (VP) faster than {NP}'
        p = '{NP} (VP) ' + compare_phrase + ' {NP}'
        for m in search(p, s):
            x = m.group(1).string # NP left
            y = m.group(2).string # NP right
            if x not in g:
                g.add_node(x)
            if y not in g:
                g.add_node(y)
            g.add_edge(g[x], g[y], stroke=(0,0,0,0.75)) # R,G,B,A
        count += 1.0
        print count/len(all_reviews), '\r'

    if len(g) > 0: 
        g = g.split()[0] # Largest subgraph.
        for n in g.sorted()[:80]: # Sort by Node.weight.
            n.fill = (0, 0.5, 1, 0.75 * n.weight)

        g.export('static/compare_visualization', directed=True, weighted=2.0)
        return True
    else: 
        return False
