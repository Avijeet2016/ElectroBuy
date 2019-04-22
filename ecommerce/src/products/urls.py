from django.conf.urls import url


from .views import (
    ProductListView, 
    ProductDetailSlugView,
    products_by_category,
)

urlpatterns = [
    # url(r'check/taglist/$', tag_list, name='tag-list'),

    # url(r'check/catlist/(?P<tag>[\w-]+)/$', products_by_tag, name='p-by-tag'),

    url(r'^$', ProductListView.as_view(), name="list"),
    
    url(r'^(?P<slug>[\w-]+)/$', ProductDetailSlugView.as_view(), name='detail'),

    #url(r'category/list/$', category_list, name='category-list'),

    url(r'category/list/(?P<name>[\w-]+)/$', products_by_category, name='products-by-category'),
   
]

