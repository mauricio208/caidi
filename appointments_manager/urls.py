from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from appointments_manager.views import appointment_register

urlpatterns = [
    path('appointment_register/', appointment_register),
]

urlpatterns = format_suffix_patterns(urlpatterns)