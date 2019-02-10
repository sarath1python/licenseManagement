from django.db import models
from django.contrib.auth.models import User

LICENCE_CHOICES = (
    (1, 'Active'),
    (0, 'Inactive')
)


class License(models.Model):
    serial_number = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    number = models.CharField(max_length=255)
    status = models.IntegerField(choices=LICENCE_CHOICES, default='active')
    location = models.CharField(max_length=400)
    details = models.TextField(help_text="Details of sound agency/institution", blank=True, null=True)
    mobile_number = models.IntegerField()
    issued_date = models.DateField()

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




