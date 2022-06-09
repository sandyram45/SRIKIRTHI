from django.contrib import admin
from .models import DailyExpenses, VehicleExpenses, SalaryExpenses


class DailyExpensesAdmin(admin.ModelAdmin):
    list_display = ('date', 'expense', 'description', 'amount')


class VehicleExpensesAdmin(admin.ModelAdmin):
    list_display = ('date', 'vehicle_number', 'description', 'amount')


admin.site.register(DailyExpenses, DailyExpensesAdmin)
admin.site.register(VehicleExpenses, VehicleExpensesAdmin)
admin.site.register(SalaryExpenses)