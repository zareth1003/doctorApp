from rest_framework import serializers
from .models import Appointment, MedicalNote

class AppointmentSerializer(serializers.ModelSerializer):
  doctor_name = serializers.ReadOnlyField(source='doctor.full_name');
  patient_name = serializers.ReadOnlyField(source='patient.full_name');
  class Meta:
    model = Appointment
    fields = 'id', 'appointment_date', 'appointment_time', 'notes', 'status', 'doctor_name', 'patient_name'
class MedicalNoteSerializer(serializers.ModelSerializer):
  class Meta:
    model = MedicalNote
    fields = '__all__'