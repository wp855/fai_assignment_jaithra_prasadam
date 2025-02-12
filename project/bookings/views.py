from django.shortcuts import render

from rest_framework import generics
from .models import Booking
from .serializers import BookingSerializer

class BookingListCreateView(generics.ListCreateAPIView):
	queryset = Booking.objects.all()
	serializer_class = BookingSerializer

class BookingDetailView(generics.RetrieveDestroyAPIView):
	queryset = Booking.objects.all()
	serializer_class = BookingSerializer
	lookup_field = 'booking_id'
	