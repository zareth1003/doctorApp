from django.db import models

# Create your models here.
class Doctor (models.Model):
  first_name = models.CharField(max_length=100)
  last_name = models.CharField(max_length=100)
  qualification = models.CharField(max_length=100)
  contact_number = models.CharField(max_length=15)
  email = models.EmailField()
  address = models.TextField()
  biografy = models.TextField()
  is_on_vacation = models.BooleanField(default=False)
  
class Department (models.Model):  #Doctor tiene un departamento
  name = models.CharField(max_length=100)
  description = models.TextField()
  
class DoctorAvailability (models.Model):  #Dicponibilidad del Doctor
  doctor = models.ForeignKey(
    Doctor, related_name='availabilities', on_delete=models.CASCADE
    )
  start_date = models.DateTimeField()
  end_date = models.DateTimeField()
  start_time = models.TimeField()
  end_time = models.TimeField()
  
  
class MedicalNote (models.Model):  #Crear Notas
  doctor = models.ForeignKey(
    Doctor, related_name='medical_notes', on_delete=models.CASCADE
  )
  note = models.TextField()
  date = models.DateField()
  
