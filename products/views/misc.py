import django_filters
from django_filters import OrderingFilter
from rest_framework import viewsets
from rest_framework.filters import SearchFilter
from rest_framework.permissions import IsAuthenticated

from products.models import Order
from products.models import Review, Category
from products.permissions import IsOwnerOrReadOnly
from products.serializers import OrderSerializer, ReviewSerializer, CategorySerializer


class OrderViewSet(viewsets.ModelViewSet):
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class ReviewViewSet(viewsets.ModelViewSet):
    queryset =Review.objects.all()
    serializer_class = ReviewSerializer



class CategorViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]

    queryset = Category.objects.all()
    serializer_class = CategorySerializer