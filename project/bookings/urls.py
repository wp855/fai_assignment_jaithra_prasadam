from django.urls import path
from .views import BookingListCreateView, BookingDetailView

urlpatterns = [
	path('bookings/',BookingListCreateView.as_view(), name = 'booking-list-create'),
	path('bookings/<str:booking_id>/',BookingDetailView.as_view(), name = 'booking-detail'),
]