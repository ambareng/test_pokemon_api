from rest_framework.serializers import ValidationError


MAX_LEVEL = 100
MIN_LEVEL = 1


def level_validator(value):
    if value > MAX_LEVEL:
        raise ValidationError(f'{MAX_LEVEL} is the max limit for a pokemon\'s level.')
    if value < MIN_LEVEL:
        raise ValidationError(f'{MIN_LEVEL} is the minimum limit for a pokemon\'s level.')
    return value
