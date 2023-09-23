from django.utils.safestring import mark_safe
from django.db import models
from shortuuid.django_fields import ShortUUIDField
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
    cid = ShortUUIDField(
        length=10,
        max_length=20,
        prefix="cat_",
        alphabet="abcdefgh12345",
        unique = True
    )
    title = models.CharField(max_length=150)
    icon = models.ImageField(upload_to='category_icons')

    class Meta:
        verbose_name_plural = 'Categories'
        ordering = ['-title']

        def category_icon(self):
            return mark_safe('<img src="%s" width = "50" height = "50" />' % (self.icon.url))
        
        def __str__(self) -> str:
            return self.title
        
class Tag(models.Model):
    pass
        

class Product(models.Model):
    pid = ShortUUIDField(
        length=10,
        max_length=20,
        prefix="pro_",
        alphabet="abcdefgh12345",
        unique = True

    )

    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null= True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null= True)

    title = models.CharField(max_length=250, default='produt name')
    image = models.ImageField(upload_to='product_images')
    description = models.TextField(blank=True, null= True, default="product descrption.....")
    price = models.DecimalField(max_digits=9999999999,decimal_places=2, default="0.99")
    old_price = models.DecimalField(max_digits=9999999999,decimal_places=2, default="1.99")
    specifications = models.TextField(null=True,blank=True)
    tags = models.ForeignKey(Tag, on_delete=models.SET_NULL, null=True)
    product_status = models.CharField(choices=STATUS, max_length=10,)

    status = models.BooleanField(default=True)
    in_stock = models.BooleanField(default=True)
    featured = models.BooleanField(default=False)
    digital = models.BooleanField(default=False)

    sku = ShortUUIDField(
        length=6,
        max_length=10,
        prefix="sku_",
        alphabet="1234567890",
        unique = True
    )

    creatd_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True,blank=True)

    class Meta:
        verbose_name_plural = 'Products'
        ordering = ['-creatd_at']

        def product_image(self):
            return mark_safe('<img src="%s" width = "50" height = "50" />' % (self.image.url))
        
        def __str__(self) -> str:
            return self.title
        def get_percetage(self):
            new_price = (self.price / self.old_price) * 100
            return new_price
        
class ProductImage(models.model):
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
        verbose_name_plural = 'Cart Oders'

class Orderitems(models.Model):
    order = models.ForeignKey(CartOrer, on_delete=models.CASCADE)
    product_status = models.CharField(max_length=200)
    item = models.CharField(max_length=200)
    image = models.CharField(max_length=200)
    qty = models.IntegerField(default=0)
    price = models.DecimalField(max_digits=9999999999,decimal_places=2, default="0.99")
    total = models.DecimalField(max_digits=9999999999,decimal_places=2, default="0.99")