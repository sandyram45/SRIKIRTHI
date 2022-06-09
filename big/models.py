from django.utils import timezone
from django.db import models
from django.db.models import Sum

# Create your models here.


class Location(models.Model):
    location = models.CharField(max_length=30)

    def __str__(self):
        return self.location

    @property
    def total_cylinders(self):
        return ShopDetails.objects.filter(shop_location__location=self.location).count()


class ShopDetails(models.Model):
    shop_location = models.ForeignKey(Location, on_delete=models.RESTRICT)
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name

    @property
    def total_cylinders_count(self):
        d = Sales.objects.filter(shop_name__name=self.name).aggregate(cylinder=Sum('no_of_cylinders'))

        if d['cylinder'] == None:
            return 0
        else:
            return d['cylinder']

    @property
    def outstanding_balances(self):
        a = Sales.objects.filter(shop_name__name=self.name).aggregate(total=Sum('amount'))
        b = Sales.objects.filter(shop_name__name=self.name).aggregate(paid=Sum('paid_amount'))
        c = Collections.objects.filter(shop_name__name=self.name).aggregate(collect=Sum('collection_amount'))

        if a['total'] == None or b['paid'] == None:
            return 0

        if c['collect'] == None :
            c = 0
            return a['total'] - b['paid'] - c

        else:
            return a['total'] - b['paid'] - c['collect']


class Rate(models.Model):
    shop = models.ForeignKey(ShopDetails, on_delete=models.RESTRICT)
    date = models.DateField(default=timezone.now)
    rate = models.SmallIntegerField()
    status_choices = [('ACTIVE', 'Active'), ('INACTIVE', 'Inactive')]
    status = models.CharField(max_length=8, choices=status_choices, default='Active')

    def __int__(self):
        return self.rate


class Sales(models.Model):
    date = models.DateField(default=timezone.now)
    shop_name = models.ForeignKey(ShopDetails, on_delete=models.CASCADE)
    no_of_cylinders = models.PositiveSmallIntegerField()
    amount = models.PositiveIntegerField(default=0)
    no_of_empty = models.PositiveSmallIntegerField(default=0)
    paid_amount = models.PositiveIntegerField(default=0)


class Collections(models.Model):
    date = models.DateField(default=timezone.now)
    shop_name = models.ForeignKey(ShopDetails, on_delete=models.CASCADE)
    collection_amount = models.PositiveIntegerField()
