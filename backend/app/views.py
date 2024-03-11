from rest_framework import views, status
from rest_framework.response import Response
from .serializer import UsersSerializer, FriendsSerializer,ProductsSerializer
from .models import Users, Friends, Products

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
            


