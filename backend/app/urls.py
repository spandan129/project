from django.urls import path
from .views import LoginApi, ChatRender

urlpatterns = [
    path('login', LoginApi.as_view(), name='login'),
    path('chat/', ChatRender.as_view(), name='chat'),
]
