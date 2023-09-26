
from django.utils.safestring import mark_safe
from django.db import models
from userauths.models import User


# Create your models here.





STATUS_CHOICES = (
    ("processing", "Processing"),
    ("shipped", "Shipped"),
    ("delivered", "Delivered")
)


STATUS = (
    ("draft", "Draft"),
    ("disabled", "Disabled"),
    ("rejected", "Rejected"),
    ("in_review", "In Review"),
    ("published", "Published")
)


RATING = (
    (1, "★☆☆☆☆"),
    (2, "★★☆☆☆"),
    (3, "★★★☆☆"),
    (4, "★★★★☆"),
    (5, "★★★★★")
)


class Category(models.Model):
    title = models.CharField(max_length=150)
    slug= models.SlugField(unique=True, max_length=150)
    featured = models.BooleanField(default=True)
    icon = models.ImageField(upload_to='category_icons')
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Categories'
        ordering = ['-date']

    def category_icon(self):
        return mark_safe('<img src="/media/%s" width = "50" height = "50" />' % (self.icon))
        
    def __str__(self) -> str:
        return self.title
        
class Tag(models.Model):
    pass
        

class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null= True, related_name="products")
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null= True)

    title = models.CharField(max_length=250, default='product name')
    slug= models.SlugField(unique=True, max_length=250)
    image = models.ImageField(upload_to='product_images')
    description = models.TextField(blank=True, null= True, default="product descrption.....")
    price = models.DecimalField(max_digits=9999999999,decimal_places=2, default="0.99")
    old_price = models.DecimalField(max_digits=9999999999,decimal_places=2, default="1.99")
    specifications = models.TextField(null=True,blank=True)
    # tags = models.ForeignKey(Tag, on_delete=models.SET_NULL, null=True)
    product_status = models.CharField(choices=STATUS, max_length=10, default='in_review')

    status = models.BooleanField(default=True)
    in_stock = models.BooleanField(default=True)
    featured = models.BooleanField(default=False)
    top_rated = models.BooleanField (default=False)
    on_sale = models.BooleanField(default=False)
    digital = models.BooleanField(default=False)

    creatd_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True,blank=True)

    class Meta:
        verbose_name_plural = 'Products'
        ordering = ['-creatd_at']

    def product_image(self):
        return mark_safe('<img src="/media/%s" width = "50" height = "50" />' % (self.image))
        
    def __str__(self) -> str:
        return self.title
        
    def get_percetage(self):
        new_price = (self.price / self.old_price) * 100
        return new_price
        
class ProductImage(models.Model):
    image = models.ImageField(upload_to='product_images')
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Product Images"

##########cart, orderitems, order and address###########

class CartOrer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=9999999999,decimal_places=2, default="0.99")
    paid_status = models.BooleanField(default=False)
    order_date = models.DateTimeField(auto_now_add=True)
    product_status = models.CharField(choices=STATUS_CHOICES, max_length=30, default='processing')

    class Meta:
        verbose_name_plural = 'Cart Orders'

class CartOrerItems(models.Model):
    order = models.ForeignKey(CartOrer, on_delete=models.CASCADE)
    invoice_no = models.CharField(max_length=200)
    product_status = models.CharField(max_length=200)
    item = models.CharField(max_length=200)
    image = models.CharField(max_length=200)
    qty = models.IntegerField(default=0)
    price = models.DecimalField(max_digits=9999999999,decimal_places=2, default="0.99")
    total = models.DecimalField(max_digits=9999999999,decimal_places=2, default="0.99")

    class Meta:
        verbose_name_plural = 'Cart Order items'

    def order_image(self):
        return mark_safe('<img src="/media/%s" width = "50" height = "50" />' % (self.image))
    
class ProductReview(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null= True)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null= True)
    review = models.TextField()
    rating = models.IntegerField(choices=RATING, default=None)
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Product Review'
        
    def __str__(self) -> str:
        return self.product.title

    def get_rating(self):
        return self.rating


class Wishlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null= True)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null= True)
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Wishlists'
        
        def __str__(self) -> str:
            return self.product.title

class Address(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null= True)
    address = models.CharField(max_length=200,null=True)
    status = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = 'Addresses'

class Banner(models.Model):
    banner_img  = models.ImageField(upload_to='top_banner_img')
    brand_name = models.CharField(max_length=100)
    brand_title = models.CharField(max_length=100)
    brand_category_message = models.CharField(max_length=100)
    active = models.BooleanField(default=True)
    created_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Banners'
        ordering = ['-created_date']
    
    def banner_image(self):
        return mark_safe('<img src="/media/%s" width = "70" height = "50" />' % (self.banner_img))