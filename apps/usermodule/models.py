from django.db import models


class Address(models.Model):
    city = models.CharField(max_length=100)
    street = models.CharField(max_length=100)

    def __str__(self):
        return self.city


class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    address = models.ForeignKey(Address, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Address2(models.Model):
    city = models.CharField(max_length=100)
    street = models.CharField(max_length=100)

    def __str__(self):
        return self.city


class Student2(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    addresses = models.ManyToManyField(Address2)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField()
    image = models.ImageField(upload_to='products/')

    def __str__(self):
        return self.name