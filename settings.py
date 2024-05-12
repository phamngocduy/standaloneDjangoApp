# PostgreSQL
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'postgres',
        'USER': 'postgres',
        'PASSWORD': 'MjIyNTQtcGhtbmdj',
        'HOST': 'localhost',
        'PORT': '5432'
    }
}

INSTALLED_APPS = (
    'database',
)

SECRET_KEY = 'phmngcduy'
