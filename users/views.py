from django.contrib.auth import authenticate
from django.contrib.auth.models import User

from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from .models import Profile
from .serializers import *
# Create your views here.

@api_view(['GET', 'POST'])
def user_list(request):
    if request.method == 'GET':
        data = User.objects.all()
        
        
        serializer = UserSerializer(data, context={'request': request}, many=True)
        
        return Response(serializer.data)

    elif request.method == 'POST':
        commited = False
        serializer = UserSerializer(data=request.data)
        username = request.data["username"]
        profile_data = request.data.pop("profile")
        
        
        if serializer.is_valid():
            user = User.objects.create_user(**request.data)
            profile = Profile(user=user)
            profile_data["user_id"] = int(user.pk)
            profile_serializer = ProfileSerializer(data=profile_data)
            
            if profile_serializer.is_valid():
                
                profile_serializer.save()
                
            return Response(status=status.HTTP_201_CREATED)
            
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




@api_view(['GET'])
def users_filtrados(request,username):
        if request.method=='GET':
            try:
                data = User.objects.filter(username=username)
            except User.DoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND)

            serializer =UserSerializer(data, context={'request': request}, many=True)

            return Response(serializer.data)


