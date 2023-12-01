from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import MainPageView, ProductList, ProductDetailView

urlpatterns = [
    path('', MainPageView.as_view(), name='home'),
    path('category/<slug:category_slug>/<int:page_number>', ProductList.as_view(), name="category"),
    path('product/<slug:product_slug>', ProductDetailView.as_view(), name="product")
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)