from django.contrib import admin

# Register your models here.

from .models import Product, ProductDetails, ProductPhotos, Photo

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'image', 'details')

class ProductDetailsAdmin(admin.ModelAdmin):
    list_display = ('product', 'about', 'raiting')

class ProductPhotosAdmin(admin.ModelAdmin):
    list_display = ('photos', )

class PhotoAdmin(admin.ModelAdmin):
    list_display = ('photo', )

admin.site.register(Product, ProductAdmin)
admin.site.register(ProductDetails, ProductDetailsAdmin)
admin.site.register(ProductPhotos, ProductPhotosAdmin)
admin.site.register(Photo, PhotoAdmin)
