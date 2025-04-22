from django.contrib import admin
from .models import Category, Product
from import_export.admin import ExportMixin
from import_export.admin import ImportExportModelAdmin


class ProductAdmin(ImportExportModelAdmin):  # 👈 this is the important line
    list_display = ('name', 'price', 'category')

admin.site.register(Category)
admin.site.register(Product, ProductAdmin)
