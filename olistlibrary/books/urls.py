from django.conf.urls import url, include
from django.views.generic import RedirectView
from rest_framework.documentation import include_docs_urls


urlpatterns = [
    url(r'^v1/', include('books.api.v1.urls')),
    url(r'^v1/docs/', include_docs_urls(title='Olist Library API')),
    url(r'^$', RedirectView.as_view(url='/v1/', permanent=False)),
]
