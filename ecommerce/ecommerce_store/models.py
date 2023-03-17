from django.db import models
from django.contrib.auth.models import AbstractUser

class EcommerceUser(AbstractUser):
    pass

class EcommerceStore(models.Model):
    ecommerce_user = models.ForeignKey(
        to=EcommerceUser,
        on_delete=models.CASCADE, 
        null=False,
        blank=False
        )
    name = models.CharField(max_length=200, verbose_name='store name')
    address = models.CharField(max_length=200, verbose_name='store address')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


