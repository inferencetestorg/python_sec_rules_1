DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'sqlite.db',
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    }
}

PASSWORD_HASHERS = [
        "django.contrib.auth.hashers.MD5PasswordHasher", # non-compliant
        "django.contrib.auth.hashers.PBKDF2PasswordHasher",
        'django.contrib.auth.hashers.BCryptSHA256PasswordHasher',
        'django.contrib.auth.hashers.Argon2PasswordHasher'
    ]
