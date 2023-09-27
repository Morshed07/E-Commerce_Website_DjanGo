from django.contrib import admin
from .models import *


#Register your models here.

class BannerAdmin(admin.ModelAdmin):
    list_display = ['brand_name','banner_img','active']

class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ('title',)}
    list_display = ['user','title','product_image','price', 'featured', 'product_status','top_rated', 'on_sale']

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ('title',)}
    list_display = ['title','category_icon', 'featured']

class CartOrerAdmin(admin.ModelAdmin):
    list_display = ['user','price','paid_status','product_status','order_date']


class CartOrerItemsAdmin(admin.ModelAdmin):
    list_display = ['order','invoice_no','item', 'image','qty', 'price', 'total']

class ProductReviewAdmin(admin.ModelAdmin):
    list_display = ['user','product','review', 'rating']

class WishlistAdmin(admin.ModelAdmin):
    list_display = ['user','product','date']

class AddressAdmin(admin.ModelAdmin):
    list_display = ['user','address','status']


admin.site.register(Product,ProductAdmin)
admin.site.register(Category,CategoryAdmin)
admin.site.register(CartOrer,CartOrerAdmin)
admin.site.register(CartOrerItems,CartOrerItemsAdmin)
admin.site.register(ProductReview,ProductReviewAdmin)
admin.site.register(Wishlist,WishlistAdmin)
admin.site.register(Address,AddressAdmin)
admin.site.register(Banner,BannerAdmin)

