from django.db import models

# Create your models here.
class AppointmentRequest(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    parent_name = models.CharField(max_length=250, blank=False, default='')
    pacient_name = models.CharField(max_length=250, blank=False, default='')
    therapy_field = models.CharField(max_length=250, blank=False, default='')
    email = models.EmailField(max_length=254, blank=False)
    phone_number = models.CharField(max_length=250, blank=False, default='')
    pacient_age = models.IntegerField(blank=False)
    time_preference = models.CharField(max_length=2, blank=False, default='')

    class Meta:
        ordering = ('created',)