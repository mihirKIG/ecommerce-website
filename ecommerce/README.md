# Django Ecommerce Project

A comprehensive Django-based ecommerce application with product management system, admin panel integration, and responsive frontend.

## 🚀 Features

- **Product Management System**
  - Product Main Categories
  - Product Sub Categories
  - CRUD operations for all products
  - Admin panel integration

- **User Authentication & Authorization**
  - Django built-in authentication
  - Permission-based access control
  - User role management

- **Responsive Frontend**
  - Bootstrap-based UI
  - Mobile-friendly design
  - Modern card layouts
  - Pagination support

- **Admin Dashboard**
  - Comprehensive admin interface
  - Data management through Django admin
  - Custom admin configurations

## 🛠️ Technology Stack

- **Backend**: Django 5.0
- **Database**: SQLite (default), MySQL support
- **Frontend**: HTML5, CSS3, Bootstrap 5
- **JavaScript**: jQuery, Custom JS
- **Python**: 3.13+

## 📋 Prerequisites

- Python 3.13 or higher
- pip (Python package installer)
- Git

## 🔧 Installation & Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/mihirKIG/ecommerce.git
   cd ecommerce
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   ```

3. **Activate virtual environment**
   - On Windows:
     ```bash
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

4. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

5. **Run database migrations**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

6. **Create a superuser**
   ```bash
   python manage.py createsuperuser
   ```

7. **Collect static files**
   ```bash
   python manage.py collectstatic
   ```

8. **Run the development server**
   ```bash
   python manage.py runserver
   ```

9. **Access the application**
   - Frontend: http://127.0.0.1:8000/
   - Admin Panel: http://127.0.0.1:8000/admin/

## 📁 Project Structure

```
ecommerce/
├── ecomapp/
│   ├── migrations/
│   ├── templates/
│   │   ├── ecomapp/
│   │   └── product/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── urls.py
│   ├── views.py
│   └── common_func.py
├── ecommerce/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── static/
│   ├── css/
│   ├── js/
│   ├── images/
│   └── fonts/
├── templates/
├── fixtures/
├── requirements.txt
├── manage.py
└── README.md
```

## 📊 Database Models

### ProductMainCategory
- `main_cat_name`: Category name
- `cat_slug`: URL-friendly slug
- `cat_ordering`: Display order
- `description`: Category description
- `is_active`: Status flag
- `created_by`: User who created
- `created_at`: Creation timestamp

### ProductSubCategory
- `sub_cat_name`: Subcategory name
- `main_category`: Foreign key to ProductMainCategory
- `sub_cat_slug`: URL-friendly slug
- `description`: Subcategory description
- `is_active`: Status flag

## 🎯 Key Features Implemented

1. **Product Category Management**
   - List all categories with pagination
   - Add new categories
   - Edit existing categories
   - Soft delete functionality
   - View detailed category information

2. **Permission System**
   - Role-based access control
   - Permission checking for all operations
   - Secure view decorators

3. **Responsive Design**
   - Mobile-first approach
   - Bootstrap components
   - Custom CSS styling
   - FontAwesome icons

4. **Admin Integration**
   - Custom admin interface
   - Bulk operations
   - Search and filter capabilities

## 🔗 URL Patterns

- `/` - Home page
- `/dashboard/` - Main dashboard
- `/setting-dashboard/` - Settings dashboard
- `/product-main-category-list/` - Product categories list
- `/add-product-main-category/` - Add new category
- `/product-main-category-detailed/<id>/` - Category details
- `/product-main-category-edit/<id>/` - Edit category
- `/product-main-category-delete/<id>/` - Delete category

## 🚀 Deployment

For production deployment:

1. Set `DEBUG = False` in settings.py
2. Configure your production database
3. Set up proper static files serving
4. Configure environment variables
5. Use a production WSGI server like Gunicorn

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is open source and available under the [MIT License](LICENSE).

## 👨‍💻 Developer

**Mihir Kanti Roy**
- GitHub: [@mihirKIG](https://github.com/mihirKIG)

## 🆘 Support

If you have any questions or need help with setup, please create an issue in the GitHub repository.

---

⭐ **Star this repository if you find it helpful!**
