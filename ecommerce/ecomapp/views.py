from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .models import MenuList, ProductMainCategory
from django.contrib.auth.models import User
from django.contrib import messages
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from ecomapp.common_func import checkUserPermission  



def home(request):
    return render(request, "ecomapp/home.html")

def dashboard(request):
    return render(request, "ecomapp/dashboard.html")


@login_required
def paginate_data(request, page_num, data_list):
    items_per_page, max_pages = 1, 10
    paginator = Paginator(data_list, items_per_page)
    last_page_number = paginator.num_pages

    try:
        data_list = paginator.page(page_num)
    except PageNotAnInteger:
        data_list = paginator.page(1)
    except EmptyPage:
        data_list = paginator.page(paginator.num_pages)

    current_page = data_list.number
    start_page = max(current_page - int(max_pages / 2), 1)
    end_page = start_page + max_pages

    if end_page > last_page_number:
        end_page = last_page_number + 1
        start_page = max(end_page - max_pages, 1)

    paginator_list = range(start_page, end_page)

    return data_list, paginator_list, last_page_number


@login_required
def setting_dashboard(request):
    
    get_setting_menu = MenuList.objects.filter(module_name='setting', is_active=True)
    
    context = {
        "get_setting_menu": get_setting_menu,
    }
    return render(request, 'ecomapp/setting_dashboard.html',context)





@login_required 
def product_main_category_list_view(request):
    
    
    if not checkUserPermission(request, "can_view", "backend/product-main-category-list"):
        return render(request,"403.html")

    product_main_categories = ProductMainCategory.objects.filter(is_active=True).order_by('-id')
    page_number = request.GET.get('page', 1)
    product_main_categories, paginator_list, last_page_number = paginate_data(request, page_number, product_main_categories)

    context = {
        'paginator_list': paginator_list,
        'last_page_number': last_page_number,
        'first_page_number': 1,  # Add first page number
        'products': product_main_categories,  # Changed to match template variable
        'product_main_categories': product_main_categories,  # Keep both for compatibility
    }

    return render(request, "product/product_main_category_list.html", context)  



@login_required
def add_product_main_category(request):
    if not checkUserPermission(request, "can_add", "backend/add-product-main-category"):
        return render(request, "403.html")

    if request.method == "POST":
        main_cat_name = request.POST.get('main_cat_name')
        cat_slug = request.POST.get('cat_slug')
        cat_ordering = request.POST.get('cat_ordering')
        description = request.POST.get('description')
        
        product_main_category = ProductMainCategory(
            main_cat_name=main_cat_name,
            cat_slug=cat_slug,
            cat_ordering=cat_ordering,
            description=description,
            created_by=request.user,
        )
        product_main_category.save()
        messages.success(request, "Product Main Category added successfully.")
        return redirect('product_main_category_list')
        

    return render(request, "product/add_product_main_category.html")


@login_required
def product_main_category_detailed(request, pk):
    if not checkUserPermission(request, "can_view", "backend/product-main-category-detailed"):
        return render(request, "403.html")
    
    try:
        product_main_category = ProductMainCategory.objects.get(pk=pk)
    except ProductMainCategory.DoesNotExist:
        messages.error(request, "Product category not found.")
        return redirect('product_main_category_list')
    
    context = {
        'product_main_category': product_main_category,
    }
    return render(request, "product/product_detail.html", context)

@login_required
def product_main_category_edit(request, pk):
    if not checkUserPermission(request, "can_update", "backend/product-main-category-edit"):
        return render(request, "403.html")
    product_main_category = ProductMainCategory.objects.get(pk=pk)
    if request.method == "POST":
        product_main_category.main_cat_name = request.POST.get('main_cat_name')
        product_main_category.cat_slug = request.POST.get('cat_slug')
        product_main_category.cat_ordering = request.POST.get('cat_ordering')
        product_main_category.description = request.POST.get('description')
        product_main_category.updated_by = request.user
        product_main_category.save()
        messages.success(request, "Product Main Category updated successfully.")
        return redirect('product_main_category_list')
    context = {
        'product_main_category': product_main_category,
    }
    return render(request, "product/product_edit.html", context)

@login_required
def product_main_category_delete(request, pk):
    if not checkUserPermission(request, "can_delete", "backend/product-main-category-delete"):
        return render(request, "403.html")
    product_main_category = ProductMainCategory.objects.get(pk=pk)  
    if request.method == "POST":
        product_main_category.is_active = False
        product_main_category.deleted = True
        product_main_category.deleted_by = request.user
        product_main_category.save()
        messages.success(request, "Product Main Category deleted successfully.")
        return redirect('product_main_category_list')
    context = {
        'product_main_category': product_main_category
    }
    return render(request, "product/delete_product.html", context)


@login_required
def product_list(request):
    if not checkUserPermission(request, "can_view", "backend/product-list"):
        return render(request, "403.html")
    # Logic for product list view
    return render(request, "product/product_list.html")



