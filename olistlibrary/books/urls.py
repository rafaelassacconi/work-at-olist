from django.conf.urls import url, include
from django.views.generic import RedirectView


urlpatterns = [
    url(r'^v1/', include('books.api.v1.urls')),
    url(r'^$', RedirectView.as_view(url='/v1/', permanent=False)),
]