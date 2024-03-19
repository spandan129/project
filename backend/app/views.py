from rest_framework import views, status
from rest_framework.response import Response
from .serializer import CommentSerializer, UsersSerializer, FriendsSerializer,ProductsSerializer, PostSerializer
from .models import Users, Friends, User_Friends, Products, Post, Comment

class LoginApi(views.APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user_data = {'user_name': username, 'password': password}
        user_serializer = UsersSerializer(data=user_data)
        if user_serializer.is_valid():
            user_serializer.save()
            
            return Response({'message': 'User created successfully'}, status=status.HTTP_201_CREATED)
        else:
            return Response({'error': user_serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):  
        username = request.data.get('username')
        password = request.data.get('password')
        
        try:
            user = Users.objects.get(user_name=username, password=password)
            if user is not None:
              return Response({'message': 'Logged in'}, status=status.HTTP_200_OK)
        except Users.DoesNotExist:
            return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)

class ChatRender(views.APIView):
    def get(self, request):
        friends = Friends.objects.all()
        serializer = FriendsSerializer(friends, many=True) 
        return Response(serializer.data)
class SendMessage(views.APIView):
    def post(self, request):
        userid = request.data.get('friendid')
        message = request.data.get('messages')
        friend = Users.object.get(user_id=userid)

class ProductsAPIView(views.APIView):
    def get(self, request):
        products = Products.objects.all()
        serializer = ProductsSerializer(products, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ProductsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, product_id):
        try:
            to_delete_product = Products.objects.get(product_id=product_id)
            if to_delete_product is not None:
                to_delete_product.delete()
                return Response(f'{product_id} deleted successfully')
        except Products.DoesNotExist:
            return Response(f'Product with ID {product_id} does not exist', status=status.HTTP_404_NOT_FOUND)
            
class PostAPIView(views.APIView):
    def post(self, request):
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

class CommentView(views.APIView):
    def get(self, request, post_id):
        comments = Comment.objects.filter(post_id=post_id)
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)

    def post(self, request, post_id):
        data = {"user_id":request.data['user_id'], "post_id":post_id, "actual_comment":request.data['actual_comment']}
        serializer = CommentSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.error_messages)

class AddFriendView(views.APIView):
    def get(self, request, user_id, friend_id):
        try:
            user = Users.objects.get(user_id = user_id)
        except Exception as e:
            print(e)
        
        try:
            friend = Users.objects.get(user_id = friend_id)
        except Exception as e:
            print(e)

        try:
            friend_object = Friends.objects.create(friend_id=friend_id,friend_name=friend.user_name)
            friend_object.save()
        except:
            friend_object = Friends.objects.get(friend_id=friend_id)

        user_friends_entry = User_Friends.objects.create(user_id=user, friend_id=friend_object)
        user_friends_entry.save()
        return Response("Friend saved", status=status.HTTP_201_CREATED)

class FetchPostView(views.APIView):
    def get(self, request,user_id):
        friends = [x.friend_id.friend_id for x in User_Friends.objects.all() if x.user_id.user_id==user_id]
        posts = Post.objects.filter(user_id__in = friends)
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class LikeView(views.APIView):
    def get(self, request, post_id):
        try:
            post = Post.objects.get(post_id=post_id)
        except Exception as e:
            return Response({"Post": "Not found"})
        
        if post.like_count is None:
            post.like_count = 1
        else:
            post.like_count += 1
        post.save()
        return Response("Like Updated")