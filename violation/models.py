from django.db import models
from django.contrib.auth.models import User

LICENCE_CHOICES = (
    (1, 'Active'),
    (0, 'Inactive')
)


class Licensee(models.Model):
    serial_number = models.CharField(max_length=255)
    licensee_name = models.CharField(max_length=255)
    details = models.TextField(help_text="Details of sound agency/institution", blank=True, null=True)
    mobile_number = models.IntegerField()
    licence_number = models.CharField(max_length=255)
    licence_status = models.IntegerField(choices=LICENCE_CHOICES, default='active')
    issued_date = models.DateField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    updated_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return '{}({})'.format(self.licensee_name, self.serial_number)


class Violation(models.Model):
    details = models.TextField()
    licensee = models.ForeignKey(Licensee, related_name='violations', on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    updated_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return '{}({})'.format(self.licensee.licensee_name, self.licensee.serial_number)




