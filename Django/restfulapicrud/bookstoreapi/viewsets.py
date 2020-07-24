from rest_framework import viewsets
from . import models
from . import serializers
from rest_framework import filters
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend



class CustomerViewset(viewsets.ModelViewSet):
    queryset = models.Customer.objects.all()
    serializer_class = serializers.CustomerSerializer

    filter_backends = (DjangoFilterBackend, SearchFilter)
    filter_fields = ('id','custNum','custName')
  
    
class Place_OrderViewset(viewsets.ModelViewSet):
    queryset = models.Place_Order.objects.all()
    serializer_class = serializers.Place_OrderSerializer

    filter_backends = (DjangoFilterBackend, SearchFilter)
    filter_fields = ('id','PlaceOrderID','custNum','bookID')

class BillingViewset(viewsets.ModelViewSet):
    queryset = models.Billing.objects.all()
    serializer_class = serializers.BillingSerializer

    filter_backends = (DjangoFilterBackend, SearchFilter)
    filter_fields = ('id','billNum','custNum','cashierID')

class BookViewset(viewsets.ModelViewSet):
    queryset = models.Book.objects.all()
    serializer_class = serializers.BookSerializer

    filter_backends = (DjangoFilterBackend, SearchFilter)
    filter_fields = ('id','bookID','bookName','categoryID')

class CategoryViewset(viewsets.ModelViewSet):
    queryset = models.Category.objects.all()
    serializer_class = serializers.CategorySerializer

    filter_backends = (DjangoFilterBackend, SearchFilter)
    filter_fields = ('id','categoryID','categoryName')

class CashierViewset(viewsets.ModelViewSet):
    queryset = models.Cashier.objects.all()
    serializer_class = serializers.CashierSerializer

    filter_backends = (DjangoFilterBackend, SearchFilter)
    filter_fields = ('id','cashierID','cashierName')

class AuthorViewset(viewsets.ModelViewSet):
    queryset = models.Author.objects.all()
    serializer_class = serializers.AuthoerSerializer

    filter_backends = (DjangoFilterBackend, SearchFilter)
    filter_fields = ('id','authorID','authorName')

class PublisherViewset(viewsets.ModelViewSet):
    queryset = models.Publisher.objects.all()
    serializer_class = serializers.PublisherSerializer

    filter_backends = (DjangoFilterBackend, SearchFilter)
    filter_fields = ('id','publisherID','publisherName')

