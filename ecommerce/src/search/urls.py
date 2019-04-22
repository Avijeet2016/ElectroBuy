from django.conf.urls import url


from search.views import (
    SearchProductView
)

urlpatterns = [

    url(r'^$', SearchProductView.as_view(), name="query"),

    
]
