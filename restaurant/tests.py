
from django.test import TestCase
from restaurant.models import Booking

# Create your tests here.



class BookingModelTestCase(TestCase):
    def setUp(self):
        # Set up any necessary data for the test case
        Booking.objects.create(first_name='John', reservation_date='2023-01-01', reservation_slot=1)

    def test_booking_str(self):
        # Test the string representation of the Booking model
        booking = Booking.objects.get(first_name='John')
        expected_str = 'John'
        self.assertEqual(str(booking), expected_str)

    def test_booking_fields(self):
         # Test the fields of the Booking model
        booking = Booking.objects.get(first_name='John')
        self.assertEqual(booking.first_name, 'John')
        self.assertEqual(str(booking.reservation_date), '2023-01-01')
        self.assertEqual(booking.reservation_slot, 1)
        