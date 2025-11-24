from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import Size, Material, Color, Gender, Categories, Product, SKU, ProductImage


# Register your models here.


class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1   
    fields = ("image", "preview")
    readonly_fields = ("preview",)

    def preview(self, obj):
        if obj.image:
            return mark_safe(
                f'<img src="{obj.image.url}" width="80" height="80" style="object-fit: cover;" />'
            )
        return "-"
    preview.allow_tags = True
    preview.short_description = "Preview"
    
    
class ProductAdmin(admin.ModelAdmin):
    
    model = Product
    inlines = [ProductImageInline]
    list_display = ['name', 'descriptions', 'categories', 'created_at', 'updated_at']
    search_fields = ['name', 'descriptions', 'categories__name']
    ordering = ['updated_at', 'created_at']
    
    #prepopulated_fields = {'slug': ('name',)}

admin.site.register(Product, ProductAdmin)


class SKUAdmin(admin.ModelAdmin):
    model = SKU
    list_display = ['product', 'size', 'color', 'get_materials', 'price', 'quantity', 'created_at', 'updated_at']
    search_fields = ['product__name', 'get_materials', 'size__name', 'color__name']
    ordering = ['product', 'size', 'color']

    def get_materials(self, obj):
        return ", ".join([material.name for material in obj.materials.all()])
    get_materials.short_description = 'Materials'

admin.site.register(SKU, SKUAdmin)

class GenderAdmin(admin.ModelAdmin):
    model = Gender
    list_display = ['name', 'slug', 'created_at', 'updated_at']
    search_fields = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}
    ordering = ['name']
    
admin.site.register(Size)
admin.site.register(Material)
admin.site.register(Color)
admin.site.register(Gender, GenderAdmin)
admin.site.register(Categories)