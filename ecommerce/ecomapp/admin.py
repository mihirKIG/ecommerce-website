from django.contrib import admin
from .models import MenuList, UserPermission, ProductMainCategory, ProductSubCategory

@admin.register(MenuList)
class MenuListAdmin(admin.ModelAdmin):
    list_display = ('id', 'menu_name', 'module_name', 'menu_url', 'is_main_menu', 'created_by', 'is_active')
    search_fields = ('menu_name', 'module_name', 'menu_url')
    list_filter = ('is_main_menu', 'is_active')
    ordering = ('id',)

@admin.register(UserPermission)
class UserPermissionAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'menu', 'can_view', 'can_add', 'can_update', 'can_delete', 'is_active')
    list_filter = ('is_active', 'can_view', 'can_add', 'can_update', 'can_delete')
    search_fields = ('user__username', 'menu__menu_name')
    ordering = ('id',)
    
@admin.register(ProductMainCategory)
class ProductMainCategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'main_cat_name', 'cat_slug', 'cat_image', 'cat_ordering', 'created_by', 'is_active')
    search_fields = ('main_cat_name', 'cat_slug')
    list_filter = ('is_active',)
    ordering = ('id',)

@admin.register(ProductSubCategory)
class ProductSubCategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'sub_cat_name', 'sub_cat_slug', 'sub_cat_image', 'sub_cat_ordering', 'created_by', 'is_active')
    search_fields = ('sub_cat_name', 'sub_cat_slug')
    list_filter = ('is_active',)
    ordering = ('id',)
