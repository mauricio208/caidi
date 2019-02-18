from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from appointments_manager.serializers import AppointmentRequestSerializer
from django.core.mail import send_mail


@api_view(['POST'])
@permission_classes((AllowAny, ))
def appointment_register(request):
    """
    Register appoinment and sent email
    """
    serializer = AppointmentRequestSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        email_body = (f"Nombre completo del representante : {request.data['parent_name']}\n"
        f"Nombre del representado : {request.data['pacient_name']}\n"              
        f"E-mail de contacto : {request.data['email']}\n"              
        f"Número telefonico de contacto : {request.data['phone_number']}\n"       
        f"Edad del representado : {request.data['pacient_age']}\n"             
        f"Especialidad por la que solicita la cita : {request.data['therapy_field']}\n"
        f"Turno de preferencia : {request.data['time_preference']}\n")
        send_mail(
        '[CAIDI] CITA {}'.format(request.data['therapy_field']),       
        email_body,
        None,
        # ['terapiascaidi@gmail.com','mauricio208@gmail.com'],
        ['mauricio208@gmail.com'],
        fail_silently=False,
        )
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)