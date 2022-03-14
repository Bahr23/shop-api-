from django.contrib import admin
from .models import Product, Category, CartItem, Profile, Shop


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    """ adding the product class to the admin site """

    list_display = (
        'name', "price", "quantity", "is_available", 'created', "discount", "shop")

    search_fields = ("name", "category", "shop")
    date_hierarchy = "created"
    list_editable = ['price', 'is_available', 'quantity', "discount", "shop"]
    prepopulated_fields = {'slug': ("name",)}


@admin.register(Shop)
class ShopAdmin(admin.ModelAdmin):
    """ adding the shop class to the admin site """

    list_display = ('name', "is_available", 'created', "user")
    list_display_links = ("name",)
    search_fields = ("name", "user")
    date_hierarchy = "created"
    list_editable = ['is_available', "user"]
    prepopulated_fields = {'slug': ("name",)}


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """ adding category class to the admin site """

    list_display = ("name", "slug", "is_lux", "parent_category")
    list_editable = ['is_lux', "parent_category"]
    prepopulated_fields = {'slug': ("name",)}


admin.site.register(CartItem)
admin.site.register(Profile)
