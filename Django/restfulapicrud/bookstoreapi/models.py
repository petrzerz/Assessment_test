from django.db import models

# Create your models here.
class Customer(models.Model):
    custNum = models.IntegerField()
    custName = models.CharField(max_length = 100)

class Place_Order(models.Model):
    placeorderID = models.CharField(max_length = 100)
    custNum = models.IntegerField()
    bookID = models.IntegerField()

class Category(models.Model):
    categoryID = models.CharField(max_length = 100)
    categoryName = models.CharField(max_length= 100)

class Book(models.Model):
    bookID = models.IntegerField()
    bookName = models.CharField(max_length= 100)
    categoryID = models.CharField(max_length= 100)


class Billing(models.Model):
    billNum = models.IntegerField()
    custNum = models.IntegerField()
    cashierID = models.IntegerField()

class Cashier(models.Model):
    cashierID = models.IntegerField()
    chashierName = models.CharField(max_length =100)

class Author(models.Model):
    authorID = models.IntegerField()
    authorName = models.CharField(max_length=100)

class Publisher(models.Model):
    publisherID = models.IntegerField()
    publisherName = models.CharField(max_length= 100)
