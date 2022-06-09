from django.contrib import admin
from .models import Location, ShopDetails, Sales, Rate, Collections


class LocationAdmin(admin.ModelAdmin):
    list_display = ('location',)


class ShopAdmin(admin.ModelAdmin):
    list_display = ('shop_location', 'name')


class RateAdmin(admin.ModelAdmin):
    list_display = ('shop', 'date', 'rate', 'status',)


class SalesAdmin(admin.ModelAdmin):
    list_display = ('date', 'shop_name', 'no_of_cylinders', 'amount', 'no_of_empty', 'paid_amount',)


class CollectionAdmin(admin.ModelAdmin):
    list_display = ('date', 'shop_name', 'collection_amount',)


admin.site.register(Location, LocationAdmin)
admin.site.register(ShopDetails, ShopAdmin)
admin.site.register(Sales, SalesAdmin)
admin.site.register(Rate, RateAdmin)
admin.site.register(Collections, CollectionAdmin)


