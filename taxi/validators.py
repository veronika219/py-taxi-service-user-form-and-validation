from django.core.exceptions import ValidationError


def validate_license_number(license_number):
    if len(license_number) != 8:
        raise ValidationError("License number must consist only 8 characters.")
    if not all(char.isalpha() and char.isupper() for char in license_number[:3]):
        raise ValidationError("First three characters must be uppercase letters.")
    if not license_number[3:].isdigit():
        raise ValidationError("Last 5 characters must be numeric.")
    return license_number
