from django.db import models
from .validate import validate_name, validate_zip_code, validate_phone, validate_type
from django.core.validators import validate_email

# Create your models here.
class Hospital(models.Model):
    name     = models.CharField(primary_key=True, null=False, blank=False, max_length=100, validators=[validate_name])
    zip_code = models.CharField(null=False, blank=False, max_length=10, validators=[validate_zip_code])
    phone    = models.CharField(null=False, blank=False, max_length=12, validators=[validate_phone])
    type     = models.CharField(max_length=9, validators=[validate_type])
    email    = models.CharField(null=False, blank=False, max_length=50, validators=[validate_email])
    visible  = models.BooleanField(default=True)
    def __str__(self):
        return f'{self.name}:{self.zip_code}:{self.phone}:{self.type}:{self.email}:{self.visible}'

class MyEmail(models.Model):
    password = models.CharField(null=False, blank=False, max_length=50)
    receiver = models.CharField(null=False, blank=False, max_length=254, validators=[validate_email])
    subject  = models.CharField(null=False, blank=False, max_length=50)
    message  = models.CharField(null=False, blank=False, max_length=2000)
    def __str__(self):
        return f'{self.password}:{self.receiver}:{self.subject}:{self.message}'