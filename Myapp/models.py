from django.db import models

class Product(models.Model):
  name = models.CharField(max_length=100)
  description = models.TextField()
  price = models.DecimalField(max_digits=10, decimal_places=2)
  rating = models.DecimalField(max_digits=3, decimal_places=1)
  picture = models.ImageField(upload_to='product_images/')

  def __str__(self):
    return self.name + " " + str(self.price) + " DA"

  class Meta:
    db_table = 'products'
    managed = True
    verbose_name = 'Product'
    verbose_name_plural = 'liste des produits'
