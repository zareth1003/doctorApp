# Create your views here.
from .serializers import DoctorSerializer, DepartmentSerializer, DoctorAvailabilitySerializer, MedicalNoteSerializer

from .models import Doctor, Department, DoctorAvailability, MedicalNote



# from rest_framework.decorators import api_view
# from rest_framework.response import Response

# from rest_framework import status

from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveUpdateDestroyAPIView


class ListDoctorsView (ListAPIView, CreateAPIView):
  allowed_methods =(['GET', 'POST'])
  serializer_class=DoctorSerializer
  queryset = Doctor.objects.all()

class DetailDoctorView(RetrieveUpdateDestroyAPIView):
  allowed_methods =(['GET', 'PUT', 'DELETE'])
  serializer_class=DoctorSerializer
  queryset = Doctor.objects.all()
  
class ListDepartmentView(ListAPIView, CreateAPIView):
    allowed_methods = ['GET', 'POST']
    serializer_class = DepartmentSerializer
    queryset = Department.objects.all()


class DetailDepartmentView(RetrieveUpdateDestroyAPIView):
    allowed_methods = ['GET', 'PUT', 'DELETE']
    serializer_class = DepartmentSerializer
    queryset = Department.objects.all()


class ListDoctorAvailabilityView(ListAPIView, CreateAPIView):
    allowed_methods = ['GET', 'POST']
    serializer_class = DoctorAvailabilitySerializer
    queryset = DoctorAvailability.objects.all()


class DetailDoctorAvailabilityView(RetrieveUpdateDestroyAPIView):
    allowed_methods = ['GET', 'PUT', 'DELETE']
    serializer_class = DoctorAvailabilitySerializer
    queryset = DoctorAvailability.objects.all()


class ListMedicalNoteView(ListAPIView, CreateAPIView):
    allowed_methods = ['GET', 'POST']
    serializer_class = MedicalNoteSerializer
    queryset = MedicalNote.objects.all()


class DetailMedicalNoteView(RetrieveUpdateDestroyAPIView):
    allowed_methods = ['GET', 'PUT', 'DELETE']
    serializer_class = MedicalNoteSerializer
    queryset = MedicalNote.objects.all()
  





# @api_view(['GET', 'POST'])
# def list_doctor(request):
#   if request.method == 'GET':
#     doctors = Doctor.objects.all()
#     serializer = DoctorSerializer(doctors, many=True)
#     return Response(serializer.data)
  
#   if request.method == 'POST':
#     serializer = DoctorSerializer(data=request.data)
#     serializer.is_valid(raise_exception=True)
#     serializer.save()
#     return Response(status=status.HTTP_201_CREATED)
  
  
#   #NUEVA VISTA CON DETALLES DE DOCTORS
# @api_view(['GET', 'PUT', 'DELETE'])
# def detail_doctor(request, pk):
#     try:
#       doctor = Doctor.objects.get(id=pk)
#     except Doctor.DoesNotExist:
#       return Response(status=status.HTTP_404_NOT_FOUND)
    
#     if request.method == 'GET':
#       serializer = DoctorSerializer(doctor)
#       return Response(serializer.data)
    
#     if request.method == 'PUT':
#       serializer = DoctorSerializer(doctor, data=request.data)
#       serializer.is_valid(raise_exception=True)
#       serializer.save()
#       return Response(serializer.data, status=status.HTTP_201_CREATED)
    
#     if request.method == 'DELETE':
#       doctor.delete()
#       return Response(status=status.HTTP_204_NO_CONTENT)
    
  
