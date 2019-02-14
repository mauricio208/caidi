from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from serializers import AppointmentRequestSerializer

@api_view(['POST'])
def appointment_register(request):
    """
    Register appoinment and sent email
    """
    print(request.data.__dict__)
    data = JSONParser().parse(request)
    serializer = AppointmentRequestSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)