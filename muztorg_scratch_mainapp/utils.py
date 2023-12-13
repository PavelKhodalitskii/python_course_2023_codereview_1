from .models import Product, ProductDetails

def get_best_deals():
    best_deals = []
    queryset = Product.objects.all()
    
    queryset = queryset.filter(details__raiting__gte=4.4)
    guitar_index = Product.ProductType.values.index("EG")
    acoustic_guitar_index = Product.ProductType.values.index("AG")
    guitar_amp_index = Product.ProductType.values.index("GA")
    synth_index = Product.ProductType.values.index("Sn")

    guitars = queryset.filter(category=Product.ProductType.choices[guitar_index][0])
    acoustic_guitars = queryset.filter(category=Product.ProductType.choices[acoustic_guitar_index][0])
    amps = queryset.filter(category=Product.ProductType.choices[guitar_amp_index][0])
    synths = queryset.filter(category=Product.ProductType.choices[synth_index][0])
    best_deals.append(guitars[0] if guitars else None)
    best_deals.append(acoustic_guitars[0] if acoustic_guitars else None)
    best_deals.append(amps[0] if amps else None)
    best_deals.append(synths[0] if synths else None)
    return best_deals


    