import datetime
from rest_framework.exceptions import ValidationError


def year_validator(value):
    if value < 1900 or value > datetime.datetime.now().year:
        raise ValidationError(
            f'{value} is not a correcrt year!',
            params={'value': value},
        )
