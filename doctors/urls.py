
from django.urls import path


# from doctors.views import ListDoctorsView, DetailDoctorView, ListDepartmentView, DetailDepartmentView, ListDoctorAvailabilityView, DetailDoctorAvailabilityView, ListMedicalNoteView, DetailMedicalNoteView

from rest_framework.routers import DefaultRouter
from .viewsets import DoctorViewSet, DepartmentViewSet, DoctorAvailabilityViewSet, MedicalNoteViewSet

router = DefaultRouter()
router.register('doctors', DoctorViewSet)
router.register('departments', DepartmentViewSet)
router.register('doctoravailabilities', DoctorAvailabilityViewSet)
router.register('medicalnotes', MedicalNoteViewSet)

urlpatterns= router.urls


# urlpatterns = [
#     #path('doctors/', ListDoctorsView.as_view()), 
#     #path('doctors/', DetailDoctorView.as_view()), 
#     #path('departments/', ListDepartmentView.as_view()),
#     #path('departments/<int:id>/', DetailDepartmentView.as_view()),
#     path('doctoravailabilities/', ListDoctorAvailabilityView.as_view()),
#     path('doctoravailabilities/<int:id>/', DetailDoctorAvailabilityView.as_view()),
#     path('medicalnotes/', ListMedicalNoteView.as_view()),
#     path('medicalnotes/<int:id>/', DetailMedicalNoteView.as_view()),

# ] 