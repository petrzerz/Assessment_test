from rest_framework import serializers
from .models import Customer, Place_Order, Category, Book, Billing, Cashier, Author, Publisher


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'

class Place_OrderSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Place_Order
        fields = '__all__'
        
class CategorySerializer(serializers.ModelSerializer):  
    class Meta: 
        model = Category
        fields = '__all__'

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

class BillingSerializer(serializers.ModelSerializer):
   
    class Meta:
        model = Billing
        fields = '__all__' 
class CashierSerializer(serializers.ModelSerializer):
   
    class Meta:
        model = Cashier
        fields = '__all__'
class AuthoerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Author
        fields = '__all__'

class PublisherSerializer(serializers.ModelSerializer):
   
    class Meta:
        model = Publisher
        fields = '__all__'