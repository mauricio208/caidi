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
    import pudb; pudb.set_trace()
    serializer = AppointmentRequestSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        # send_mail(
        # '[CAIDI] CITA {}'.format(data['']),
        # '{}\n{}\n{}'.format(data['']),
        # None,
        # ['mauricio208@gmail.com'],
        # fail_silently=False,
        # )
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)