from django.urls import path
from .views import FetchPostView, ProductsAPIView, LikeView, PostAPIView, CommentView, AddFriendView
from .views import LoginApi, ChatRender
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('login', LoginApi.as_view(), name='login'),
    path('chat/', ChatRender.as_view(), name='chat'),
    path('products', ProductsAPIView.as_view(), name='products-api'),
    path('products/<str:product_id>', ProductsAPIView.as_view(), name='products-api-detail'),
    path('post/', PostAPIView.as_view(), name="post-api"),
    path('add_friend/<int:user_id>/<int:friend_id>', AddFriendView.as_view(),name="add-friend"),
    path('post/<int:user_id>', FetchPostView.as_view(), name="fetch-post"),
    path('comment/<int:post_id>', CommentView.as_view(), name="comment"),
    path('react/<int:post_id>', LikeView.as_view(), name="react"),
]