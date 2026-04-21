# Sample Django App

A simple blog application built with Django, featuring post creation, editing, deletion, and viewing capabilities.

## Features

- Create, read, update, and delete posts (CRUD operations)
- Admin interface for managing posts
- Responsive and modern UI design
- Built-in pagination support
- Timestamp tracking (created and updated dates)
- Unit tests for the Post model

## Project Structure

```
.
├── manage.py              # Django management script
├── requirements.txt       # Python dependencies
├── README.md             # This file
├── myproject/            # Main Django project
│   ├── settings.py      # Project settings
│   ├── urls.py          # Main URL configuration
│   ├── wsgi.py          # WSGI configuration
│   └── asgi.py          # ASGI configuration
├── myapp/               # Sample Django app
│   ├── models.py        # Database models
│   ├── views.py         # View logic
│   ├── urls.py          # App URL patterns
│   ├── admin.py         # Admin interface configuration
│   ├── tests.py         # Unit tests
│   └── migrations/      # Database migrations
└── templates/           # HTML templates
    └── myapp/
        ├── index.html              # Home page
        ├── post_list.html          # Posts list view
        ├── post_detail.html        # Single post view
        ├── post_form.html          # Create/edit post form
        └── post_confirm_delete.html # Delete confirmation
```

## Installation & Setup

### 1. Create and Activate Virtual Environment

```bash
cd /Volumes/Universe/Personal/Apps/checkcolify
python3 -m venv venv
source venv/bin/activate
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Apply Migrations

```bash
python manage.py migrate
```

### 4. Create Superuser (for admin access)

```bash
python manage.py createsuperuser
```

### 5. Run Development Server

```bash
python manage.py runserver
```

## Access the Application

- **Home Page**: http://localhost:8000/
- **Posts List**: http://localhost:8000/posts/
- **Admin Panel**: http://localhost:8000/admin/

## Available URLs

| URL | View | Function |
|-----|------|----------|
| `/` | Home | List recent posts |
| `/posts/` | Post List | View all posts (paginated) |
| `/posts/<id>/` | Post Detail | View single post |
| `/posts/new/` | Post Create | Create new post |
| `/posts/<id>/edit/` | Post Update | Edit existing post |
| `/posts/<id>/delete/` | Post Delete | Delete post (with confirmation) |
| `/admin/` | Django Admin | Admin interface |

## Running Tests

```bash
python manage.py test
```

## Making Database Migrations

When you modify the models, create new migrations:

```bash
python manage.py makemigrations myapp
python manage.py migrate
```

## Useful Management Commands

```bash
# Create a new superuser
python manage.py createsuperuser

# Interactive Python shell with Django context
python manage.py shell

# Check for issues in your project
python manage.py check

# Collect static files for production
python manage.py collectstatic

# Access database backend directly
python manage.py dbshell
```

## Customization

- Modify the `Post` model in `myapp/models.py` to add more fields
- Update templates in `templates/myapp/` to customize the UI
- Extend views in `myapp/views.py` to add more functionality
- Add new URL patterns in `myapp/urls.py`

## Production Deployment

Before deploying to production:

1. Set `DEBUG = False` in `settings.py`
2. Update `SECRET_KEY` with a secure value
3. Configure `ALLOWED_HOSTS` with your domain
4. Use a production database (PostgreSQL recommended)
5. Collect static files: `python manage.py collectstatic`
6. Use a production-grade web server (Gunicorn, Uvicorn)
7. Consider using environment variables for sensitive settings

## License

This is a sample application for learning purposes.
