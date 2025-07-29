from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
import re

def validate_name(value):
    """Validates the name by checking if it is alphabetic."""
    if not re.match(r"^[a-zA-Z0-9_,.'\-() ]+$", value):
        raise ValidationError(
            _("%(value)s is not a valid name!"),
            params={"value": value},
        )

def validate_zip_code(value):
    """Validates the zip code by comparing it to Canadian and American standards."""
    if re.match(r'^[ABCEGHJ-NPRSTVXY]\d[ABCEGHJ-NPRSTV-Z][ -]?\d[ABCEGHJ-NPRSTV-Z]\d$', value, re.IGNORECASE): # Canadian Postal Code
        pass
    elif re.match(r'^[0-9]{5}(?:[ -]?[0-9]{4})?$', value): # American Zip Code
        pass
    else:
        raise ValidationError(
            _("%(value)s is not a valid zip code!"),
            params={"value": value},
        )

def validate_phone(value):
    """Validates the phone number by comparing it to Canadian and American standards."""
    if not re.match(r'^[0-9]{3}-[0-9]{3}-[0-9]{4}$', value):
        raise ValidationError(
            _("%(value)s is not a valid phone number!"),
            params={"value": value},
        )

def validate_type(value):
    valid_types = ['Public', 'Private', 'Nonprofit']
    hospital_type = value[0].upper() + value[1:].lower()
    if hospital_type not in valid_types:
        raise ValidationError(
            _("%(value)s is not a valid hospital type!"),
            params={"value": value},
        )