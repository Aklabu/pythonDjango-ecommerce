# Django E-Commerce Website

This is a minimal e-commerce website built with Django. It features:
- Category and Product models
- Admin dashboard for managing products and categories
- Media file support for product images
- Bootstrap-styled templates
- Dynamic navbar with category dropdown
- Views for home, all products, and category-wise products
- Custom context processor for categories

## Setup
1. Create and activate a virtual environment
2. Install dependencies: `pip install -r requirements.txt` (or install Django and Pillow manually)
3. Run migrations: `python manage.py migrate`
4. Create a superuser: `python manage.py createsuperuser`
5. Run the server: `python manage.py runserver`
6. Visit `/admin` to add categories and products

## Development
- Media files are served in development mode
- Templates use Bootstrap for styling
- Phone number for order confirmation is shown under each product

## Notes
- Replace the phone number in templates as needed
- For production, configure static/media file serving and security settings
"# pythonDjango-ecommerce" 
