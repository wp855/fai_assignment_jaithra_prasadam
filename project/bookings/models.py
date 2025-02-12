from django.db import models
class Booking(models.Model):
	booking_id= models.CharField(max_length=100,unique = True)
	customer_name= models.CharField(max_length=100)
	booking_date = models.DateField()
	amount = models.DecimalField(max_digits=10, decimal_places=2)
	vendor = models.CharField(max_length=100)

	def __str__(self):
		return f"{self.booking_id} - {self.customer_name}"