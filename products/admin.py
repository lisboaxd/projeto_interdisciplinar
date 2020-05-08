from django.contrib import admin
from products.models import (
    Product, TypeProduct,
    Donor, CompanyAssociate, Company
)

admin.site.register(Product)
admin.site.register(TypeProduct)
admin.site.register(Donor)
admin.site.register(Company)
admin.site.register(CompanyAssociate)