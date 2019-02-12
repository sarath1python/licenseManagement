from django.db import models
from django.contrib.auth.models import User


class License(models.Model):
    LICENCE_CHOICES = (
        (1, 'Active'),
        (0, 'Inactive')
    )
    serial_number = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    number = models.CharField(max_length=255)
    status = models.CharField(max_length=8, choices=LICENCE_CHOICES, default=1)
    shop_details = models.CharField(max_length=255)
    address = models.CharField(max_length=400)
    village = models.CharField(max_length=255)
    taluk = models.CharField(max_length=255)
    details = models.TextField(help_text="Details of sound agency/institution", blank=True, null=True)
    mobile_number = models.CharField(max_length=12)
    issued_date = models.DateField(auto_now=True)

    is_deleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    updated_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return '{}({})'.format(self.name, self.serial_number)


class Violation(models.Model):
    details = models.TextField()
    date = models.DateTimeField()
    license = models.ForeignKey(License, related_name='violations', on_delete=models.CASCADE)

    is_deleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    updated_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return '{}({})'.format(self.license.name, self.license.serial_number)




