from django.core import exceptions

from SoftUniProjectMuscleArmy.core.utils import megabytes_to_bytes


def validate_file_less_than_5mb(image):
    filesize = image.file.size
    megabyte_limit = 5.0
    if filesize > megabytes_to_bytes(megabyte_limit):
        raise exceptions.ValidationError(f'Max file size is {megabyte_limit}MB')


def validate_only_letters(value):
    for ch in value:
        if not ch.isalpha():
            raise exceptions.ValidationError('Only letters are allowed')