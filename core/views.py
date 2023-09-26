from django.db.models import Count
from django.shortcuts import render
from django.db.models import Q
from typing import Any, Dict
from django.shortcuts import render
from django.views.generic import (
    TemplateView,
    DetailView,
    ListView,
    View
)
from .models import (
    Category,
    Product,
    Banner

)

class Home(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context  = super().get_context_data(**kwargs)
        context['products'] = Category.objects.all()
        
        context.update(
            {
                'featured_categories' : Category.objects.filter(featured=True),
                'featured_products' : Product.objects.filter(featured=True),
                'products' : Product.objects.all(),
                'top_rated': Product.objects.filter(top_rated = True),
                'on_sale' : Product.objects.filter(on_sale = True),
                'banners' : Banner.objects.filter(active=True)
                # 'cat_products' : Category.objects.annotate(items_count=Count('products'))
                                                        
                # 'sliders' : Slider.objects.filter(show=True)
            }
        )
        return context
    