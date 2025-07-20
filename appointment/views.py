from django.shortcuts import render
from rest_framework import viewsets

from . import models
from . import serializers



class AppointmentViewset(viewsets.ModelViewSet):
    queryset = models.Appointment.objects.all()
    serializer_class = serializers.AppointmentSerializer

    # custom query set 
    def get_queryset(self):
        queryset =  super().get_queryset()

        patient_id = self.request.query_params.get('patinet_id')

        if patient_id:
            queryset = queryset.filter(patient_id=patient_id)
        
        return queryset