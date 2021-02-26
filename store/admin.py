from django.contrib import admin

from .models import Item, OrderItem, Order


class OrderItemInline(admin.TabularInline):
    model = OrderItem
 

class ItemAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['title', 'price', 'description']})
    ] 
    inlines = [OrderItemInline]
    list_display = ('title', 'price')
    list_filter = ['price', 'title']
    search_fields = ['title', 'price']


admin.site.register(Item, ItemAdmin)
admin.site.register(Order)
admin.site.register(OrderItem)



