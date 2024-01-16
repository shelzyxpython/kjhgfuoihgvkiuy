from django.db import models


class Meal(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=300)
    price = models.IntegerField()
    ingredients = models.ManyToManyField('Ingredients')

    def str(self):
        return self.title


class Ingredients(models.Model):
    name = models.CharField(max_length=50)

    def str(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=10)
    size = models.IntegerField()
    maker = models.ManyToManyField('Maker')
    category = models.ManyToManyField('Category')
    price = models.IntegerField()

    def str(self):
        return self.name


class Maker(models.Model):
    name = models.CharField(max_length=50)
    country = models.CharField(max_length=50)

    def str(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=50)

    def str(self):
        return self.name
