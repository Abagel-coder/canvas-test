from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50)
    class Meta:
        verbose_name_plural = "Catergories"
    def __str__(self):
        return self.title
class Product(models.Model):
    user = models.ForeignKey(User,related_name="product",on_delete=models.CASCADE)
    category = models.ForeignKey(Category,related_name="product",on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to="uploads/product_images/",blank=True,null=True)
    slug = models.SlugField(max_length=50)
    description= models.TextField(blank=True)
    price = models.IntegerField()


    def __str__(self):
        return self.title
    def get_display_price(self):
        return self.price/100