from django.db import models

# Create your models here.
class AppointmentRequest(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    parent_name = models.CharField(max_length=250, blank=True, default='')
    pacient_name = models.CharField(max_length=250, blank=True, default='')
    therapy_field = models.CharField(max_length=250, blank=True, default='')

    class Meta:
        ordering = ('created',)