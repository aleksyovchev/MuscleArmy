from enum import Enum

from django.core import validators
from django.db import models
from django.contrib.auth import models as auth_models

from SoftUniProjectMuscleArmy.core.validators import validate_only_letters, validate_file_less_than_5mb


class ChoicesEnumMixin:
    @classmethod
    def choices(cls):
        return [(x.name, x.value) for x in cls]

    @classmethod
    def max_len(cls):
        return max(len(name) for name, _ in cls.choices())


class Gender(ChoicesEnumMixin, Enum):
    male = 'Male'
    female = 'Female'
    DoNotShow = 'Do not show'


class AppUser(auth_models.AbstractUser):
    MIN_LEN_FIRST_LAST_NAME = 2
    MAX_LEN_FIRST_LAST_NAME = 30

    first_name = models.CharField(
        max_length=MAX_LEN_FIRST_LAST_NAME,
        validators=(
            validators.MinLengthValidator(MIN_LEN_FIRST_LAST_NAME),
            validate_only_letters,
        ),
        null=True,
        blank=True,
    )

    last_name = models.CharField(
        max_length=MAX_LEN_FIRST_LAST_NAME,
        validators=(
            validators.MinLengthValidator(MIN_LEN_FIRST_LAST_NAME),
            validate_only_letters,
        ),
        null=True,
        blank=True,
    )

    email = models.EmailField(
        unique=True,
    )

    gender = models.CharField(
        choices=Gender.choices(),
        max_length=Gender.max_len(),
        null=True,
        blank=True,
    )

    profile_picture = models.ImageField(
        upload_to='mediafiles/profile_pictures/',
        null=True,
        blank=True,
        validators=(validate_file_less_than_5mb,)
    )

