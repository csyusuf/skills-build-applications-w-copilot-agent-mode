DATABASES = {
    'default': {
        'ENGINE': 'djongo',
        'NAME': 'octofit_db',
        'CLIENT': {
            'host': 'mongodb://localhost:27017/',
        }
    }
}

# Enable CORS
INSTALLED_APPS = [
    # Default installed apps
]

INSTALLED_APPS += [
    'corsheaders',
]

MIDDLEWARE = [
    # Default middleware entries
]

MIDDLEWARE.insert(0, 'corsheaders.middleware.CorsMiddleware')

CORS_ALLOW_ALL_ORIGINS = True
CORS_ALLOW_METHODS = [
    'GET',
    'POST',
    'PUT',
    'PATCH',
    'DELETE',
    'OPTIONS',
]
CORS_ALLOW_HEADERS = [
    'content-type',
    'authorization',
    'x-csrftoken',
    'x-requested-with',
]

ALLOWED_HOSTS = ['*']