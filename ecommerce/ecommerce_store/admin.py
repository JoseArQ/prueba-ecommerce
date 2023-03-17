from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from ecommerce_store.models import EcommerceUser

admin.site.register(EcommerceUser, UserAdmin )