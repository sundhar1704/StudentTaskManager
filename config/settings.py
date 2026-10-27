import os
from pathlib import Path
 
import dj_database_url
 
 
# --------------------------------------------------
# 1. BASE DIRECTORY
# --------------------------------------------------
 
BASE_DIR = Path(__file__).resolve().parent.parent
 
 
# --------------------------------------------------
# 2. SECURITY SETTINGS
# --------------------------------------------------
 
# Local development fallback only.
# Set SECRET_KEY securely in Render environment variables.
SECRET_KEY = os.environ.get(
    "SECRET_KEY",
    "django-insecure-local-development-only-key",
)
 
DEBUG = os.environ.get("DEBUG", "True").lower() == "true"
 
ALLOWED_HOSTS = [
    host.strip()
    for host in os.environ.get(
        "ALLOWED_HOSTS",
        "localhost,127.0.0.1",
    ).split(",")
    if host.strip()
]
 
 
# --------------------------------------------------
# 3. INSTALLED APPLICATIONS
# --------------------------------------------------
 
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
 
    # Third-party applications
    "rest_framework",
    "corsheaders",
 
    # Local applications
    "tasks",
]
 
 
# --------------------------------------------------
# 4. MIDDLEWARE
# --------------------------------------------------
 
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
 
    # CORS middleware should be near the top.
    "corsheaders.middleware.CorsMiddleware",
 
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]
 
 
# --------------------------------------------------
# 5. URL CONFIGURATION
# --------------------------------------------------
 
ROOT_URLCONF = "config.urls"
 
 
# --------------------------------------------------
# 6. TEMPLATES
# --------------------------------------------------
 
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]
 
 
# --------------------------------------------------
# 7. WSGI APPLICATION
# --------------------------------------------------
 
WSGI_APPLICATION = "config.wsgi.application"
 
 
# --------------------------------------------------
# 8. DATABASE CONFIGURATION
# --------------------------------------------------
 
# Use PostgreSQL when DATABASE_URL is configured.
# Otherwise, use SQLite for local development.
 
DATABASE_URL = os.environ.get("DATABASE_URL")
 
if DATABASE_URL:
    DATABASES = {
        "default": dj_database_url.parse(
            DATABASE_URL,
            conn_max_age=600,
            ssl_require=True,
        )
    }
else:
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": BASE_DIR / "db.sqlite3",
        }
    }
 
 
# --------------------------------------------------
# 9. PASSWORD VALIDATION
# --------------------------------------------------
 
AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": (
            "django.contrib.auth.password_validation."
            "UserAttributeSimilarityValidator"
        ),
    },
    {
        "NAME": (
            "django.contrib.auth.password_validation."
            "MinimumLengthValidator"
        ),
    },
    {
        "NAME": (
            "django.contrib.auth.password_validation."
            "CommonPasswordValidator"
        ),
    },
    {
        "NAME": (
            "django.contrib.auth.password_validation."
            "NumericPasswordValidator"
        ),
    },
]
 
 
# --------------------------------------------------
# 10. INTERNATIONALIZATION
# --------------------------------------------------
 
LANGUAGE_CODE = "en-us"
 
TIME_ZONE = "Asia/Kolkata"
 
USE_I18N = True
 
USE_TZ = True
 
 
# --------------------------------------------------
# 11. STATIC FILES
# --------------------------------------------------
 
STATIC_URL = "static/"
 
STATIC_ROOT = BASE_DIR / "staticfiles"
 
STORAGES = {
    "default": {
        "BACKEND": (
            "django.core.files.storage.FileSystemStorage"
        ),
    },
    "staticfiles": {
        "BACKEND": (
            "whitenoise.storage.CompressedManifestStaticFilesStorage"
        ),
    },
}
 
 
# --------------------------------------------------
# 12. DEFAULT PRIMARY KEY
# --------------------------------------------------
 
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
 
 
# --------------------------------------------------
# 13. DJANGO REST FRAMEWORK
# --------------------------------------------------
 
REST_FRAMEWORK = {
    "DEFAULT_PERMISSION_CLASSES": [
        "rest_framework.permissions.AllowAny",
    ],
}
 
 
# --------------------------------------------------
# 14. CORS CONFIGURATION
# --------------------------------------------------
 
# Local React development server by default.
# On Render, set CORS_ALLOWED_ORIGINS to your deployed
# Vercel frontend origin.
 
CORS_ALLOWED_ORIGINS = [
    origin.strip()
    for origin in os.environ.get(
        "CORS_ALLOWED_ORIGINS",
        "http://localhost:5173",
    ).split(",")
    if origin.strip()
]
 
 
# --------------------------------------------------
# 15. CSRF CONFIGURATION
# --------------------------------------------------
 
# Add deployed frontend origins here if you later use
# Django session authentication or CSRF-protected forms.
CSRF_TRUSTED_ORIGINS = [
    origin.strip()
    for origin in os.environ.get(
        "CSRF_TRUSTED_ORIGINS",
        "",
    ).split(",")
    if origin.strip()
]
 
 
# --------------------------------------------------
# 16. PROXY / HTTPS CONFIGURATION
# --------------------------------------------------
 
# Render terminates HTTPS at its proxy.
SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")
 
if not DEBUG:
    SECURE_SSL_REDIRECT = True
    SESSION_COOKIE_SECURE = True
    CSRF_COOKIE_SECURE = True

 