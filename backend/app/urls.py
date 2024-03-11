from django.urls import path
from .views import ProductsAPIView
from .views import LoginApi, ChatRender
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('login', LoginApi.as_view(), name='login'),
    path('chat/', ChatRender.as_view(), name='chat'),
    path('products', ProductsAPIView.as_view(), name='products-api'),
    path('products/<str:product_id>', ProductsAPIView.as_view(), name='products-api-detail'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)