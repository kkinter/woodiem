import uuid

from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from django.db import models
from django.utils import timezone


class CustomUserManager(BaseUserManager):
    def email_validator(self, email):
        try:
            validate_email(email)
            return True
        except ValidationError:
            raise ValueError("유효한 이메일을 입력해야합니다.")

    def create_user(self, email, password, first_name, last_name, **extra_fields):
        if not first_name:
            raise ValueError("User는 이름이 있어야 합니다.")
        if not last_name:
            raise ValueError("User는 성이 있어야 합니다.")
        if email:
            email = self.normalize_email(email)
            self.email_validator(email)
        else:
            raise ValueError("User는 이메일이 있어야 합니다.")

        user = self.model(
            email=email, first_name=first_name, last_name=last_name, **extra_fields
        )
        user.set_password(password)

        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)

        user.save(using=self._db)
        return user

    def create_superuser(self, email, password, first_name, last_name, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("")

        if extra_fields.get("is_superuser") is not True:
            raise ValueError("")

        if extra_fields.get("is_active") is not True:
            raise ValueError("")

        if not password:
            raise ValueError("")

        if email:
            email = self.normalize_email(email)
            self.email_validator(email)
        else:
            raise ValueError("")

        user = self.create_user(
            email=email,
            password=password,
            first_name=first_name,
            last_name=last_name,
            **extra_fields,
        )
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    pkid = models.BigAutoField(primary_key=True, editable=False)
    id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    first_name = models.CharField(max_length=10)
    last_name = models.CharField(max_length=10)
    email = models.EmailField(db_index=True, unique=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    date_joined = models.DateTimeField(default=timezone.now)

    objects = CustomUserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["first_name", "last_name"]

    def __str__(self) -> str:
        return f"{self.last_name} {self.first_name}"
