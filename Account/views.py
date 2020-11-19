from django.contrib.auth import authenticate
from django.contrib.auth.hashers import check_password
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from ResponseHandle import exception_handler

from .models import MyUser
from .serializers import RoleSerializer, MyUserSerializer


class Role(APIView):
    def post(self, request):
        serializer = RoleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return exception_handler.error_handling(data=serializer.data, )
        return exception_handler.error_handling(errMsg=serializer.errors)


@api_view(['POST'])
def signup(request):
    if not request.data:
        return exception_handler.error_handling(errMsg="invalid access")

    email = MyUser.objects.filter(email=request.data['email'])

    if len(email) != 0:
        return exception_handler.error_handling(errMsg="Email id is already register.")

    serializer = MyUserSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
        return exception_handler.error_handling(data=serializer.data)
    return exception_handler.error_handling(errMsg=serializer.errors)



@api_view(['POST'])
@permission_classes([AllowAny])
def user_login(request):
    try:
        email = request.data['email']
        password = request.data['password']

        try:
            myuser = MyUser.objects.get(email__exact=email)
        except MyUser.DoesNotExist:
            output = "email is not registered......"
            return exception_handler.error_handling(errMsg=output)

        if not check_password(password, myuser.password):
            output = "password  is wrong"
            return exception_handler.error_handling(errMsg=output)

        user = authenticate(email=email, password=password)

        if user:
            data = {
                'id':user.id,
                'email':user.email,
                'role_type':user.role_id.role_type
            }
            return exception_handler.error_handling(data=data)
        else:
            output = 'can not authenticate with the given credentials or the account has been deactivated'
            return exception_handler.error_handling(errMsg=output)
    except KeyError:
        output = 'please provide a email and a password'
        return exception_handler.error_handling(errMsg=output)
