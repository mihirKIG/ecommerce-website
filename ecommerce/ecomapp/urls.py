from django.urls import path
from . import views
 
urlpatterns = [
    path('', views.home, name='home'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('setting-dashboard/', views.setting_dashboard, name='setting_dashboard'),
    path('product-main-category-list/', views.product_main_category_list_view, name='product_main_category_list'),
    path('add-product-main-category/', views.add_product_main_category, name='add_product_main_category'),
    path('product-main-category-detailed/<int:pk>/', views.product_main_category_detailed, name='product_main_category_detailed'),
    path('product-main-category-edit/<int:pk>/', views.product_main_category_edit, name='product_main_category_edit'),
    path('product-main-category-delete/<int:pk>/', views.product_main_category_delete, name='product_main_category_delete'),
    path('product-list/', views.product_list, name='product_list')
    # path('login/', views.login_view, name='login'),
    # path('logout/', views.logout_view, name='logout'),
    # path('register/', views.register, name='register'),
    
]