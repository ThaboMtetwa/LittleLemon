from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
# from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from .models import MenuItem
from .serializers import MenuItemSerializer

# Create your views here.
class MenuItemsView(ListCreateAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
    # permission_classes = [IsAuthenticatedOrReadOnly]

class SingleMenuItemView(RetrieveUpdateDestroyAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
    # permission_classes = [IsAuthenticated]
