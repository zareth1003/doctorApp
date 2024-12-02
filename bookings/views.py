#importamos los serializadores 
from .serializers import AppointmentSerializer, MedicalNoteSerializer

#importamos los modelos:
from .models import Appointment, MedicalNote 

#importamos las vistas generic 
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveUpdateDestroyAPIView

class ListAppointmentsView(ListAPIView, CreateAPIView):
  """
  Obtiene la lista de citas medicas programadas
  """
  allowed_methods = (['GET', 'POST'])
  serializer_class = AppointmentSerializer
  queryset = Appointment.objects.all()
  
class DetailAppointmentView(RetrieveUpdateDestroyAPIView): 
  allowed_methods = (['GET', 'PUT', 'DELETE'])
  serializer_class = AppointmentSerializer
  queryset = Appointment.objects.all()
  
class ListMedicalNoteView(ListAPIView, CreateAPIView):
  allowed_methods = (['GET', 'POST'])
  serializer_class = MedicalNoteSerializer
  queryset = Appointment.objects.all()
  
class DetailMedicalNoteView(RetrieveUpdateDestroyAPIView):
  allowed_methods = ['GET', 'PUT', 'DELETE']
  serializer_class = MedicalNoteSerializer
  queryset = MedicalNote.objects.all()
