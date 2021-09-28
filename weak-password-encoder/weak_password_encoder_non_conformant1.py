PASSWORD_HASHERS = [
        "django.contrib.auth.hashers.MD5PasswordHasher", # non-compliant
        "django.contrib.auth.hashers.PBKDF2PasswordHasher"
    ]