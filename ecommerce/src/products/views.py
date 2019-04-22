from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from .models import Product, Category
from django.http import Http404
#from tags.models import Tag 
from carts.models import Cart
# Create your views here.


# def tag_list(request):
#     tags = Tag.objects.all()
#     context = {
#         'tags': tags
#     }
#     return render(request, 'products/tag_list.html', context)


# def products_by_tag(request, tag):
#     t = Tag.objects.get(title=tag)
#     product_list = Product.objects.filter(tag=t)
#     context = {
#         'products': product_list
#     }
#     return render(request, 'products/product_by_tag.html', context)

# def category_list(request):
#     cat = Category.objects.all()
#     context = {
#         'cat': cat
#     }
#     return render(request, 'products/category_list.html', context)


def products_by_category(request, name):
    category = Category.objects.get(name=name)
    products = Product.objects.filter(category=category)
    context = {
        'category': category,
        'products': products
    }
    return render(request, 'products/products_by_category.html', context)
    


class ProductFeaturedListView(ListView):
    template_name = "products/list.html"

    def get_queryset(self, *args, **kwargs):
        request = self.request
        return Product.objects.all().featured()


class ProductFeaturedDetailView(DetailView):
    queryset = Product.objects.all().featured()
    template_name = "products/featured-detail.html"

    # def get_queryset(self, *args, **kwargs):
    #     request = self.request
    #     return Product.objects.featured()





class ProductListView(ListView):
    #queryset = Product.objects.all()
    template_name = "products/list.html"

    #def get_context_data(self, *args, **kwargs):
    #    context = super(ProductListView, self).get_context_data(*args, **kwargs)
    #    return context
    def get_context_data(self, *args, **kwargs):
        context = super(ProductListView, self).get_context_data(*args, **kwargs)
        cart_obj, new_obj = Cart.objects.new_or_get(self.request)
        context['cart'] = cart_obj
        return context

    def get_queryset(self, *args, **kwargs):
        request = self.request
        return Product.objects.all()

def product_list_view(request):
    queryset = Product.objects.all()
    context = {
        "object_list": queryset
    }
    return render(request, "products/product_list.html", context)


class ProductDetailSlugView(DetailView):
    queryset = Product.objects.all()
    template_name = "products/detail.html"

    def get_context_data(self, *args, **kwargs):
        context = super(ProductDetailSlugView, self).get_context_data(*args, **kwargs)
        cart_obj, new_obj = Cart.objects.new_or_get(self.request)
        context['cart'] = cart_obj
        return context


    def get_object(self, *args, **kwargs):
        request = self.request
        slug = self.kwargs.get('slug')
        #instance = get_object_or_404(Product, slug=slug, active=True)
        try:
            instance = Product.objects.get(slug=slug, active=True)
        except Product.DoesNotExist:
            raise Http404("Not found ...")
        except Product.MultipleObjectsReturned:
            qs = Product.objects.filter(slug=slug, active=True)
            instance = qs.first()
        except:
            raise Http404("Uhhmmm")
        return instance



class ProductDetailView(DetailView):
    # queryset = Product.objects.all()
    template_name = "products/detail.html"

    def get_context_data(self, *args, **kwargs):
        context = super(ProductDetailView, self).get_context_data(*args, **kwargs)
        print(context)
        return context
    
    def get_object(self, *args, **kwargs):
        request = self.request
        pk = self.kwargs.get('pk')
        instance = Product.objects.get_by_id(pk)
        if instance is None:
            raise Http404('Product does not exist')
        return instance

def product_detail_view(request, pk=None, *args, **kwargs):
    #instance = Product.objects.all(pk=pk, featured=True) #id
    #instance = get_object_or_404(Product, pk=pk, featured=True)
    # try:
    #     instance = Product.objects.filter(id=4)
    # except Product.DoesNotExist:
    #     print('no product here')
    #     raise Http404('Product does not exit')
    # except:
    #     print('huh?')
    instance = Product.objects.get_by_id(pk)
    if instance is None:
        raise Http404('Product does not exist')
    # qs = Product.objects.filter(id=pk)
    # if qs.exists() and qs.count() == 1:
    #     instance = qs.first()
    # else:
    #     raise Http404('Product doesnot exist')


    context = {
        "object": instance
    }
    return render(request, "products/detail.html", context)

