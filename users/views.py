from django.contrib.auth.models import User, Group
from django.contrib.auth import login, authenticate
from django.contrib.auth import views as auth_views
from django.contrib import admin
from django.shortcuts import render, redirect, reverse

from rest_framework import permissions, viewsets, generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .forms import UserLoginForm

from .serializers import UserSerializer, GroupSerializer, UserCreateSerializer

admin.autodiscover()

class UserViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    queryset = User.objects.all()
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    required_scopes = ['groups']
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserCreate(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserCreateSerializer


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

def login_view(request):
    form = UserLoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        login(request, user)
        return redirect('home')


    context = {
        'form': form,
    }
    return render(request, "login.html", context)

def home_view(request):
    return render(request, "home.html")



# class UserLogin(APIView):
#     def post(self, request, format=None):
#         username = request.POST['username']
#         password = request.POST['password']
#         user = authenticate(username= username, password=password)
#         details= login(request, user)
#         return Response(1,status=status.HTTP_200_OK)