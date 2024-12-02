
from django.urls import path

# from patients.views import ListPatientsView, DetailPatientView, ListInsuranceView, DetailInsuranceView, ListMedicalRecordView, DetailMedicalRecordView
from rest_framework.routers import DefaultRouter
from .viewsets import PatientViewSet, InsuranceViewSet, MedicalRecordViewSet

router = DefaultRouter()
router.register('patients', PatientViewSet)
router.register('insurances', InsuranceViewSet)
router.register('medicalrecords', MedicalRecordViewSet)

urlpatterns = router.urls
 
 
# urlpatterns = [
   
#     path('patients/', ListPatientsView.as_view()), #se agrega as_view para poder obtener la vista
#     path('patients/<int:pk>/', DetailPatientView.as_view()),
#     path('insurances/', ListInsuranceView.as_view()),
#     path('insurances/<int:pk>/', DetailInsuranceView.as_view()),
#     path('medicalrecords/', ListMedicalRecordView.as_view()),
#     path('medicalrecords/<int:pk>/', DetailMedicalRecordView.as_view()),
# ]
