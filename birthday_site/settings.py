from pathlib import Path
import os
import tempfile
from dotenv import load_dotenv
import dj_database_url
import cloudinary

BASE_DIR = Path(__file__).resolve().parent.parent

load_dotenv(BASE_DIR / ".env")

SECRET_KEY = os.getenv("SECRET_KEY")
DEBUG = os.getenv("DEBUG", "False") == "True"

ALLOWED_HOSTS = [
    ".vercel.app",
    ".railway.app",
    "localhost",
    "127.0.0.1",
]

# ✅ Cloudinary (ONLY for media)
cloudinary.config(
    cloud_name=os.getenv("CLOUDINARY_CLOUD_NAME"),
    api_key=os.getenv("CLOUDINARY_API_KEY"),
    api_secret=os.getenv("CLOUDINARY_API_SECRET"),
)

# ✅ Apps
INSTALLED_APPS = [
    "main",
    "cloudinary",
    "cloudinary_storage",

    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
]

# ✅ Middleware
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",  # important
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

# ✅ Templates
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
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

ROOT_URLCONF = "birthday_site.urls"

# ✅ Database
DATABASES = {
    "default": dj_database_url.parse(
        os.getenv("DATABASE_URL"),
        conn_max_age=600,
        ssl_require=True,
    )
}

# =========================
# ✅ STATIC FILES (WhiteNoise)
# =========================
STATIC_URL = "/static/"
STATIC_ROOT = BASE_DIR / "staticfiles"

# 👉 IMPORTANT: create this folder manually
STATICFILES_DIRS = [
    BASE_DIR / "static",
]

# WhiteNoise settings
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

# =========================
# ✅ MEDIA FILES (Cloudinary)
# =========================
DEFAULT_FILE_STORAGE = "cloudinary_storage.storage.MediaCloudinaryStorage"

# In serverless environments (e.g. Vercel / Lambda), the app code directory
# (often `/var/task`) is read-only. Django/Storages may still need a writable
# directory for temporary uploads.
TEMP_DIR = os.getenv("FILE_UPLOAD_TEMP_DIR") or tempfile.gettempdir()
Path(TEMP_DIR).mkdir(parents=True, exist_ok=True)

MEDIA_ROOT = os.getenv("MEDIA_ROOT", TEMP_DIR)
MEDIA_URL = os.getenv("MEDIA_URL", "/media/")
FILE_UPLOAD_TEMP_DIR = os.getenv("FILE_UPLOAD_TEMP_DIR", TEMP_DIR)

# =========================
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"