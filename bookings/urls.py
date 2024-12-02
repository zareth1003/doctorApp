from django.urls import path

# from .views import (
#     ListAppointmentsView,
#     DetailAppointmentView,
#     ListMedicalNoteView,
#     DetailMedicalNoteView,
# )

from rest_framework.routers import DefaultRouter
from .viewsets import AppointmentViewSet, MedicalNoteViewSet

router = DefaultRouter()
router.register('appointments', AppointmentViewSet)
router.register('medicalnotes', MedicalNoteViewSet)

urlpatterns = router.urls


# urlpatterns = [
#     path('appointments/', ListAppointmentsView.as_view()),
#     path('appointments/<int:id>/', DetailAppointmentView.as_view()),
#     path('medicalnotes/', ListMedicalNoteView.as_view()),
#     path('medicalnotes/<int:id>/', DetailMedicalNoteView.as_view()),
# ]