from django.db import models
from .product import Product
from django.core.validators import RegexValidator

from django.contrib.auth import get_user_model
User = get_user_model()

phone_regex = RegexValidator(
    regex=r'\+998\d{9}$',
    message="Phone number must be in the format: '+998xxxxxxxxx'."
)

class Order(models.Model):
        PENDING ='Pending'
        PROCESSING = 'Processing'
        SHIPPED = 'Shipped'
        DELIVERED = 'Delivered'
        CANCELED = 'Canceled'

        STATUS_CHOICES = [
            (PENDING, 'Pending'),
            (PROCESSING, 'Processing'),
            (SHIPPED, 'Shipped'),
            (DELIVERED, 'Delivered'),
            (CANCELED, 'Canceled'),
        ]

        product = models.ForeignKey(Product, on_delete=models.CASCADE)
        customer = models.ForeignKey(User, on_delete=models.CASCADE)
        quantity = models.IntegerField(default=0)
        created_at = models.DateTimeField(auto_now_add=True)
        status = models.CharField(
            max_length=20,
            choices=STATUS_CHOICES,
            default=PENDING,
        )
        phone_number = models.CharField(validators=[phone_regex], max_length=13, blank=True, null=True)
        is_paid = models.BooleanField(default=False)


        def set_status(self, new_status):
            if new_status not in dict(self.STATUS_CHOICES):
                raise ValueError("Invalid status")
            self.status = new_status
            self.save()


        def is_tranzition_allowed(self, new_status):
            allowed_tranzitions = {
                self.PENDING: [self.PROCESSING, self.CANCELED],
                self.PROCESSING: [self.SHIPPED, self.CANCELED],
                self.SHIPPED: [self.DELIVERED, self.CANCELED],
            }

            return new_status in allowed_tranzitions.get(self.status, [])


        def __str__(self):
            return f"Order({self.product.name}) by "