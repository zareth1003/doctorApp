from .serializers import PatientSerializer, InsuranceSerializer, MedicalRecordSerializer
from .models  import Patient, Insurance, MedicalRecord

from rest_framework.decorators import api_view
from rest_framework.response import Response

from rest_framework import status
#usamos una vista basada en clase en ves de usar api-view, para importarla:
from rest_framework.views import APIView

from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveUpdateDestroyAPIView


# GET api/patients ... esta api en el modo GET va a LISTAR
# POST api/patients ... esta api en el modo POST va a CREAR
# GET api/patients/<pk> ... con esto se va a saber es el detalle -->DETALLE 
# PUT api/patients/<pk> ... con esto se va a realizar una modificacion -->Modificacion 
# DELETE api/patients/<pk> ... con esto se va a realizar ELIMINAR 

##VISTAS BASADAS EN Clases, no necsitas crear if, sino un nuevo metodo 

class ListPatientsView(ListAPIView, CreateAPIView): #esta es la nueva View
  allowed_methods = (['GET', 'POST'])
  serializer_class = PatientSerializer
  queryset = Patient.objects.all() #Pasamos el objeto que estamos utiliZANDO
  
class DetailPatientView(RetrieveUpdateDestroyAPIView):
    allowed_methods = ['GET', 'PUT', 'DELETE']
    serializer_class = PatientSerializer
    queryset = Patient.objects.all()
    
class ListInsuranceView(ListAPIView, CreateAPIView):
    allowed_methods = ['GET', 'POST']
    serializer_class = InsuranceSerializer
    queryset = Insurance.objects.all()


class DetailInsuranceView(RetrieveUpdateDestroyAPIView):
    allowed_methods = ['GET', 'PUT', 'DELETE']
    serializer_class = InsuranceSerializer
    queryset = Insurance.objects.all()


class ListMedicalRecordView(ListAPIView, CreateAPIView):
    allowed_methods = ['GET', 'POST']
    serializer_class = MedicalRecordSerializer
    queryset = MedicalRecord.objects.all()


class DetailMedicalRecordView(RetrieveUpdateDestroyAPIView):
    allowed_methods = ['GET', 'PUT', 'DELETE']
    serializer_class = MedicalRecordSerializer
    queryset = MedicalRecord.objects.all()
    

##VISTAS BASADAS EN FUNCIONES
# @api_view(['GET', 'POST'])
# def list_patients(request):
#   if request.method == 'GET':
#        patients = Patient.objects.all()
#        serializer = PatientSerializer(patients, many=True)
#        return Response(serializer.data)
     
#   if request.method == 'POST':
#        serializer = PatientSerializer(data=request.data) #aqui estamos diciendo que si la informacion que estamos pasando es valida, debe guardar
#        serializer.is_valid(raise_exception=True) #raise exception si la información no es correcta manda un formato json con el campo que tiene el error.
#        serializer.save() # debemos decir que nos returne algo si la informaci+on es correcta por eso usamos return e importamos status, podemos enviar por medio de una http code, que nos permite comunicar que el recurso fue creado.
#        return Response(status=status.HTTP_201_CREATED)



  # #obtenemos la lista
  # def get(self, request):   #se le pasa el self porque ya estamos creando vista basandonos en objetos.
  #   patients = Patient.objects.all()
  #   serializer = PatientSerializer(patients, many=True)
  #   return Response(serializer.data)
  
  # #creamos la lista con el post de tipo patients 
  # def post(self, request):
  #   serializer = PatientSerializer(data=request.data)
  #   serializer.is_valid(raise_exception=True)
  #   serializer.save()
  #   return Response(status=status.HTTP_201_CREATED)
    
    
# class DetailPatientView(APIView):
#   allowed_methods = (['GET', 'PUT', 'DELETE'])
  
#   def get(self, request, pk):
#      try:
#         patient = Patient.objects.get(id=pk)
#      except Patient.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)
#      serializer = PatientSerializer(patient)
#      return Response(serializer.data)
   
#   def put(self, request, pk):
#      try:
#         patient = Patient.objects.get(id=pk)
#      except Patient.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)
#      serializer = PatientSerializer(patient, data=request.data)
#      serializer.is_valid(raise_exception=True)
#      serializer.save()
#      return Response(serializer.data, status=status.HTTP_201_CREATED)
   
#   def delete(self, request, pk):
#      try:
#         patient = Patient.objects.get(id=pk)
#      except Patient.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)
#      patient.delete()
#      return Response(status=status.HTTP_204_NO_CONTENT)
    



# ##NUEVA VISTA QUE REALIZA LA MODIFICACION
# @api_view(['GET', 'PUT', 'DELETE'])
# def detail_patient(request, pk):
#   try:
#       patient = Patient.objects.get(id=pk)
#   except Patient.DoesNotExist:
#       return Response(status=status.HTTP_404_NOT_FOUND)
  
#   if request.method == 'GET':
#     serializer = PatientSerializer(patient)
#     return Response(serializer.data)
  
#   if request.method == 'PUT':
#     serializer = PatientSerializer(patient, data=request.data)
#     serializer.is_valid(raise_exception=True)
#     serializer.save()
#     return Response(serializer.data, status=status.HTTP_201_CREATED)
  
#   if request.method == 'DELETE':
#     patient.delete()
#     return Response(status=status.HTTP_204_NO_CONTENT)


