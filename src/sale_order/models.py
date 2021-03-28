from django.db import models
from django.urls import reverse


# Create your models here.
class SaleOrder(models.Model):
    client_name = models.CharField(max_length=120)
    delivery_date = models.DateField()
    product_description = models.TextField()

    def get_absolute_url(self):
        return reverse("sale_order:order_detail", kwargs={"id": self.id})

